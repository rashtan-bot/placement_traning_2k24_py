def palindrome(x):
    temp = x
    rev = 0
    while  temp != 0:
        rev = (rev * 10) + temp % 10
        temp = temp // 10
    if x == rev: 
        print('palindrome')
    else: 
        print('not palindrome')

def isPrime(n):
    for i in range(2, n//2):
        if n % i == 0: return False
    return True

def primes(n):
    if n < 2: return
    for i in range(2, n):
        if isPrime(i): print(i)


