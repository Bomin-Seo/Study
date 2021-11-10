FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y nginx
RUN echo "test site"
WORKDIR /etc/nginx
CMD ["nginx","-g","daemon off;"]
EXPOSE 80