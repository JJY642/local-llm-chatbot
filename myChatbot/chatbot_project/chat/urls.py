from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversation_list, name='conversation_list'),
    path('chat/new/', views.conversation_new, name='conversation_new'),
    path('chat/<int:pk>/', views.chat_room, name='chat_room'),
    path('chat/<int:pk>/send/', views.send_message, name='send_message'),
    path('chat/<int:pk>/delete/', views.conversation_delete, name='conversation_delete'),
]
