# 18. Has duplicates
# The following method checks whether a list has
# duplicate values by using the fact that set() contains only unique elements.


def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x)  # True
has_duplicates(y)  # False