def binarySearch(val, lst):
    first = 0
    last = len(lst) - 1
    while first <= last:
        mid = (first + last) // 2
        if val < lst[mid]:
            last = mid - 1
        elif val > lst[mid]:
            first = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    lst = [10, 20, 30, 40, 50, 60]
    lst.sort(reverse=False)
    print(binarySearch(4, lst))
