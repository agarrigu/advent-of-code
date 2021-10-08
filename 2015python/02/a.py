with open('input.txt') as input:
    input = input.read().splitlines()

box_dimensions = []
for element in input:
    box_dimensions.append([int(i) for i in element.split('x')])

for element in box_dimensions:
    element.sort()

answer = 0
for element in box_dimensions:
    l = int(element[0])
    w = int(element[1])
    h = int(element[2])
    answer += 2 * (l*w + w*h + l*h) + l*w

print(answer)
