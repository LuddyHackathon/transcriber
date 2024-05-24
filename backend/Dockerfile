FROM python:3.9-slim

RUN mkdir -p /home/python/transcriber

WORKDIR /home/python/transcriber

COPY requirements.txt ./

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y git && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 65535

ENTRYPOINT [ "python"]

CMD ["app.py"]
