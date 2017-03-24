FROM mhart/alpine-node:latest

RUN apk add --no-cache bash 
RUN apk add --no-cache python
RUN apk add --no-cache make
RUN apk add --no-cache g++
# copy over runner script
ADD docker_requirements /tmp
#install webtorrent
WORKDIR /Movies

RUN npm install -g webtorrent-cli@latest --save

#make it executable
RUN chmod +x /tmp/file.sh
RUN chmod +x /tmp/test.sh
ENTRYPOINT ["bash", "/tmp/file.sh"]