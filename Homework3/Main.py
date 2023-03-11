# def your_function(*args):
#     print(args)
#     result = [val for val in args if isinstance(val, (int, float))]
#     print(result)
#     result2 = sum(result)
#     print(result2)
#
#
# your_function(1, 5, -3, 'abc', [12, 56, 'cad'])
# your_function()

# def your_function(*args, param_1):
#     print(args)
#     result = [val for val in args if isinstance(val, (int, float))]
#     print(result)
#     result2 = sum(result)
#     print(result2)
#
#
# your_function(2, 4, 'abc', param_1=2)

# def insert_number():
#     number = input('type number: ')
#     return int(number)
#
#
# def verfication():
#     while True:
#         try:
#             number = insert_number()
#             return number
#
#         except ValueError:
#             print('Value is not a number')
#     print(verfication())
#     def show_number():
#         print(verfication())
#
# insert_number()
# def f(n):
#     if n == 0:
#         return [0]
#
#     previous_step_list = f(n - 1)
#     previous_step_list.append(n)
#
#     return previous_step_list
#
#
# f1 = f(10)
# print('function1: ', f1)
# suma = sum(f1)
# print('suma este egala cu :', suma)
# even_numbers = f1[::2]
# print('numerele pare sunt: ', even_numbers)
# sum_of_even_numbers = sum(even_numbers)
# print(sum_of_even_numbers)
# odd_numbers = f1[1::2]
# print('numerele impare sunt: ', odd_numbers)
# sum_of_odd_numbers = sum(odd_numbers)
# print('Suma numerelor impare este: ', sum_of_odd_numbers)
