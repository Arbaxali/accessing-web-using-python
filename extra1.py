import re
handle = open('extra2.txt')
numbers = 0
for line in handle:
    line = line.rstrip()
    numbers = numbers + sum(map(lambda x: int(x), re.findall('([0-9]+)', line)))

print(numbers)
