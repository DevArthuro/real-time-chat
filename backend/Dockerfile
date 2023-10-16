FROM python:3.11.5-alpine3.18

WORKDIR /home/src

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]