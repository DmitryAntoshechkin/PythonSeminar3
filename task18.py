# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X


from random import randint

try:
    size = int(input('Введите количество элементов массива: '))
    if size < 1:
        print('Введите число больше 1')
    else:
        a = [randint(1,100) for _ in range(size)]
        print(a)
        x = int(input('Введите искомое число: '))
        min_diff = 101
        index = 0
        for i in range(size):
            diff = a[i] - x
            if diff < 0:
                diff *= -1
            if diff < min_diff:
                index = i
                min_diff = diff
        print(f'Ближайший элемент массива : {a[index]}')
except:
     print('Введены некорректные данные')