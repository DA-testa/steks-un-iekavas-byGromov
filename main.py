# python3 
# Author: Aleksandrs Pučenkins 17.gr. 221RDB335

from collections import namedtuple


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":

            opening_brackets_stack.append(Bracket(next, i+1))
            pass

        if next in ")]}":
            
            if not len(opening_brackets_stack):
                return i+1
            
            
            pass


def main():
    text = input()

    if 'I' in text:
        text = input()

    mismatch = find_mismatch(text)

    print (mismatch)

if __name__ == "__main__":
    main()
