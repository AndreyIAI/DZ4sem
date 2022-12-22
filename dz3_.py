import numpy
from random import randint as r

list_inp = [r(-10, 30) for i in range(20)]

res = numpy.array(list_inp)
unique_res = numpy.unique(res)
print("Сгененрированная последовательность чисел:\n", res)
print()
print("Cписок неповторяющихся элементов исходной последовательности:\n",
      unique_res)