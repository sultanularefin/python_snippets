# 7. Chunk
# This method chunks a list into smaller lists of a specified size.

def chunk(list, size):

    for i in range(0,3,3):
        print(list[i]);
    for i in range(0,3,1):
        print(list[i]);
    for i in range(0, len(list), 3):
        # each element after 3 itearions
        print(list[i]);
    return [list[i:i+size] for i in range(0, len(list), 3)];
        # print(list[i]);




    # return [list[i:i+size] for i in range(0,len(list), size)]



# range([start,] stop [, step]) -> range object
# step is iteration.


print("chunk operation: ", chunk([12,33,41,31,445,44545,4512,4213,5124,6,63,99,90],3));