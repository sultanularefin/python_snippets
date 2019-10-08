# 8. Compact
# This method removes falsy values (False, None, 0 and "") from a list by using filter().

def compact(lst):
    return list(filter(None, lst))


# compact([0, 1, False, 2, '', 3, 'a', 's', 34])



# [ 1, 2, 3, 'a', 's', 34 ]


print("compact operation: ", compact([0, 1, False, 2, '', 3, 'a', 's', 34]));



