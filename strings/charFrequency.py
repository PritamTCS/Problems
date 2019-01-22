# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

import string


def CharFreq(stri):
    d = {}
    for k in string.ascii_lowercase:
        for i in stri:
            if i == k:
                if d.get(i) is None:
                    d[i] = 1
                else:
                    d[i] = d[i] + 1
    return d


if __name__ == "__main__":
    print(CharFreq("google.com"))
