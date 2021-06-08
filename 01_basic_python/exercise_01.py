import click
import math


@click.command()
@click.argument('function')
@click.argument('value', type=int)
def action(function, value):
    function = function.upper()
    if function == 'SIN':
        method = math.sin
    elif function == 'COS':
        method = math.cos
    elif function == 'TAN':
        method = math.tan

    result = method(math.radians(value))
    click.echo(f'{function}({value}) = {result}')


if __name__ == '__main__':
    action()
