with open('input.txt') as input:
    input = input.read()

houses = set()

coordinates = [0, 0]
robo_coordinates = [0, 0]

# Lol, there is a better way
for i, ele in enumerate(input):
    if (i % 2 == 0):
        if (ele == '>'):
            coordinates[0] += 1
        elif (ele == '^'):
            coordinates[1] += 1
        elif (ele == '<'):
            coordinates[0] -= 1
        elif (ele == 'v'):
            coordinates[1] -= 1
        houses.update([(tuple(coordinates))])
    else:
        if (ele == '>'):
            robo_coordinates[0] += 1
        elif (ele == '^'):
            robo_coordinates[1] += 1
        elif (ele == '<'):
            robo_coordinates[0] -= 1
        elif (ele == 'v'):
            robo_coordinates[1] -= 1
        houses.update([(tuple(robo_coordinates))])

print(len(houses))
