#1) მომხმარბელს შემოატანინეთ თავისი სიმაღლე (height) და წლების რაოდენობა (years), შემდეგ კი გამოუთვალეთ სავაურადო სიმაღლე EH (Estimated Height), ჩათვალეთ რომ ადამიანი ყოველ წელს იზრდება 0.5 სანტიმეტრით

height = float(input("შეიყვანეთ თქვენი ამჟამინდელი სიმაღლე: "))
years = int(input("წლების რაოდენობა: "))

EH = height + (years * 0.5)

print(EH)


#2) კომენტარებით ახსენით რა არის boolean მონაცემთა ტიპი და თითოეულ შედარების ოპერატორზე მოყვანილი მაგალითის შედეგი დაბეჭდეთ: >, <, ==, >=, <=

#Boolean მონაცემთა ტიპი შეიცავს ორ მნიშვნელობას: True (სიმართლე) ან False (ცრუ) იგი გამოიყენება გამოთვლებში და შედარებებში

a = 10
b = 5

print("a > b =", a > b)   #True
print("a < b =", a < b)   #False
print("a == b =", a == b) #False
print("a >= b =", a >= b) #True
print("a <= b =", a <= b) #False

# print(type("23")) 
# print(type(5))
# print(type(2.4))

# ნებისმიერი ინფორმაცია/სიმბოლები რაც წერია ბრჭყალებში ''/"" არის string
# ბრჭყალების გარეშე დაწერილი რიცხვითი მნიშვნელობა არის ან int (მთელი) ან float (ათწლიადი)

# digit = int(input("Enter a digit: "))

# implicit data conversion - ბუნბერივი (თავისთავად) მონაცემთა ტიპის შეცვალა
# print(10 / 2)

# explicit data conversion - ხელონვური (ჩვენით) მონაცემთა ტიპის შეცვალა
# int('2')
# float('2.3')
# str(5)

# age = int(input())
# print(type(age))

# print(5 + 1.2)

# Comparsion Operations

# boolean - მონაცემთა ტიპი 2 შესაძლო მნიშნვლობით: True (ჭეშმარიტი, მართალი) ან False (მცდარი, ტყუილი)

# print(type(True))
# print(type(False))

# შედარების ოპერაციის შედეგი არის ყოველთვის Boolean მონაცეთა ტიპის მნიშვნელობა
# print(5 > 2) # True
# print(4 < 3) # False
# print(9 == 8) # False
# print(4 >= 4) # True
# print(12 <= 11) # False