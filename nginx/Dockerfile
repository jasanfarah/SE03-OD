FROM nginx:latest
RUN apk upgrade --update-cache --available && \apk add openssl
COPY default.conf /etc/nginx/nginx.conf
COPY html /etc/nginx/html
COPY certs /etc/nginx/ssl