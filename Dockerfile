FROM python:3.12.0b1-slim-buster

RUN pip3 install -r requirements.txt

ENV CHANNEL_ACCESS_TOKEN ""
ENV CHANNEL_SECRET ""
ENV CHANNEL_USERID ""
ENV CALLBACK_DOMAIN ""
ENV STARTURL ""

ENTRYPOINT ["/usr/local/bin/python3", "main.py"]