def duplicateChar(str):
    d = {}
    for k in str:
        d[k] = str.count(k)

    return d


def duplicateCharWithoutDict(str):
    for k in str:
        strCount = str.count(k)
        if strCount > 1:
            print(k, strCount)


if __name__ == "__main__":
    print(duplicateChar("google.com"))
    duplicateCharWithoutDict("google.com")
