import AdventTools
import re


class Password:
    def __init__(self, min, max, letter, password):
        self.min = min
        self.max = max
        self.letter = letter
        self.password = password

    def isValidPasswordPart1(self):
        if (self.min <= self.password.count(self.letter) <= self.max):
            return True
        return False

    def isValidPasswordPart2(self):
        try:
            indexOne = self.password[self.min - 1]
            condition1 = indexOne == self.letter
        except:
            condition1 = False
        try:
            indexTwo = self.password[self.max - 1]
            condition2 = indexTwo == self.letter
        except:
            condition2 = False
        # TODO There has to be a better way, try again when not drunk XD
        # Look for method that doesn't care if index out of bound
        if (condition1 ^ condition2):
            return True
        return False


def convertStringToPassword(string):
    min, max, letter, password = re.search(r'(\d+)-(\d+) (\w): (\w+)', string).groups()
    return Password(int(min), int(max), letter, password)


def solveProblem(input, validationMethod):
    validPasswords = 0
    for n in input:
        if (convertStringToPassword(n).validationMethod()):
            validPasswords += 1
    return validPasswords


input = AdventTools.ReadInput.inputToStrList()


def a():
    return solveProblem(input, Password.isValidPasswordPart1)


def b():
    return solveProblem(input, Password.isValidPasswordPart2)


def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
