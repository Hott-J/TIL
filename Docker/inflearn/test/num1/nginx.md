$ docker run -d --rm \
  -p 50000:80 \
  -v $(pwd)/index.html:/usr/share/nginx/html/index.html \
  nginx