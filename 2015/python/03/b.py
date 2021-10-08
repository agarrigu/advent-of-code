# I got the santasTurn idea from Mo Beigi https://mobeigi.com/blog/category/capture-the-flag/advent-of-code/
# They used it reluctantly but I really liked it.
with open('input.txt') as input:
    input = input.read()

houses = set()

coordinates = [0, 0]
robo_coordinates = [0, 0]
santasTurn = True

for i, ele in enumerate(input):
    if (ele == '>'):
        coordinates[0] += int(santasTurn)
        robo_coordinates[0] += int(not santasTurn)
    elif (ele == '^'):
        coordinates[1] += int(santasTurn)
        robo_coordinates[1] += int(not santasTurn)
    elif (ele == '<'):
        coordinates[0] -= int(santasTurn)
        robo_coordinates[0] -= int(not santasTurn)
    elif (ele == 'v'):
        coordinates[1] -= int(santasTurn)
        robo_coordinates[1] -= int(not santasTurn)

    if (santasTurn):
        houses.update([(tuple(coordinates))])
    else:
        houses.update([(tuple(robo_coordinates))])

    santasTurn = not santasTurn

print(len(houses))
