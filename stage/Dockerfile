FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    python3 \
    python3-tk \
    python3-pip \
    && apt clean

WORKDIR /app

COPY app/ /app/

CMD ["python3", "main.py"]