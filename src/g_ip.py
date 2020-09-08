import click
import socket

@click.group()
def cli():
    pass

@cli.command(name="ip_internal")
def ip_internal():
    print(f"IP Internal: {socket.gethostbyname(socket.gethostname())}")

if __name__ == '__main__':
    cli()


# How To Run in Terminal
# ON FOLDER PROJECT
# python3 g_ip.py ip_internal
# Resources
# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib