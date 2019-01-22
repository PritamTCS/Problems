def Test(str):
    char = str[0]
    str1 = str.replace(char, '$')
    str1 = char + str1[1:]
    return str1


if __name__ == "__main__":
    print(Test('restart'))
