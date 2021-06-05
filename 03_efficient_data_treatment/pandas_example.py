import pandas as pd
from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class City:
    name: str
    population: int
    area_km2: float

    def pandas(self):
        data = {
            'name': self.name,
            'population': pd.to_numeric(self.population),
            'area_km2': pd.to_numeric(self.area_km2),
        }
        return data


cities = [
    City(name='Dublin', population=554_554, area_km2=117.8),
    City(name='Toledo', population=84_282, area_km2=232.1),
]


data = pd.DataFrame(city.pandas() for city in cities)
print(data)
data = data.set_index('name')
print(data)

# Create a figure to store the graph
fig, axs = plt.subplots(figsize=(12, 8))

# Create a bar graph in that area
data['population'].plot.bar(ax=axs)
plt.title('Population')

# Save the result in a png
fig.savefig('cities_population.png')

# Aggregate results
result = data.agg(['sum', 'count'])
print(result)
