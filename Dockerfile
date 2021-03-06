FROM python:3.9.7-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["python3", "manage.py"]