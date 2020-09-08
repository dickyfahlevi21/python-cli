import click
import statistics
# Resources
# https://pythonforundergradengineers.com/statistics-in-python-using-the-statistics-module.html#:~:text=Summary,function%20you%20want%20to%20use.
# https://www.geeksforgeeks.org/fmean-function-in-python-statistics/

@click.group()
def cli():
    pass

@cli.command(name = "mean")
@click.argument("number", type = click.INT, nargs = -1)
def mean(number):
    result = statistics.mean(number)
    print(f'\nHasil mean: {result}\n')

@cli.command(name = "median")
@click.argument("number", type = click.INT, nargs = -1)
def median(number):
    result = statistics.median(number)
    print(f'\nHasil median: {result}\n')

@cli.command(name = "mode")
@click.argument("number", type = click.INT, nargs = -1)
def mode(number):
    result = statistics.mode(number)
    print(f'\nHasil mode: {result}\n')

@cli.command(name = "fmean")
@click.argument("number", type = click.INT, nargs = -1)
def fmean(number):
    result = statistics.fmean(number)
    print(f'\nHasil fmean: {result}\n')


if __name__ == '__main__':
    cli()

# How To Run in Terminal
# ON FOLDER PROJECT/
# python3 c_statistic.py mean 90 80 77 45 32 45
# python3 c_statistic.py median 10 2 4 5 9 12
# python3 c_statistic.py mode 3 5 8 0 9 8 3 0 8
# python3 c_statistic.py fmean 100 53 28 90 130