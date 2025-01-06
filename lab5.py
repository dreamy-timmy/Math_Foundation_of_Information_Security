import numpy as np
from lab2 import euclid_extended
from lab4 import binary_modular_power

def is_prime(number):
    number = abs(number)
    if number <= 1: 
        return False
    if number == 2 or number == 3:
        return True
    for x in range(2, int(np.sqrt(number))+1):
        if number % x == 0:
            return False
    return True

def private_key_search(e, p, q):
    phi = (p-1)*(q-1)
    gcd, d, _ = euclid_extended(phi, e)
    assert gcd == 1
    d %= phi
    
    return d

# 36 -> 18 -> 9 -> 3 -> 1
# 2 2 3 3

def generate_prime_products():
    primes = []
    for num in range(3, 1000):  
        if is_prime(num):
            primes.append(num)
    
    prime_products = []
    for i in range(0, len(primes), 3):
        if i + 2 < len(primes):
            prime_products.append(primes[i] * primes[i + 1] * primes[i + 2])
    return prime_products

# print(generate_prime_products())


# факторизация методом ПРОБНОГО ДЕЛЕНИЯ
def trial_division(n: int, two_degree=0, three_degree=0):
    factors = []
    prime_products = generate_prime_products()
    for _ in range(two_degree):
        factors.append(2)
        n //= 2
    for _ in range(three_degree):
        factors.append(3)
        n //= 3

    for product in prime_products:
        gcd, _, _ = euclid_extended(product, n)
        while (gcd != 1):
            factors.append(gcd)
            n //= gcd
            if is_prime(n):
                factors.append(n)
                return factors
            gcd, _, _ = euclid_extended(product, n)

    if n > 1:
        factors.append(n)
    return factors

def decrypt_message(C, d, n):
    return binary_modular_power(C, d, n)

# print(trial_division(36, two_degree=2, three_degree=2))

def trial_division_interface():
    split_list = input(f'Введите через пробел последовательно число для факторизации(n), кол-во степеней 2, кол-во степеней 3:\n')
    n, two_d, three_d = map(int, split_list.split())
    factors = trial_division(n, two_d, three_d)
    print(f'Найденные простые множители числа: {factors}')

# trial_division_interface()
def induvidual_var():
    e, n, C = 59, 29999, 21959

    p, q = trial_division(n)
    d = private_key_search(e, p, q)

    print(f'Расшифрованное сообщение: {decrypt_message(C, d, n)}')

def private_key_search_interface():
    input_split = input('Введите последовательно через пробел открытый ключ(е), два множителя n (p,q):\n')
    e, p, q = map(int, input_split)
    d = private_key_search(e, p, q)
    print(f'Найденный закрытый ключ: {d}')

def decrypt_message_interface():
    input_split = input('Введите последовательно через пробел блок зашифрованного сообщения(С), закрытый ключ(d) и модуль шифрования(n):\n')
    C, d, n = map(int, input_split)
    M = decrypt_message(C, d, n)
    print(f'Расшифрованное сообщение: {M}')

# обычный метод факторизации------------------
# def factorize_simple(n):         
#     factors = []
#     # iter = 0
#     for x in range(2, int(np.sqrt(n)+1)):
#         while n%x==0:
#             factors.append(x)
#             n //= x
#         if is_prime(n):
#             factors.append(n)
#             n //= n
#         if n == 1:
#             break
#         # 356 / 4 = 89
#         # iter += 1
#     return factors
# ---------------------------
