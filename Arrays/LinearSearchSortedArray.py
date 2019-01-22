def sortedListLinearSearch(val, lst):
    for k in lst:
        if k > val:
            return False
        if k == val:
            return True
    return False


if __name__ == "__main__":
    Lst = [50, 70, 30, 40, 90, 10]
    sortedLst = sorted(Lst)
    # print(sortedLst)
    print(sortedListLinearSearch(90, sortedLst))
