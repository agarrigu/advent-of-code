import AdventTools

input = AdventTools.ReadInput.inputToIntLIst()


def a():
    output = sum(input[i+1] > input[i] for i, r in enumerate(input[1:]))
    return output


def b():
    output = sum(input[i+3] > input[i] for i, r in enumerate(input[:-3]))
    return output
    '''
    oh boy santa, I don't think this is a much more thorough sweep. You should
    redo your maths.
    '''

def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
