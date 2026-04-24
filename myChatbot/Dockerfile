FROM python:3.11.6

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /usr/src/app/chatbot_project

EXPOSE 8000

CMD ["../entrypoint.sh"]
