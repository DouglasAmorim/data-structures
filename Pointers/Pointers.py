num1 = 11 
num2 = num1

print('Before num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)

# id(variable) shows the position in memory wich the variable points
print('\nnum1 points to: ', id(num1))
print('num2 points to: ', id(num2))

# When we change the value of num2, the position in memory changes
# This is why Integers are unmutable, so if we put some Int in memory we cannot change
num2 = 22
print('\nAfter num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)

# id(variable) shows the position in memory wich the variable points
print('\nnum1 points to: ', id(num1))
print('num2 points to: ', id(num2))


# Lets try check Dictionaries

dict1 = { 
    'value': 11
}

dict2 = dict1

print('Before dict2 value is updated:')
print('dict1 =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to: ', id(dict1))
print('dict2 points to: ', id(dict2))

# Dictionarios are not Immutable, so when we change de 'value', inst created another value in memory
dict2['value'] = 12

print('\nAfter dict2 value is updated:')
print('dict1 =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to: ', id(dict1))
print('dict2 points to: ', id(dict2))