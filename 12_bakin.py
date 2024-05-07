import random

def fill_array(n, min_val, max_val):
    """
    Заполняет массив случайными значениями.

    Аргументы:
    n (int): Длина массива (количество элементов).
    min_val (int): Минимальное значение для случайных чисел.
    max_val (int): Максимальное значение для случайных чисел.

    Возвращает:
    list: Список случайных чисел.
    """
    random_array = [random.randint(min_val, max_val) for _ in range(n)]
    return random_array

def print_array(array):
    """
    Выводит массив на экран.

    Аргументы:
    array (list): Массив, который нужно вывести на экран.
    """
    print("Массив:", array)

# Пример использования функций:
if __name__ == "__main__":
    # Заполняем массив из 10 случайными числами от 1 до 100
    my_array = fill_array(10, 1, 100)
    
    # Выводим массив на экран
    print_array(my_array)
