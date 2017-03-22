FROM node

#install webtorrent
RUN npm install -g webtorrent-cli@latest --save
# copy over runner script
ADD file.sh /tmp/
ADD test.sh /tmp/
WORKDIR /Movies

#make it executable
RUN chmod +x /tmp/file.sh
RUN chmod +x /tmp/test.sh
#ENTRYPOINT ["bash", "/tmp/file.sh"]