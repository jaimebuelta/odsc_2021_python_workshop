from collections import namedtuple


City = namedtuple('City', 'name, population, area_km2')


dublin = City(name='Dublin', population=554_554, area_km2=117.8)
toledo = City(name='Toledo', population=84_282, area_km2=232.1)


print(dublin)
print(toledo)
