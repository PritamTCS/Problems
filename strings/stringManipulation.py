# Sample String : 'restart'
# Expected Result : 'resta$t'


def stringManipulation(str):
    listStringExtract = list(str[1:])
    first_char = str[0]
    for k in listStringExtract:
        if k == first_char:
            indexOf = listStringExtract.index(k)
            listStringExtract[indexOf] = '$'
    listStringExtract.insert(0, first_char)
    return "".join(listStringExtract)


def withReplace(str):
    char = str[0]
    str1 = str.replace(char, '$')
    str1 = char + str1[1:]
    return str1


if __name__ == "__main__":
    print(stringManipulation('restart'))
    print(withReplace('restart'))
