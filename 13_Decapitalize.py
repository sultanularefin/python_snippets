# 13. Decapitalize
# This method can be used to turn the first letter of the given string into lowercase.

def decapitalize(str):
    return str[:1].lower() + str[1:]


print(decapitalize('FooBar'));  # 'fooBar'
print(decapitalize('FooBar'));  # 'fooBar'