'''
Given input as {forward|down|up n} where each element is a change in possition:
Part 1: What do you get if you multiply your final horizontal position by your final depth?
Part 2: Where `down n` and `up n` is a chnage in aim and 
`forward n` is horizontal direction and `forward n` * aim is depth:
    What do you get if you multiply your final horizontal position by your final depth?
'''
import AdventTools

input = AdventTools.ReadInput.inputToStrList('\n')


def convertInputToTable(input):
    a = [command.split() for command in input[:-1]]
    b = [(command[0], int(command[1])) for command in a]
    return b


instructions = convertInputToTable(input)


def a():
    xpos = 0
    ypos = 0
    for c in instructions:
        if c[0] == 'forward':
            xpos += c[1]
        elif c[0] == 'down':
            ypos += c[1]
        elif c[0] == 'up':
            ypos -= c[1]
    return xpos * ypos


def b():
    xpos = 0
    ypos = 0
    aim = 0
    for c in instructions:
        if c[0] == 'down':
            aim += c[1]
        elif c[0] == 'up':
            aim -= c[1]
        else:
            xpos += c[1]
            ypos += c[1] * aim
    return xpos * ypos


def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
