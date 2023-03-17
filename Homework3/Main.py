# Exercise Nr. 1 - Sum of all numbers
# def get_sum_from_parameters(*args, **kwargs):
#     total = 0

# for arg in args:
#     # if type(arg) == int or type(arg) == float:
#     #     total += arg
#     # try:
#     #     total += float(arg)
#     # except ValueError:
#     #     pass
#     if isinstance(arg, (int, float)):
#         total += arg

# TODO #1: Account for `kwargs` and sum all the numbers in there
# TODO #2: Account for every number at any level in both `args` and `kwargs`
#
# return total
def get_sum_from_kwargs(*args, **kwargs):
    total = 0

    print(kwargs)
    for kwarg in kwargs.values():

        if isinstance(kwarg, (int, float)):
            total += kwarg
            print(kwarg)

    return total


print(get_sum_from_kwargs(2, 4, 'abc', param_1=2, param_2=3))

# print(get_sum_from_parameters(1, 5, -3, "abc", "12", [12, 56, "cad"]))
# print(get_sum_from_parameters(1, 5, -3, "abc", "12", [12, 56, [1, 2], "cad"]))
# print(get_sum_from_parameters(1, 5, -3, "abc", "12", [12, 56, [1, 2, {3, 4}], "cad"]))
# print(get_sum_from_parameters())
# print(get_sum_from_parameters(2, 4, "abc", param_1=2))
# print(get_sum_from_parameters(2, 4, "abc", param_1=2, param_2="abc"))
# print(get_sum_from_parameters(2, 4, "abc", param_1=2, param_2="abc", param_3=2.5))
# TODO #2: Account for every number at any level in both `args` and `kwargs`
def get_sum_from_all(*args, **kwargs):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
    for kwarg in kwargs.values():

        if isinstance(kwarg, (int, float)):
            total += kwarg
            print(kwarg)

    return total
print(get_sum_from_all(2, 4, 'abc', param_1=2, param_2=3))
# Exercise Nr. 2 - Recursive sum with "multiple return values"
# def get_rec_sum(n: int) -> tuple:
#     if n == 0:
#         return 0, 0, 0
#
#     total_sum, even_sum, odd_sum = get_rec_sum(n - 1)
#
#     total_sum += n
#     if n % 2 == 0:
#         even_sum += n
#     else:
#         odd_sum += n
#
#     return total_sum, even_sum, odd_sum
#
#
# total_sum, even_sum, odd_sum = get_rec_sum(5)
# print("total_sum", total_sum)
# print("even_sum", even_sum)
# print("odd_sum", odd_sum)
#
# Exercise Nr. 3 - Parse input function
# def get_integer_from_input():
#     user_input = input("Input: ")
#
#     try:
#         return int(user_input)
#     except ValueError:
#         return 0
#
#
# print(get_integer_from_input())

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
#
#
# def your_function(param_1, *args):
#     print(args)
#     result = [val for val in args if isinstance(val, (int, float))]
#     print(result)
#     result2 = sum(result)
#     print(result2)
#
#
# your_function(2, 4, 'abc', param_1=2)
#
#
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
#
#     def show_number():
#         print(verfication())
#
#
# insert_number()
#
#
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
