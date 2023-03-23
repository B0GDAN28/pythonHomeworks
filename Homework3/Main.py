# The solution of first exercise:
def get_sum(*args, **kwargs):
    total = 0
    result = [val for val in args if isinstance(val, (int, float))]

    result2 = sum(result)
    print(result2)
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
    for kwarg in kwargs.values():

        if isinstance(kwarg, (int, float)):
            total += kwarg

    return total


get_sum(1, 5, -3, 'abc', [12, 56, 'cad'])
get_sum()
print(get_sum(2, 4, 'abc', param_1=2, param_2=3))


# The solution of second exercise
def f(n):
    if n == 0:
        return [0]
    previous_step_list = f(n - 1)
    previous_step_list.append(n)
    return previous_step_list


f1 = f(10)
print('function1: ', f1)
suma = sum(f1)
print('suma este egala cu :', suma)
even_numbers = f1[::2]
print('numerele pare sunt: ', even_numbers)
sum_of_even_numbers = sum(even_numbers)
print(sum_of_even_numbers)
odd_numbers = f1[1::2]
print('numerele impare sunt: ', odd_numbers)
sum_of_odd_numbers = sum(odd_numbers)
print('Suma numerelor impare este: ', sum_of_odd_numbers)


# The solution of third exercise:
def get_number():
    number = input("Write a number: ")

    try:
        return int(number)
    except ValueError:
        return 0


print(get_number())
