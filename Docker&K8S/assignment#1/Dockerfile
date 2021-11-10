FROM python:latest
RUN pip3 install django
WORKDIR /usr/src/app
COPY . .
WORKDIR ./mytestsite
CMD ["python3","manage.py","runserver","0:8000"]
EXPOSE 8000

