import AdventTools


def path(map, right, down):
    totalTrees = 0
    mapPatternSize = len(map[0])
    for i, row in enumerate(map):
        if i % down != 0:
            continue
        x = i * right
        possition = x % mapPatternSize
        if row[possition] == '#':
            totalTrees += 1
    return totalTrees


input = AdventTools.ReadInput.inputToStrList()


def a():
    return path(input, 3, 1)


def b():
    a = path(input, 1, 1)
    b = path(input, 3, 1)
    c = path(input, 5, 1)
    d = path(input, 7, 1)
    e = path(input, 1, 2)
    return a * b * c * d * e


def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
