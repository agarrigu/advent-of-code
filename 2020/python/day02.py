import AdventTools
import re


class Password:
    def __init__(self, min, max, letter, password):
        self.min = min
        self.max = max
        self.letter = letter
        self.password = password

    def isValidPassword(self):
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


input = AdventTools.ReadInput.inputToStrList()


# TODO a() and b() are practically the same, make function
def a():
    validPasswords = 0
    for n in input:
        if (convertStringToPassword(n).isValidPassword()):
            validPasswords += 1
    output = validPasswords
    return output


def b():
    validPasswords = 0
    for n in input:
        if (convertStringToPassword(n).isValidPasswordPart2()):
            validPasswords += 1
    output = validPasswords
    return output


def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
