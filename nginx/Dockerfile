FROM nginx:1.13-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY site.crt /etc/nginx/ssl
COPY jasan.dk.key /etc/nginx/ssl 
COPY /html /etc/nginx/html