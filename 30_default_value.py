# 30. Get default value for missing keys
# This snippet shows how you can get a default value
# in case a key you are looking for is not included in the dictionary.


d = {'a': 1, 'b': 2}

print(d.get('c', 3, )) # 3
print(d.get('d',8));