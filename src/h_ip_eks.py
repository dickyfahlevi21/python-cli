import click
import urllib.request


@click.group()
def cli():
    pass

@cli.command(name="ip_eksternal")
def ip_eksternal():
    print(f"IP Eksternal : {urllib.request.urlopen('https://ident.me').read().decode('utf8')}")


if __name__ == '__main__':
    cli()


# How To Run in Terminal
# ON FOLDER PROJECT
# python3 h_ip.py ip_eksternal
# Resources
# https://stackoverflow.com/questions/2311510/getting-a-machines-external-ip-address-with-python