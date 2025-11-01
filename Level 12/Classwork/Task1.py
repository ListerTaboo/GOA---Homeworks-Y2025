#1) and, or და not ლოგიკურ ოპერაციების ყველა შემავალი True/False მნიშვნლობებების კომბინაცები აიღეთ და დაბეჭდეთ


#And
# not_going = False
# not_drinking_water = False
# print(not_going and not_drinking_water)

#And
not_dancing = False
not_drinking_water = False
not_staying = True
its_9pm = True
print(not_dancing and not_drinking_water) #False
print(not_drinking_water and not_staying) #False
print(not_staying and its_9pm) #True

#Or
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

#Not
print(not True) #False
print(not False) #True