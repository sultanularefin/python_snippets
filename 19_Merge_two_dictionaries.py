# 19. Merge two dictionaries
# The following method can be used to merge two dictionaries.
import pdb;
def merge_two_dicts1(a, b):
    # pdb.set_trace();
    c = a.copy()   # make a copy of a
    pdb.set_trace();
    c.update(b)    # modify keys and values of a with the ones from b
    pdb.set_trace();
    return c


def merge_dictionaries2(a, b):

    return "**a, **b --Not working";
    # return {**a, **b};





a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}

print(merge_dictionaries2(a, b));

# {'y': 3, 'x': 1, 'z': 4}

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_two_dicts1(a, b)) # {'y': 3, 'x': 1, 'z': 4}