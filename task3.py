# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
#  Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

from random import randint

try:
    size = int(input('Введите количество элементов массива: '))
    if size < 1:
        print('Введите число больше 1')
    else:
        a = [randint(1,20) for _ in range(size)]
        print(a)
        seq_len_max = 1
        result = [0]*2
        for i in range(size):
            seq_len = 1
            while a[i]+seq_len in a:
                seq_len+=1
            if seq_len > seq_len_max:
                result[0] = a[i]
                result[1] = a[i]+seq_len-1
                seq_len_max = seq_len
            #print(i,seq_len,result,)
        print (result)

except:
     print('Введены некорректные данные')