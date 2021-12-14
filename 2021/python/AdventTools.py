class ReadInput:

    @staticmethod
    def inputToString():
        with open('input.txt', 'r') as file:
            input = file.read()
        return input

    @staticmethod
    def inputToInt():
        with open('input.txt', 'r') as file:
            input = file.read()
        return int(input)

    @staticmethod
    def inputToStrList(separator):
        with open('input.txt', 'r') as file:
            input = file.read().split(separator)
        return input

    @staticmethod
    def inputToIntLIst():
        with open('input.txt', 'r') as file:
            input = file.read().splitlines()
        return [int(i) for i in input]


def main():
#    a = ReadInput.inputToString()
#    b = ReadInput.inputToStrList()
#    c = ReadInput.inputToIntLIst()
#    d = ReadInput.inputToInt()
    e = ReadInput.inputToStrList('\n\n')
    print(e)


if __name__ == "__main__":
    main()
