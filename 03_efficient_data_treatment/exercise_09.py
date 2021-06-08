import csv
import pandas as pd
import matplotlib.pyplot as plt
import click


@click.command()
@click.argument('csv_in', type=click.Path())
@click.argument('png_out', type=click.Path())
def main(csv_in, png_out):
    # with open(csv_in) as fp:
    #     input_data = csv.DictReader(fp)
    #     data = pd.DataFrame(input_data)

    data = pd.read_csv(csv_in)
    # Transform the seasons to integer
    data.Season = data.Season.astype(int)

    grouped = data.groupby('Season')['Episode']
    result = grouped.agg(['count'])

    # Create a figure to store the graph
    fig, axs = plt.subplots(figsize=(12, 8))

    # Create a bar graph in that area
    result['count'].plot.bar(ax=axs)
    plt.title('Episodes per season')

    # Save the result in a png
    fig.savefig(png_out)


if __name__ == '__main__':
    main()
