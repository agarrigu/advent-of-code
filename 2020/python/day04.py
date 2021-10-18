import AdventTools
import re


def convertInputToListOfDics(input):
    entries = [s.replace('\n', ' ') for s in input]
    '''
    omg, finding this bug took hours,
    went through the whole list until I found
    the trailing white space at the end of entries[].
    Learnt to debug with pdb though, that's nice.
    This little hack will do for now. I'll come back to it later.
    '''
    entries[len(entries) - 1] = entries[len(entries) - 1].rstrip()
    passports = [dict(e.split(":") for e in p.split(" ")) for p in entries]
    return passports


def isValidPassportPart1(passport, requiredFields):
    return all(field in passport for field in requiredFields)


# this. took. ages. jesus.
def isValidPassportPart2(passport):
    hgt = passport['hgt']
    colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    validByr = 1920 <= int(passport['byr']) <= 2002
    validIyr = 2010 <= int(passport['iyr']) <= 2020
    validEyr = 2020 <= int(passport['eyr']) <= 2030
    validHcl = re.search(r'^#[\da-f]{6}$', passport['hcl'])
    validEcl = passport['ecl'] in colours
    validPid = re.search(r'^\d{9}$', passport['pid'])
    # TODO refactor until validHgt, bit messy.
    validCmForm = re.search(r'^\d{3}cm$', hgt)
    if validCmForm and 150 <= int(validCmForm.group()[:3]) <= 193:
        validCm = True
    else:
        validCm = False
    validInForm = re.search(r'^\d{2}in$', hgt)
    if validInForm and 59 <= int(validInForm.group()[:2]) <= 76:
        validIn = True
    else:
        validIn = False
    validHgt = validCm or validIn
    if not validByr:
        return False
    if not validIyr:
        return False
    if not validEyr:
        return False
    if not validHgt:
        return False
    if not validHcl:
        return False
    if not validEcl:
        return False
    if not validPid:
        return False
    return True


def validatePassportsPart1(passports, requiredFields):
    return [p for p in passports
            if isValidPassportPart1(p, requiredFields)]


def validatePassportsPart2(passports):
    return [p for p in passports if isValidPassportPart2(p)]


input = AdventTools.ReadInput.inputToStrList('\n\n')
passports = convertInputToListOfDics(input)
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
nonRequiredFields = ['cid']
validPassports = validatePassportsPart1(passports, requiredFields)


def a():
    return len(validPassports)


def b():
    return len(validatePassportsPart2(validPassports))


def main():
    print('a', a())
    print('b', b())


if __name__ == '__main__':
    main()
