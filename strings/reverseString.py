def stringReverse(str):
    return str[::-1]


def strReverse(str):
    str1 = ""
    for k in range(len(str)):
        str1 = str1 + str[len(str) - 1 - k]
    return str1


if __name__ == "__main__":
    print(stringReverse('pritam'))
    print(strReverse('pritam'))
