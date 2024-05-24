FROM python:3.9-alpine

RUN mkdir -p /home/python/transcriber

WORKDIR /home/python/transcriber

COPY requirements.txt ./

RUN apk update && apk add --no-cache git

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 65535

ENTRYPOINT [ "python"]

CMD ["app.py"]
