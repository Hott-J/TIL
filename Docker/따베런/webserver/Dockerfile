FROM ubuntu:18.04
LABEL maintainer = "hottj <jhj13062015@gmail.com>"
# install apache
RUN apt-get update \
	&& apt-get install -y apache2
# 도커파일 한 라인당 레이어 하나이므로 apt-get을 &&로 합쳐서 레이어를 줄인다
RUN echo "TEST WEB" > /var/www/html/index.html
# 아파치웹은 /var/www/html 디폴트로 여기에 저장한다
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]


