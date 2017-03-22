FROM node
ENV MAGNET empty

#install webtorrent
RUN npm install -g webtorrent-cli@latest --save
# copy over runner script
ADD file.sh /tmp/
WORKDIR /Movies

#make it executable
RUN chmod +x /tmp/file.sh
ENTRYPOINT ["bash", "/tmp/file.sh"]