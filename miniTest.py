numbers = list(range(1, 101))
result = []

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for n in reversed(numbers):
    if is_prime(n):
        continue
    elif n % 15 == 0:
        result.append("FooBar")
    elif n % 3 == 0:
        result.append("Foo")
    elif n % 5 == 0:
        result.append("Bar")
    else:
        result.append(str(n))

print(" ".join(result))