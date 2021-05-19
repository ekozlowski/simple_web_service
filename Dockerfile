FROM python:3.9

RUN mkdir /app
WORKDIR /app
ADD app.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "uvicorn", "app:app", "--reload", "--host", "0.0.0.0" ]