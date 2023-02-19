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
            
            rear_opening_bracket = opening_brackets_stack[len(opening_brackets_stack) - i]
            
            if are_matching(rear_opening_bracket[0], next):
                opening_brackets_stack.remove(rear_opening_bracket)
            else:
                return i+1
            pass


        if len(opening_brackets_stack) == 0:
            return 'Success'
        else:
            return i



def main():
    text = input()

    if 'I' in text:
        text = input()

    mismatch = find_mismatch(text)

    print (mismatch)

if __name__ == "__main__":
    main()
