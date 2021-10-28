#! /usr/bin/env python

def check_palindrome(phrase):
    phrase = phrase.replace(' ', '').lower()
    revphrase = phrase[::-1]
    return revphrase == phrase


def show_palindrome_check(phrase):
    is_palindrome = check_palindrome(phrase)
    print(phrase+':', is_palindrome)


def erase_uppercase(string):
    letters = list(string)
    letters.sort()
    upper = [l for l in letters if l.isupper()]
    for u in upper:
        string = string.replace(u, '')

    return string[:]


if __name__ == '__main__':
    print('Are the next phrases palindromes?')
    show_palindrome_check('anita lava la tina')
    show_palindrome_check('el loro come coco como loco')
    show_palindrome_check('dabale arroz a la zorra el abad')
    show_palindrome_check('never odd or even')
    print()

    print('Erasing uppercase letters!')
    string = "This is the time.  We're going to do it. Let's finish this, Ok?"
    print(string)
    string = erase_uppercase(string)
    print(string)
