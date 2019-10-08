# 12. Get vowels
# This method gets vowels ('a', 'e', 'i', 'o', 'u') found in a string.

list =[];

def get_vowels(string):
    for each in string:
        if each in 'aeiou':
            # print(each);
            list.append(each);



    print("list: ",list);
    return [each for each in string if each in 'aeiou']


get_vowels('foobar') # ['o', 'o', 'a']
get_vowels('gym') # []