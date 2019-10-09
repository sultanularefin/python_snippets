from collections import Counter;
import pdb;

def sum(x,y):
    ans = x+y
    return ans

def TwoSum(arr):
    # ret = [];
    ret = ""
    # for i in range(n):

    for i in range(1, len(arr), 1):
        # pdb.set_trace();
        for j in range(i+1, len(arr), 1):
            # print("i: ",i);
            # print("j: ",j);
            # print("(arr[i]: ", arr[i]);
            # print("arr[j]: ", arr[j]);
            result=sum(arr[i] , arr[j]);
            # print("sum(arr[i] , arr[j]): ", result)
            # pdb.set_trace();
            if (result == arr[0]):
                # pdb.set_trace();
                # print("FOUND");
                ret =ret +str(arr[i]);
                ret= ret + ',';
                ret =ret + str(arr[j]);
                ret =ret + ' ';
                # pdb.set_trace();





        # code goes here
    # print("ret: ",ret);
    # for i in range(0, len(ret), 2)

    if(len(ret)==0):
        return -1 ;
    else:
        return ret;

    # keep this function call here
    # print(TwoSum(input()))
print(TwoSum([17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]));