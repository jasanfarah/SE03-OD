FROM nginx:1.13-alpine
COPY /certs/site.crt /etc/nginx/ssl/
COPY /certs/jasan.key /etc/nginx/ssl/ 
COPY /certs/rootCA.pem /etc/nginx/ssl/ 
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY /html /etc/nginx/html
