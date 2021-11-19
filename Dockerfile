FROM ubuntu

WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate


# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["python3", "manage.py"]