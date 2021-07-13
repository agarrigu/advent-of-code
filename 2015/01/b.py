with open('input.txt') as input:
    input = input.read()

answer = 0
for i, element in enumerate(input):
    if (element == '('):
        answer += 1
    elif (element == ')'):
        answer -= 1
    if (answer == -1):
        print(i + 1)
        break
