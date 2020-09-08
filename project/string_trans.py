import click

@click.group()
def transformation():
    pass

@transformation.command(name = "lowercase")
@click.argument("value", type = click.STRING)
def upper(value):
    print(value.lower())

@transformation.command(name = "uppercase")
@click.argument("value", type = click.STRING)
def lower(value):
    print(value.upper())

@transformation.command(name = "capitalize")
@click.argument("value", type = click.STRING)
def capital(value):
    print(value.title())


if __name__ == '__main__':
    transformation()

# How To Run in Terminal
# ON FOLDER PROJECT/
# python3 string_trans.py lowercase "I aM CrAzY TeXT"
# python3 string_trans.py uppercase "I aM CrAzY TeXT"
# python3 string_trans.py capitalize "I aM CrAzY TeXT"