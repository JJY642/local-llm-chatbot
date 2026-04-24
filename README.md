# Local LLM Chatbot

Django, PostgreSQL, Nginx, Docker Compose, Ollama를 이용한  
Local LLM 기반 채팅 웹 애플리케이션입니다.

## 프로젝트 개요

본 프로젝트는 외부 AI 서비스(ChatGPT, Gemini 등)를 사용하지 않고  
Local LLM을 활용하여 사용자의 데이터를 로컬 환경에서 처리하고 저장하는  
채팅 웹 애플리케이션입니다.

사용자는 웹 브라우저를 통해 AI와 대화할 수 있으며,  
모든 대화 기록은 PostgreSQL 데이터베이스에 저장됩니다.

---

## 기술 스택

- Django
- PostgreSQL
- Nginx
- Docker Compose
- Ollama (Local LLM)

---

## 실행 방법

### 1. 프로젝트 실행

```bash 
docker compose up -d --build

### 2. Local LLM 모델 설치 (필수)
본 프로젝트는 Ollama를 사용하며, 모델은 자동으로 포함되지 않습니다.
따라서 아래 명령어로 모델을 설치해야 합니다.

```bash
docker compose exec ollama ollama pull gemma4:e2b


### 3. 웹 접속

http://localhost

## 시스템 구조

브라우저 → Nginx → Django (Gunicorn) → PostgreSQL
                                 ↓
                              Ollama (LLM)

Nginx: 요청 수신 및 정적 파일 제공

Django: 웹 로직 처리 및 LLM 호출

PostgreSQL: 대화 데이터 저장

Ollama: Local LLM 실행


## 주요 기능

새로운 대화 생성

사용자 메시지 입력

Local LLM 응답 생성

대화 기록 저장 및 조회


## 데이터 저장 구조

Conversation: 대화방 정보

Message: 사용자 메시지 및 LLM 응답

## 주의 사항

최초 실행 시 반드시 LLM 모델을 설치해야 합니다.

모델 설치 전에는 채팅 기능이 정상적으로 동작하지 않습니다.

