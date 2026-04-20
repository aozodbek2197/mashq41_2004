# 1-mashq
import sys
sys.setrecursionlimit(2000)

def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

print(fact(100))
# 2-mashq
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

pg = prime_generator()
for _ in range(10):
    print(next(pg), end=' ') 
# 3-mashq
def average(*numbers):
    if not numbers: return 0
    return sum(numbers) / len(numbers)

print(average(10, 20, 30, 40))  
