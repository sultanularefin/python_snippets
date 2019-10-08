def palindrome(a):
    print("a[::-1]:",a[::-1]);
    return a == a[::-1]
    # OK, so
    # string[0::-1] is one
    # character, it
    # says
    # "count backwards from index 0 as far as you can".As
    # far as it
    # can is the
    # start
    # of
    # the
    # string.




print("palindrome('mom'): ",palindrome('mom')); # True