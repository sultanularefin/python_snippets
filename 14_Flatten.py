# 14. Flatten
# The following methods flatten a potentially deep list using recursion.

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


print("op result: of deep_flatten([1, [2], [[3], 4], 5]) ",deep_flatten([1, [2], [[3], 4], 5]));
# [1,2,3,4,5]

print("op result: of spread([1, [2], [[3], 4], 5]) ",spread([1, [2], [[3], 4], 5]));