'''
Given input like `192\n208\n200\n243\n` where each element is a measurment:
Part 1: How many measurements are larger than the previous measurement?
Part 2: Considering the sums of a three-measurement sliding window:
    How many sums are larger than the previous sum?
'''
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
