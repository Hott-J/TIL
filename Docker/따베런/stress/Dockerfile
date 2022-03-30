FROM debian
MAINTAINER hakjae chung <jhj13062015@gmail.com>
RUN apt-get update; apt-get install stress -y
CMD ["/bin/sh", "-c", "stress -c 2"]