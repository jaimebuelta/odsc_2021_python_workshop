import csv
import click
import mistune
import matplotlib.pyplot as plt
from collections import defaultdict


@click.command()
@click.argument('file_in', type=click.File('r'))
@click.argument('template', type=click.File('r'))
@click.argument('file_out', type=click.File('w'))
def action(file_in, template, file_out):
    seasons = defaultdict(int)

    TEMPLATE = template.read()

    for row in csv.DictReader(file_in):
        season = row['Season']
        seasons[season] += 1

    # sort and write the result
    data = list(seasons.items())
    pos = list(range(len(data)))
    values = [value for label, value in data]
    labels = [label for label, value in data]
    plt.bar(pos, values)
    plt.xticks(pos, labels)

    figure = plt.gcf()
    figure.set_size_inches(10, 6)
    GRAPHIC = 'graphic.png'
    plt.savefig(GRAPHIC)

    context = {
        'header': 'The Simpsons seasons',
        'text': 'This is an automatic report generating a text '
                'and graph showing the number of episodes on '
                'each season of "The Simpsons"',
        'graph': GRAPHIC,
    }

    md_body = TEMPLATE.format(**context)

    # Transform from Markdown to HTML
    html_body = mistune.markdown(md_body)

    file_out.write(html_body)


if __name__ == '__main__':
    action()
