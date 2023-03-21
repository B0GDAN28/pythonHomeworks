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

def get_sum_from_all(*args, **kwargs):
    total = 0
