def is_prime(func):
    def wrapper(a,b,c):
        result = func(a, b, c)
        count = 0
        for i in range(2, result // 2):
            if result % i ==0:
                count += 1
        if count <= 0:
            return f'Простое число: {result}'
        else:
            return f'Составное число: {result}'
    return wrapper
@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result
result = sum_three(1, 2, 3)
print(result)
result = sum_three(1, 2, 2)
print(result)