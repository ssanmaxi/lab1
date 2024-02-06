def isprime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i  == 0:
            return False
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prime_list = list(filter(lambda x: isprime(x), numbers))
print(prime_list)