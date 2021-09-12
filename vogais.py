def is_lowercase_vowel(letter):
    if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
        return True
    return False


def is_uppercase_vowel(letter):
    if (letter == 'A') or (letter == 'E') or (letter == 'I') or (letter == 'O') or (letter == 'U'):
        return True
    return False


def vogal(letter):
    isVowel = False
    if is_lowercase_vowel(letter):
        isVowel = True
    if is_uppercase_vowel(letter):
        isVowel = True

    return isVowel


def test_is_lowercase_vowel():
    if(is_lowercase_vowel("a") == True):
        print('ok for is_lowercase_vowel("a")')
    else:
        print('not ok for is_lowercase_vowel("a")')
    if(is_lowercase_vowel("A") == False):
        print('ok for is_lowercase_vowel("A")')
    else:
        print('not ok for is_lowercase_vowel("A")')
    if(is_lowercase_vowel("b") == False):
        print('ok for is_lowercase_vowel("b")')
    else:
        print('not ok for is_lowercase_vowel("b")')


def test_is_uppercase_vowel():
    if(is_uppercase_vowel("A") == True):
        print('ok for is_uppercase_vowel("A")')
    else:
        print('not ok for is_uppercase_vowel("A")')
    if(is_uppercase_vowel("a") == False):
        print('ok for is_uppercase_vowel("a")')
    else:
        print('not ok for is_uppercase_vowel("a")')
    if(is_uppercase_vowel("b") == False):
        print('ok for is_uppercase_vowel("b")')
    else:
        print('not ok for is_uppercase_vowel("b")')


def test_vogal():
    if(vogal("A") == True):
        print('ok for test_vogal("A")')
    else:
        print('not ok for test_vogal("A")')
    if(vogal("a") == True):
        print('ok for test_vogal("a")')
    else:
        print('not ok for test_vogal("a")')
    if(vogal("b") == False):
        print('ok for test_vogal("b")')
    else:
        print('not ok for test_vogal("b")')


test_is_lowercase_vowel()
test_is_uppercase_vowel()
test_vogal()
