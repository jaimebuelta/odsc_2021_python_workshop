import sh


# awk -F "\"*,\"*" '{print $1}' simpsons_data.csv | uniq -c

result = sh.uniq(sh.awk('-F', '\"*,\"*', '{print $1}', 'simpsons_data.csv'),
                 '-c')
seasons = {}

for line in result:
    if 'Season' in line:
        continue

    number, season = line.split()
    seasons[season] = int(number)

print(seasons)
print(sum(seasons.values()))
