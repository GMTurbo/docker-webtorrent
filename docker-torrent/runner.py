import sys
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
    parser.add_argument('-rb', '--rebuild', dest='rebuild',
                        action='store_true')
    parser.set_defaults(rebuild=False, detach=True)
    return parser.parse_args()


CONFIG = parse_args()

CLIENT = docker.from_env()

if CONFIG.rebuild is True:
    print CLIENT.images.build(path=".")

print "CLIENT.containers.run(\"{i}\", \"{t}\", detach={d})".format(
    i=CONFIG.image,
    t=CONFIG.torrent,
    d=CONFIG.detach
)

print CLIENT.containers.run(
    CONFIG.image,
    CONFIG.torrent,
    detach=CONFIG.detach
)
