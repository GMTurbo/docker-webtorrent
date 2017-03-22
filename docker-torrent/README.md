# Docker-Webtorrent - for distributed torrent seeding

### to run
```git clone https://github.com/GMTurbo/docker-webtorrent.git```
```sh
cd <repo>
chmod 755 ./download
./download [it, d] <magnetlink>
#it = iterative mode
#d = daemon mode
```
## A handly command
```bash
alias dl="bash {path_to_repo}/download"
```

## show me
```bash
#download a torrent in a docker container, run as a daemon
dl d "magnet:?xt=urn:btih:1cd457e8a37fdbf93a933aafa06c14e06f07fc0c&dn=Its.
Always.Sunny.in.Philadelphia.S12E01.720p.HDTV.x264-AVS&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%
3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2
Fpublic.popcorn-tracker.org%3A6969"
```