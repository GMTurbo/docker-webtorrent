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

Python
-
Ok, so i have a new python script that runs this.
```bash
python runner.py -t "magnet:?xt=urn:btih:01b16f3b713d25914dc847c502fc4b6afbad9950&dn=Its.Always.Sunny.in.P
hiladelphia.S12E10.720p.HDTV.x264-AVS&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Ftracker.c
oppersurfer.tk%3A6969&tr=udp%3A%2F%2Fpublic.popcorn-tracker.org%3A6969" --verbose --rebuild
```

```python
python runner.py --help                                          
usage: runner.py [-h] [-t [TORRENT]] [-v [VOLUME]] [-i [IMAGE]] [-d] [-a]
                 [-rb] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  -t [TORRENT], --torrent [TORRENT]
  -v [VOLUME], --volume [VOLUME]
  -i [IMAGE], --image [IMAGE]
  -d, --detach
  -a, --attach
  -rb, --rebuild
  --verbose
```
