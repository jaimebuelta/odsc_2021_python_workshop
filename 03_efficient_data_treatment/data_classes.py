from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int
    area_km2: float
    capital: bool = False


dublin = City(name='Dublin', population=554_554, area_km2=117.8, capital=True)
toledo = City(name='Toledo', population=84_282, area_km2=232.1)
bad = City(name='Toledo', population='84_282', area_km2=232.1)


print(dublin)
print(toledo)
print(bad)
