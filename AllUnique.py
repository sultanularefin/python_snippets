# 1. All unique

# The following method checks whether the given list has duplicate elements.
# It uses the property of set() which removes duplicate elements from the list.


def all_unique(lst):
    print("len(set(lst)):",len(set(lst)));
    return len(lst) == len(set(lst))



arr = []

print("enter n");
num = int(input())



print("num: ", num);

num_array = list()

print ('Enter numbers in array: ');
for i in range(int(num)):
    one = input("one_num :")
    num_array.append(int(one))
print ('ARRAY: ',num_array);



x = [1,1,2,2,3,2,3,4,5,6]
# print("arr: ",arr);

y = [1,2,3,4,5]
result1 = all_unique(x) # False

print("Result1: ",result1);

result2 = all_unique(y) # True

print("Result2: ",result2);