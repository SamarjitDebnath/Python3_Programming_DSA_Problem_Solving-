"""Stack Implementation
    And Problems on Stack

@samarjit_debnath
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        if self.is_empty():
            return
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peep(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


# 1. Reverse a string

def reverse_str(string):
    stack = Stack()
    n = len(string)
    for i in range(n):
        stack.push(str(string[i]))
    print(string)
    rev_str = ""

    for i in range(0, n, 1):
        if stack.is_empty():
            return
        rev_str += (stack.pop())

    return rev_str


# 2. Conversion of Integer to Binary

def int2bin(number):
    stack = Stack()

    while number > 0:
        stack.push(number % 2)
        number //= 2
    bin = ""
    while not stack.is_empty():
        bin += str(stack.pop())

    return bin


# 3. Balanced Parenthesis

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_balanced_paren(string):
    stack = Stack()
    is_balanced = True
    index = 0

    while index < len(string) and is_balanced:
        if not string[index].isalnum():
            paren = string[index]
            if paren in '([{':
                stack.push(paren)
            else:
                if stack.is_empty():
                    is_balanced = False
                else:
                    top = stack.pop()
                    if not is_match(top, paren):
                        is_balanced = False
        index += 1

    if stack.is_empty() and is_balanced:
        return True
    else:
        return False

# Driver code


if __name__ == '__main__':
    s = Stack()
    text = '(Hello)'
    print(is_balanced_paren(text))


