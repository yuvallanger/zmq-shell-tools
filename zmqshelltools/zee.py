import sys

import click
import zmq


@click.command()
@click.argument('address')
def main(address):
    """foo"""
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUSH)
    socket.bind(address)

    for line in sys.stdin:
        socket.send(line.encode())

    socket.close()

if __name__ == '__main__':
    main()
