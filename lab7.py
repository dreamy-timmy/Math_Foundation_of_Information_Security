from lab4 import binary_modular_power
from lab6 import integer_sqrt

# a^x ≡ b (mod p)
def babyStep_giantStep(a, b, p):
    '''
    Шаг младенца, шаг великана - алгоритм нахождения дискретного логарифма по модулю p.\n
    Нахождение x в выражении: `log_a(b) = x (mod p)`
    '''
    k = integer_sqrt(p)+1
    i = 1
    y = binary_modular_power(a, i*k, p)
    z = b*binary_modular_power(a, i, p) % p
    z_list = [z]
    y_list = [y]
    while not [v for v in z_list if v in y_list] :
        i += 1
        y = a**(i*k) % p
        z = b*a**i % p
        y_list.append(y)
        z_list.append(z)
    z_index = [i+1 for i in range(len(z_list)) if z_list[i] in y_list][0]
    y_index = [i+1 for i in range(len(y_list)) if y_list[i] in z_list][0]
    # print(z_list)
    # print(sorted(y_list))
    # print(f'y_index: {y_index}, k: {k}, z_ind: {z_index}, length: {len(z_list)}')
    x = y_index*k - z_index

    return x

# print(babyStep_giantStep(2, 18441, 30203))

def babyStep_giantStep_interface():
    list_input = input('Введите последовательно через пробел соответствующие a, b и p (a^x ≡ b (mod p)):\n')
    a, b, p = map(int, list_input.split())
    x = babyStep_giantStep(a, b, p)
    print(f'Полученная степень x: {x}, проверка: b = {binary_modular_power(a, x, p)}')
# babyStep_giantStep_interface()


