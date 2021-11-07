FROM python:3.9.7-slim-buster

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY:-AI4HUDpFhmJQWMCYsV3JM5np3hVRCeQ3}

WORKDIR /app

# set environment variables

# PYTHONDONTWRITEBYTECODE
# If this is set to a non-empty string, Python won’t try to write .pyc files on the import of source modules.
# This is equivalent to specifying the -B option.
ENV PYTHONDONTWRITEBYTECODE 1

# PYTHONUNBUFFERED
# If this is set to a non-empty string it is equivalent to specifying the -u option.
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN mkdir db
VOLUME db-vol
RUN python3 manage.py migrate

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["python3", "manage.py"]