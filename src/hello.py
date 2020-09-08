import click


@click.group()
def cli():
    pass

@cli.command(name = "hello")
def hello():
    click.echo('Hello World!')


if __name__ == '__main__':
    hello()