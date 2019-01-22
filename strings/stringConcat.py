# Sample String : 'w3resource'
# Expected Result : 'w3ce'


def FirstAndLastTwo(str):
    return str[:2] + str[-2:]


if __name__ == "__main__":
    print(FirstAndLastTwo("w3resource"))
    print(FirstAndLastTwo("w3"))
