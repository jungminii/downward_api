FROM python:3.9-slim

# curl 설치하여 통신
RUN apt-get update && apt-get install -y curl

# Flask와 필요한 패키지 설치
WORKDIR /app
COPY requirements.txt . #Flask cors 설치
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
