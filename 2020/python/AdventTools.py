class AdventTools:

    @staticmethod
    def inputToString():
        with open('input.txt', 'r') as file:
            input = file.read()
        return input

    def inputToInt():
        with open('input.txt', 'r') as file:
            input = file.read()
        return int(input)

    @staticmethod
    def inputToStrList():
        with open('input.txt', 'r') as file:
            input = file.read().splitlines()
        return input

    @staticmethod
    def inputToIntLIst():
        with open('input.txt', 'r') as file:
            input = file.read().splitlines()
        return [int(i) for i in input]


def main():
    a = AdventTools.inputToString()
    b = AdventTools.inputToStrList()
    c = AdventTools.inputToIntLIst()
    d = AdventTools.inputToInt()
    print(type(a), type(b),type(c),type(d))


if __name__ == "__main__":
    main()
