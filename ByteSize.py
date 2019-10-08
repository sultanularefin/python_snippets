# 4. Byte size
# This method returns the length of a string in bytes.

def byte_size(string):
    return (len(string.encode('utf-8')))


print("byte_size('😀'): ",byte_size('😀'));  # 4
print("byte_size(\'Hello World\'): ",byte_size('Hello World')); # 11