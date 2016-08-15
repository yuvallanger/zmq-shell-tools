import zmq
import click


@click.command()
@click.argument('addresses', nargs=-1)
def main(addresses):
    """foo"""
    ctx = zmq.Context()
    sockets = []

    for addr in addresses:
        socket = ctx.socket(zmq.PULL)
        socket.connect(addr)
        sockets.append(socket)

    try:
        while True:
            rsocks, _, _ = zmq.select(sockets, [], [], 125)
            for sock in rsocks:
                print(sock.recv().decode(), end='')

    except KeyboardInterrupt:
        for socket in sockets:
            socket.close()


if __name__ == '__main__':
    main()
