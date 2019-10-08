# 15. Difference
# This method finds the difference between two
# iterables by keeping only the values that are in the first one.
import pdb;

def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    pdb.set_trace();
    comparison1 = set_a.difference(set_b);
    pdb.set_trace();

    comparison2 = set_b.difference(set_a);
    pdb.set_trace();
    return list(comparison1);


print("difference([1,2,3], [1,2,4]) : ",difference([1,2,3], [1,2,4]) );

# [3]