def anagramCheck(str1, str2):
    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    print(anagramCheck('listen', 'silent'))
