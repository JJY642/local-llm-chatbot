from django.shortcuts import render

# Create your views here.
import os
import requests

from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation, Message


def call_local_llm(prompt):
    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")

    try:
        response = requests.post(
            f"{ollama_url}/api/generate",
            json={
                "model": os.getenv("OLLAMA_MODEL", "llama3.2:1b"),
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get("response", "응답을 생성하지 못했습니다.")

    except requests.exceptions.RequestException as e:
        return f"Local LLM 연결 실패: {e}"


def conversation_list(request):
    conversations = Conversation.objects.order_by("-created_at")
    return render(request, "conversation_list.html", {
        "conversations": conversations
    })


def conversation_new(request):
    conversation = Conversation.objects.create(title="새 대화")
    return redirect("chat_room", pk=conversation.pk)


def chat_room(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    messages = conversation.messages.order_by("created_at")

    return render(request, "chat_room.html", {
        "conversation": conversation,
        "messages": messages,
    })


def send_message(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)

    if request.method == "POST":
        user_text = request.POST.get("message", "").strip()

        if user_text:
            Message.objects.create(
                conversation=conversation,
                sender="user",
                content=user_text,
            )

            if conversation.title == "새 대화":
                conversation.title = user_text[:30]
                conversation.save()

            bot_reply = call_local_llm(user_text)

            Message.objects.create(
                conversation=conversation,
                sender="bot",
                content=bot_reply,
            )

    return redirect("chat_room", pk=conversation.pk)


def conversation_delete(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)

    if request.method == "POST":
        conversation.delete()
        return redirect("conversation_list")

    return render(request, "conversation_confirm_delete.html", {
        "conversation": conversation
    })
