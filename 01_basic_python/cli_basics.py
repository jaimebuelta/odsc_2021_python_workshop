import click
import time


@click.command()
@click.argument('number', type=int)
@click.option('--text', default='EXAMPLE')
def main(number, text):
    for _ in range(number):
        click.echo(click.style('echo ', fg='green') + text)
        time.sleep(.2)


if __name__ == '__main__':
    main()
