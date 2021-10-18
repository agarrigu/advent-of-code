import AdventTools
input = AdventTools.ReadInput.inputToStrList()


def calcBSP(bsp, add):
    output = 0
    s = 1
    reverse = bsp[::-1]
    for d in reverse:
        if d == add:
            output += s
        s *= 2
    return output

def calcColumn(seat):
    return calcBSP(seat[7:], 'R')

def calcRow(seat):
    return calcBSP(seat[:7], 'B')

def calcSeatID(seat):
    return calcRow(seat) * 8 + calcColumn(seat)

def allSeatIDs(seats):
    allSeatIDs = [calcSeatID(seat) for seat in seats]
    allSeatIDs.sort()
    return allSeatIDs

allSeatIDs = allSeatIDs(input)
def a():
    return allSeatIDs[-1]


def b():
    for i, id in enumerate(allSeatIDs):
        if id + 1 != allSeatIDs[i + 1]:
            return id + 1



def main():
    print(a())
    print(b())

if __name__ == '__main__':
    main()
