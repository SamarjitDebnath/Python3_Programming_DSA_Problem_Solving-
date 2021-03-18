"""
Generator Function example
usage of "yield" instead of "return"

@samarjit_debnath
"""


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def GenPrime(max_num):
    for num1 in range(2, max_num):
        if isPrime(num1):
            yield num1

# Driver Code


if __name__ == '__main__':
    prime = GenPrime(50)
    print("Prime: ", next(prime))
    print("Prime: ", next(prime))
    print("Prime: ", next(prime))