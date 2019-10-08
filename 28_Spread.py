# 28. Spread
# This method flattens a list similarly like [].concat(...arr) in JavaScript.


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
            # def extend(self, *args, **kwargs): # real signature unknown
            # """ Extend list by appending elements from the iterable. """

        else:
            ret.append(i)
    return ret


print("spread([1,2,3,[4,5,6],[7],8,9]): ",spread([1,2,3,[4,5,6],[7],8,9]));
 # [1,2,3,4,5,6,7,8,9]