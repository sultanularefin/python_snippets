# 22. Time spent
# This snippet can be used to calculate the time it takes to execute a particular code.

import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c) #3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

# ('Time: ', 1.1205673217773438e-05)

# in my machine:
# 3
# ('Time: ', 1.5974044799804688e-05)
