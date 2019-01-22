def linearSearch(val, lst):
    for i in lst:
        if i == val:
            return True
    else:
        return False


if __name__ == "__main__":
    print(linearSearch(2, [10, 20, 40, 32]))
