import AdventTools

input = AdventTools.ReadInput.inputToStrList()


def counterPart1(instructions):
    iterator = 0
    counter = 0
    usedIterators = []
    while (True):
        '''
        I have tried to implement a do while of sorts here, I'm sure there is
        a more pythonesque method of implimenting this. Requires further
        research.
        '''
        if usedIterators.count(iterator) > 1:
            break
        key = instructions[iterator][:3]
        value = int(instructions[iterator][4:])
        if key == 'acc':
            counter += value
            iterator += 1
        elif key == 'jmp':
            iterator += value
        elif key == 'nop':
            iterator += 1
        usedIterators.append(iterator)
        '''
        Even though the last elif could just be an else, I rather (intuitively)
        make it very clear what the code is actually checking for.
        Should see what that means in terms of run time, etc...
        '''
    return counter


def isValidInstructionsPart2(instructions):
    '''
    Even though adding an acc counter would be a minimal addition, it really
    doesn't need it. For really huge inputs it might be faster to skip that
    step.
    '''
    iterator = 0
    usedIterators = []
    while (True):
        key = instructions[iterator][:3]
        if key == 'jmp':
            value = int(instructions[iterator][4:])
            iterator += value
        else:
            iterator += 1
        if iterator == len(instructions):
            return True
        usedIterators.append(iterator)
        if usedIterators.count(iterator) > 1:
            return False


def counterPart2(instructions):
    iterator = 0
    counter = 0
    while (True):
        key = instructions[iterator][:3]
        value = int(instructions[iterator][4:])
        if key == 'acc':
            counter += value
            iterator += 1
        elif key == 'jmp':
            iterator += value
        elif key == 'nop':
            iterator += 1
        if iterator == len(instructions):
            return counter


def a():
    return counterPart1(input)


def b():
    for i, adress in enumerate(input):
        tempInstructions = input.copy()
        key = adress[:3]
        if key == 'jmp':
            tempInstructions[i] = 'nop' + adress[3:]
        elif key == 'nop':
            tempInstructions[i] = 'jmp' + adress[3:]
        else:
            continue
        if isValidInstructionsPart2(tempInstructions):
            return counterPart2(tempInstructions)


def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
