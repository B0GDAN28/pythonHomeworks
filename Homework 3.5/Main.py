# TODO #1: Account for `kwargs` and sum all the numbers in there
def get_sum_from_kwargs(*args, **kwargs):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg

    for kwarg in kwargs.values():

        if isinstance(kwarg, (int, float)):
            total += kwarg

    return total


print(get_sum_from_kwargs(2, 4, 'abc', param_1=2, param_2=3))


# TODO #2: Account for every number at any level in both `args` and `kwargs`

def sum_numbers(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        elif isinstance(arg, str) and arg.isdigit():
            total += int(arg)
        elif isinstance(arg, list):
            total += sum_numbers(*arg)
        elif isinstance(arg, tuple):
            total += sum_numbers(*arg)
        elif isinstance(arg, set):
            total += sum_numbers(*arg)
        elif isinstance(arg, dict):
            total += sum_numbers(*arg.values())
    return total


result = sum_numbers(1, 5, -3, "abc", "12", "3", "10", [12, 56, [1, 2, {3, 4, 10}], "cad"])
print(result)
