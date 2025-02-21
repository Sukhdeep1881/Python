from pickletools import float8

from tensorflow.python.ops.numpy_ops.np_dtypes import float16


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # f9 = f8+f7 = 34
    # f8 = f7+f6 = 21
    # f7 = f6+f5 = 13
    # f6 = f5+f4 = 8
    # f5 = f4+f3 = 5
    # f4 = f3+f2 = 3
    # f3 = f2+f1 = 2
    # f2 = f1 + f0 = 1
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
