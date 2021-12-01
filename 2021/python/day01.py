import AdventTools

input = AdventTools.ReadInput.inputToIntLIst()


def a():
    output = sum(input[i+1] > input[i] for i, r in enumerate(input[1:]))
    return output


def b():
    count = 0
    for i, r in enumerate(input[:-3]):
        iSumWindow = input[i] + input[i + 1] + input[i + 2]
        jSumWindow = input[i + 1] + input[i + 2] + input[i + 3]
        if jSumWindow > iSumWindow:
            count += 1
    return count


def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
