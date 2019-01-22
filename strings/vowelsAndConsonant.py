def vowConsCount(str):
    str = str.lower()
    vowel = consonant = 0
    for k in str:
        if k in ["a", "e", "i", "o", "u"]:
            vowel += 1
        else:
            consonant += 1
    return vowel, consonant


if __name__ == "__main__":
    print(vowConsCount('pritam'))
