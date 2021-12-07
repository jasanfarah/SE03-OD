FROM nginx:1.13-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY certs/site.crt /etc/nginx/ssl
COPY certs/jasan.key /etc/nginx/ssl 
COPY /html /etc/nginx/html