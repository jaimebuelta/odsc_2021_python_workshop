import csv
import click
from collections import defaultdict


@click.command()
@click.argument('file_in', type=click.File('r'))
@click.argument('file_out', type=click.File('w'))
def action(file_in, file_out):

    seasons = defaultdict(int)

    for row in csv.DictReader(file_in):
        season = row['Season']
        seasons[season] += 1

    # sort and write the result
    writer = csv.DictWriter(file_out, fieldnames=['Season', 'Episodes'])
    writer.writeheader()
    for season, episodes in seasons.items():
        data = {
            'Season': season,
            'Episodes': episodes,
        }
        writer.writerow(data)


if __name__ == '__main__':
    action()
