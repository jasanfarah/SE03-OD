FROM nginx:latest
RUN apt update && apt install openssl
COPY default.conf /etc/nginx/nginx.conf
COPY html /etc/nginx/html
COPY certs /etc/nginx/ssl