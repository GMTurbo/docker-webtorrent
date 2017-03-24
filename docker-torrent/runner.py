import sys
import os
import docker
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--torrent', nargs='?', default="", type=str)
    parser.add_argument('-v', '--volume', nargs='?',
                        default="~/movies", type=str)
    parser.add_argument('-i', '--image', nargs='?',
                        default="torrent_downloader", type=str)
    parser.add_argument('-d', '--detach', dest='detach', action='store_true')
    parser.add_argument('-a', '--attach', dest='detach', action='store_false')
    parser.add_argument('-rb', '--rebuild', dest='rebuild',
                        action='store_true')
    parser.add_argument('--verbose', dest='verbose',
                        action='store_true')
    parser.set_defaults(rebuild=False, detach=True, verbose=False)
    return parser.parse_args()


CONFIG = parse_args()

if CONFIG.verbose is True:
    print CONFIG

CLIENT = docker.from_env()

if CONFIG.rebuild is True:
    pwd = os.getenv("PWD")
    if CONFIG.verbose is True:
        print pwd
    print CLIENT.images.build(path=pwd, tag="torrent_downloader")

if CONFIG.verbose is True:
    print "CLIENT.containers.run(\"{i}\", \"{t}\", detach={d},\
volumes=({v}: ('bind': '/Movies', 'mode': 'rw')".format(
        i=CONFIG.image,
        t=CONFIG.torrent,
        d=CONFIG.detach,
        v=CONFIG.volume
)

print CLIENT.containers.run(
    CONFIG.image,
    CONFIG.torrent,
    detach=CONFIG.detach,
    volumes={os.path.expanduser(CONFIG.volume): {'bind': '/Movies', 'mode': 'rw'}},
    remove=not CONFIG.detach
)
