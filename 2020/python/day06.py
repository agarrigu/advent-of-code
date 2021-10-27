import AdventTools
import sys

sys.setrecursionlimit(26)

input = AdventTools.ReadInput.inputToStrList('\n\n')
input[- 1] = input[- 1].rstrip('\n')

def findIntersections(form):
    '''
    I'm having problems implemntig this recursive function,
    I'm going to insist in this method to continue learning recursion
    but I'm going to move on for a while and come back to it.
    Part 1 works perfectly.
    '''
    output = ""
    if not form:
        return
    thePop = form.pop()
    print(output, thePop, len(form), form)
    output += thePop in findIntersections(form)

def a():
    forms = [set(form.replace('\n', '')) for form in input]
    output = 0
    for form in forms:
        output += len(form)
    return output

def b():
    forms = [form.split('\n') for form in input]
    bigYes = 0
    for form in forms:
        bigYes += len(findIntersections(form))
    return bigYes

def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
