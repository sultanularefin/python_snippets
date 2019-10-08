# 16. Difference by
# The following method returns the difference between two
# lists after applying a given function to each element of both lists.

def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor

print("difference_by([2.1, 1.2], [2.3, 3.4], floor): ",difference_by([2.1, 1.2], [2.3, 3.4], floor));
# [1.2]

print("difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])",
      difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']));


# [ { x: 2 } ]
