web: gunicorn django_fedorchuk.wsgi --log-file -
worker: celery -A django_fedorchuk worker -l info -B
