from subprocess import Popen, PIPE
import logging

import click
import zmq


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option('--bind', default='tcp://127.0.0.1:9000')
@click.option('--command', default='cat')
def main(bind, command):
    ctx = zmq.Context()
    socket = ctx.socket(zmq.REP)
    socket.bind(bind)
    logging.info('Bound to {}'.format(bind))

    while True:
        # Not line by line ATM.
        # It'd be nice but probably not sane.
        proc = Popen(command, bufsize=1, stdin=PIPE, stdout=PIPE)
        input = socket.recv()  # XXX Multiparts?
        output, _ = proc.communicate(input)
        socket.send(output)

    socket.close()


if __name__ == '__main__':
    main()
