FROM python:3.9-slim

RUN mkdir -p /home/python/transcriber

WORKDIR /home/python/transcriber

COPY requirements.txt ./

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y git p7zip-full ffmpeg wget && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/Purfview/whisper-standalone-win/releases/download/Faster-Whisper-XXL/Faster-Whisper-XXL_r245.2_linux.7z

RUN 7z x Faster-Whisper-XXL_r245.2_linux.7z

RUN rm Faster-Whisper-XXL_r245.2_linux.7z

RUN chmod +x Faster-Whisper-XXL/faster-whisper-xxl

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 65535

ENTRYPOINT [ "python"]

CMD ["app.py"]
