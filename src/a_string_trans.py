import click

@click.group()
def cli():
    pass

@cli.command(name = "lowercase")
@click.argument("value", type = click.STRING)
def lower(value):
    print(value.lower())

@cli.command(name = "uppercase")
@click.argument("value", type = click.STRING)
def upper(value):
    print(value.upper())

@cli.command(name = "capital")
@click.argument("value", type = click.STRING)
def capital(value):
    print(value.title())


if __name__ == '__main__':
    cli()

# How To Run in Terminal
# ON FOLDER PROJECT/
# python3 a_string_trans.py lowercase "I aM CrAzY TeXT"
# python3 a_string_trans.py uppercase "I aM CrAzY TeXT"
# python3 a_string_trans.py capitalize "I aM CrAzY TeXT"