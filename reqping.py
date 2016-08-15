import sys
import logging

import zmq
import click


logging.basicConfig(level=logging.DEBUG)

@click.command()
@click.option('--address')
@click.option('--sender')
def main(address, sender):
    """foo"""

    logging.info(address, sender)

    ctx = zmq.Context()
    socket = ctx.socket(zmq.REQ)
    socket.connect(address)

    k = 0
    while True:
        message = "Message {} from {}".format(k, sender)
        logging.info(message)
        socket.send(message.encode())
        logging.info(socket.recv().decode())
        k += 1

    socket.close()


if __name__ == '__main__':
    main()
