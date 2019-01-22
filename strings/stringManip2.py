# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


def strMan2(str1, str2):
    new_str1 = str2[0:2] + str1[-1:]
    new_str2 = str1[0:2] + str2[-1:]
    return new_str1 + " " + new_str2


if __name__ == "__main__":
    print(strMan2('abc', 'xyz'))
