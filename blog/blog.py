with open('example.txt') as file:
    numbers = [int(line) for line in file]

average = sum(numbers) / len(numbers)

with open('result.txt', 'w') as file:
    file.write(f'Average: {average}')
