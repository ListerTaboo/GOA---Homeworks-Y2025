#Logical Operators: And, Or, Not

#And
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

#Or
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

#Not
print(not True) #False
print(not False) #True


#Examples:
#Not
print(not True) #False
print(not False) #True

#Or
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

#And
not_raining = False
not_sunny = False

print(not_raining and not_sunny)


#Ranges
numbers = range(2, 5)
print(numbers)

# 0, 1, 2, 3, 4.
for num in range(5):
    print(num)
    
name = "ilia"
for char in "ilia":
    print(char)