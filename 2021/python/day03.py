import AdventTools

input = AdventTools.ReadInput.inputToStrList('\n')


mag = len(input[0])
input = [int(b, 2) for b in input[:-1]]

def a():
    size = len(input)
    gamma = 0
    for i in range(mag):
        mask = pow(2, i)
        count = sum(w & mask == mask for w in input)
        if count > size/2:
            gamma += mask
    epsilon = gamma ^ 0xFFF
    # Need to find a dynamic way to get 0xFFF
    return gamma * epsilon


def b():
    oxygen = input.copy()
    for i in range(mag -1, -1, -1):
        size = len(oxygen)
        if size == 1:
            break
        mask = pow(2, i)
        count = sum(w & mask == mask for w in oxygen)
        if count >= size/2:
            oxygen = [w for w in oxygen if w & mask == mask]
        else:
            oxygen = [w for w in oxygen if not w & mask]
    
    c02 = input.copy()
    for i in range(mag -1, -1, -1):
        size = len(c02)
        if size == 1:
            break
        mask = pow(2, i)
        count = sum(w & mask == mask for w in c02)
        if count < size/2:
            c02 = [w for w in c02 if w & mask == mask]
        else:
            c02 = [w for w in c02 if not w & mask]

    return oxygen[0] * c02[0]


def main():
    print(a())
    print(b())


if __name__ == '__main__':
    main()
