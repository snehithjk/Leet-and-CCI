#check if string has unique chars in it

def hasUnique(str):
    m = set()
    for i in str:
        if i in m:
            return False
        m.add(i)

    return True

assert hasUnique("abcd") == True
assert hasUnique("abcda") == False
