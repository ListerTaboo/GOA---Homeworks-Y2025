#1. For საიტერაციო ცვლადი
#2. Num საიტერაციო ცვლადი
#3. In ოპერატორი
#4. მიმდევრობა
#5. ორწერტილი :
#6. კოდის ბლოკი
#7. 


# total = 0
# for num in range(15, 25, 3):
#         #print(num)
#         total += num
# print(total)

mircxus_pin_code = "4531"

code = input("Enter your pin code:")

while code != mircxus_pin_code:
    code = input("Enter your pin code:")

print("Access Granted !")