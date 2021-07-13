with open('input.txt') as input:
    input = input.read()

houses = set()

coordinates = [0, 0]

for ele in input:
    if (ele == '>'):
        coordinates[0] += 1
    elif (ele == '^'):
        coordinates[1] += 1
    elif (ele == '<'):
        coordinates[0] -= 1
    elif (ele == 'v'):
        coordinates[1] -= 1

    houses.update([(tuple(coordinates))])

print(len(houses))
