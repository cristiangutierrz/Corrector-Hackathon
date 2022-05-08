FROM fholzer/nginx-brotli:v1.12.0
WORKDIR /etc/nginx
ADD nginx.conf /etc/nginx/nginx.conf

COPY . /usr/share/nginx/html
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]