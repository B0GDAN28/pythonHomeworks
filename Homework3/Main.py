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

def your_function(*args, param_1=2):
    print(args)
    result = [val for val in args if isinstance(val, (int, float))]
    print(result)
    result2 = sum(result)
    print(result2)


your_function(2, 4, 'abc', param_1= 2)

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
