# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    # closing_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass
                
        if next in ")]}":
            # Process closing bracket, write your code here
            # closing_brackets_stack.append(Bracket(next, i + 1)
            if len(opening_brackets_stack) == 0:
                return i + 1
            elif not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1

            opening_brackets_stack.pop()
            pass

    if opening_brackets_stack:
        return i - 1
    return "Success"


def main():
    fi = input("I or F: ")
    if "I" in fi or "i" in fi:
        text = input("Brackets: ")
        mismatch = find_mismatch(text)
    elif "F" in fi or "f" in fi:
        test_num = input("Choose test number (0-5): ")
        with open(f"test/{test_num}", "r") as file:
            text = file.read()
            mismatch = find_mismatch(text)

    # Printing answer, write your code here
    if mismatch == None:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
