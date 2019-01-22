def removeDuplicates(lst):
    lst1 = []
    for k in lst:
        if k not in lst1:
            lst1.append(k)
    return lst1


if __name__ == "__main__":
    print(removeDuplicates([1, 2, 2, 3, 3, 4]))
