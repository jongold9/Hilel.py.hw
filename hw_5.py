# 1.
# def isitPrime(k):
#     if k == 2 or k == 3:
#         return True
#     if k % 2 == 0 or k < 2:
#         return False
#     for i in range(3, int(k ** 0.5) + 1, 2):
#         if k % i == 0:
#             return False
#
#     return True
#
#
# print(isitPrime(int(input("is_prime:"))))
# 2.
# text = input("text: ")
# result = len(text.split())
# print("There are ", str(result), " words.")
# print("There are ", text.count('') - 1, " symbols.")
# text = input("text: ")
#
#
# def number():
#     result = len(text.split())
#     print("There are ", str(result), " words.")
#     print("There are ", text.count('') - 1, " symbols.")
#
#
# print(number())
# 3.
# figure = input("1-rectangle, 2-ellipse, 3-triangle : ")
#
# a = float(input("a: "))
# b = float(input("b: "))
#
#
# def mat():
#     if figure == "1":
#         print("S = : %.2f" % (a * b))
#     elif figure == "2":
#         from math import pi
#         print("S = ", (pi * a * b))
#     else:
#         print("S = ", (a * b / 2))
#
#
# print(mat())
# 4.
# списрк
# import random
# r = [random.randint(0, 1)
#      for x in range(20)]
# #фильтр
#     # if r % 2 != 0:
#     #     r = 0
# #посчитать 0
# print(r)
#
# print(r.count(0))
# import random
# #
# #
# def print_element_from_list(some_list: list):
#     for i, elem in enumerate(some_list):
#         if elem % 2 != 0:
#              i elem = 0
#             print(elem)
#         else:
#             print(elem)
#     print("all_0: ", some_list.count(0))
#
#
# numbers = [random.randint(0, 100) for x in range(20)]
#
# print_element_from_list(numbers)

# 5.
# a = float(input("a: "))
# def square():
#      p = 4 * a
#      s = a * a
#      d = 2 ** 0.5 * a
#      print((p, s, d))
#
# print(square())

# 6.
dict_fun = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(dict_fun)
dict_fun = {key: val for key, val in dict_fun.items() if val is not None}
print(dict_fun)