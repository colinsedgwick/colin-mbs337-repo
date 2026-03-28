FROM python:3.12

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY app.py .

CMD ["python3", "app.py"]