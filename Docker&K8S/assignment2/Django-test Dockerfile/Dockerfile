FROM python:latest
RUN pip install django
RUN pip install Pillow
RUN pip install django-extensions
RUN pip install django-bulma
WORKDIR /usr/src/app
COPY . .
WORKDIR ./workdir2
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
EXPOSE 8000

