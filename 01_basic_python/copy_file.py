import click


@click.command()
@click.argument('file_in', type=click.File('r'))
@click.argument('file_out', type=click.File('w'))
def action(file_in, file_out):
    for line in file_in:
        file_out.write(line)


if __name__ == '__main__':
    action()
