from collections import deque

WINDOW_SIZE = 3

with open('average_values.txt') as fp:
    values = [int(line) for line in fp]

averages = []


average_window = deque([], WINDOW_SIZE)

for value in values:
    average_window.append(value)
    if len(average_window) < WINDOW_SIZE:
        avg = None
    else:
        avg = int(sum(d for d in average_window) / len(average_window))

    averages.append(avg)


# Print the results
print(', '.join(str(value) for value in values))
print(', '.join(str(value) if value else '  ' for value in averages))
