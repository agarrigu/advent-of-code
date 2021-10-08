import AdventTools


def findSum2020(list):
    for i in list:
        for j in list:
            if (i + j == 2020):
                return [i, j]


def findSumThree2020(list):
    for i in list:
        for j in list:
            for k in list:
                if (i + j + k == 2020):
                    return [i, j, k]
                        # This amount of nesting is getting dangerous
                            # TODO find a better way,
                                # maybe something recursive?


input = AdventTools.ReadInput.inputToIntList()


def a():
    output = findSum2020(input)
    return output[0] * output[1]


def b():
    output = findSumThree2020(input)
    return output[0] * output[1] * output[2]


def main():
    print(b())


if __name__ == '__main__':
    main()
