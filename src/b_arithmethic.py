import click
import functools #for reduce


@click.group()
def cli():
    pass

# input must be integer
# nargs = -1 for input will be infinite
@cli.command(name = "add")
@click.argument("number", type = click.INT, nargs = -1)
def add(number:int):
    print(functools.reduce(lambda a,b : a + b, number))

@cli.command(name = "subtract")
@click.argument("number", type = click.INT, nargs = -1)
def subtract(number:int):
    print(functools.reduce(lambda a,b : a - b, number))

@cli.command(name = "multiply")
@click.argument("number", type = click.INT, nargs = -1)
def multiply(number:int):
    print(functools.reduce(lambda a,b : a * b, number))

@cli.command(name = "divide")
@click.argument("number", type = click.INT, nargs = -1)
def divide(number:int):
    print(int(functools.reduce(lambda a,b : a / b, number)))


if __name__ == '__main__':
    cli()

# How To Run in Terminal
# ON FOLDER PROJECT/
# python3 b_arithmethic.py add 1 4 5 2 3
# python3 b_arithmethic.py subtract 10 2 4
# python3 b_arithmethic.py multiply 3 5 8
# python3 b_arithmethic.py divide 100 5 2