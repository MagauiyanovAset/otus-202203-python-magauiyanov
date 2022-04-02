# """
# Домашнее задание №1 Функции и структуры данных
# Функция, которая принимает N целых чисел,и возвращает список квадратов этих чисел
# >>> power_numbers(1, 2, 5, 7)
#  <<< [1, 4, 25, 49]


def power_numbers(*numbers, power=2):
    print("числа", numbers, "в степени", power)
    result = [number ** power for number in numbers]
    return result

print(power_numbers(2, 6, 3))


    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа    # (выбор производится передачей дополнительного аргумента)
    # >>> filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]

# функция для вычисления нечетных чисел:


def func_odd(o_numbers):
    return list(filter((lambda x: x % 2 != 0), o_numbers))

# функция для вычисления четных чисел:


def func_even(e_numbers):
    return list(filter((lambda x: x % 2 == 0), e_numbers))

# функция для вычисления простых чисел:


def func_pr(pr_numbers):
    result_pr = []
    for pr_number in pr_numbers:
        for num in range(2, pr_number):
            if pr_number % num == 0:
                break
        else:
            result_pr.append(pr_number)
    return result_pr


def filter_numbers(numbers, type_func):
    if type_func is ODD:
        return func_odd(numbers)
    elif type_func is EVEN:
        return func_even(numbers)
    else:
        return func_pr(numbers)


if __name__ == '__main__':
    ODD = func_odd
    EVEN = func_even
    PRIME = func_pr

    print("нечетные числа из списка")
    print(filter_numbers([2, 3, 8, 13, 12, 17, 21, 19], ODD))
    print("четные числа из списка")
    print(filter_numbers([2, 3, 8, 13, 12, 17, 21, 19], EVEN))
    print("простые числа из списка")
    print(filter_numbers([2, 3, 8, 13, 12, 17, 21, 19], PRIME))
