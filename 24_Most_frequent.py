# 24. Most frequent
# This method returns the most frequent element that appears in a list.

def most_frequent(list):
    # key = list.count;
    # print("key: ",key);
    # print("list.count: ",list.count);
    print("list.count(list): ",list.count(list));
    print("list.count(2): ", list.count(2));
    print("set(list): ",set(list));
    print("max(set(list): ",max(set(list)));


    return max(set(list), key=list.count);


numbers = [1, 2, 1, 2, 3, 2, 1, 4, 2]
print("most_frequent(numbers):",most_frequent(numbers));