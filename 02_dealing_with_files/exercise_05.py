import fpdf
import csv
import click
import matplotlib.pyplot as plt
from collections import defaultdict


@click.command()
@click.argument('file_in', type=click.File('r'))
@click.argument('file_out', type=click.Path())
def action(file_in, file_out):

    seasons = defaultdict(int)

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

    figure = plt. gcf()
    figure. set_size_inches(10, 6)
    GRAPHIC = 'graphic.png'
    plt.savefig(GRAPHIC)

    document = fpdf.FPDF()
    document.set_font('Times', 'B', 14)
    document.add_page()

    document.cell(0, 5, 'The Simpsons seasons')
    document.ln()

    text = ('This is an automatic report generating a text '
            'and graph showing the number of episodes on '
            'each season of "The Simpsons"')
    document.set_font('Times', '', 14)
    document.multi_cell(0, 5, text)
    document.ln()

    # Add the image
    document.image(GRAPHIC, w=200)

    # Add some text afterwards
    document.multi_cell(0, 5, 'Footer')
    document.ln()

    document.output(file_out)


if __name__ == '__main__':
    action()
