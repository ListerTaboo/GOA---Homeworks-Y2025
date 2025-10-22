#2)
#  > (მეტია)
print(5 > 3)     #True
print(2 > 7)     #False
print(10 > 10)   #False
print(-1 > -5)   #True
print(0 > -1)    #True

# >= (მეტია ან ტოლია)
print(5 >= 3)    #True
print(2 >= 7)    #False
print(10 >= 10)  #True
print(-1 >= -1)  #True
print(0 >= 1)    #False

# < (ნაკლებია)
print(3 < 5)     #True
print(7 < 2)     #False
print(10 < 10)   #False
print(-5 < -1)   #True
print(0 < 1)     #True

# <= (ნაკლებია ან ტოლია)
print(3 <= 5)    #True
print(7 <= 2)    #False
print(10 <= 10)  #True
print(-5 <= -5)  #True
print(1 <= 0)    #False

# == (ტოლია)
print(5 == 5)     #True
print(3 == 4)     #False
print("a" == "a") #True
print(10 == 10.0) #True
print(True == False) #False

# != (არ არის ტოლი)
print(5 != 3)    #True
print(7 != 7)    #False
print("hi" != "hello") #True
print(10 != 10.0)  #False
print(False != True) #True


#3)

a = 7 > 3      #True  → 7 მეტია 3-ზე
b = 10 <= 5    #False → 10 ნაკლები ან ტოლია 5-ის? არა
c = 4 == 4     #True  → 4 ტოლია 4-ის
d = 8 != 9     #True  → 8 არ არის ტოლი 9-ის
e = 2 >= 10    #False → 2 მეტია ან ტოლია 10-ის? არა

#ახსნა:
#"ოპერატორი" არის სიმბოლო, რომელიც კონკრეტულ მოქმედებას ასრულებს (მაგ: >, <, ==, !=)
#"ოპერაცია" არის ის მოქმედება, რაც ოპერატორის საშუალებით სრულდება (მაგ: 7 > 3 — ეს არის შედარების ოპერაცია)


#4)
#რიცხვითი შედარებები
print(5 > 3)          #True → 5 მეტია 3-ზე
print(2 < 1)          #False → 2 ნაკლები არ არის 1-ზე
print(10 >= 10)       #True → ტოლია
print(-5 <= -2)       #True → -5 ნაკლებია -2-ზე
print(8 != 8)         #False → 8 ტოლია 8-ის

#სტრინგების შედარებები
print("a" < "b")      #True → 'a' მოდის 'b'-მდე ანბანში
print("apple" > "ant")#True → "apple" lexicographically დიდია "ant"-ზე (მესამე ასოზე განსხვავდება)
print("dog" == "Dog") #False → დიდი და პატარა ასოები განსხვავებულია
print("cat" != "Cat") #True → ასოების რეგისტრი განსხვავდება
print("zebra" >= "zebra") #True → ზუსტად ტოლია

#ცვლადების შედარებები
x = 10
y = 15
z = 10
print(x < y)          #True → 10 ნაკლებია 15-ზე
print(x == z)         #True → ტოლია
print(y != z)         #True → 15 არ უდრის 10-ს
print(y > 100)        #False → 15 ნაკლებია 100-ზე
print(x >= 10)        #True → ტოლია

#სხვადასხვა ტიპების შედარება
print(5 == 5.0)       #True → Python-ში int და float თანასწორია როცა მნიშვნელობები ტოლია
print(5 is 5.0)       #False → განსხვავებული ტიპებია (int vs float)
print("5" == 5)       #False → str != int (ტიპები განსხვავებულია)
print(str(5) == "5")  #True → ორივე სტრინგია და მნიშვნელობები ტოლია
print(True == 1)      #True → True ინტერპრეტირდება როგორც 1
print(False == 0)     #True → False ინტერპრეტირდება როგორც 0
print(True > False)   #True → 1 > 0
print(False < True)   #True → 0 < 1
print("True" == True) #False → სტრინგი და ბულიანი მნიშვნელობა სხვადასხვა ტიპისაა
print(None == 0)      #False → None არ უდრის 0-ს

# --- შერეული ცვლადები ---
a = "10"
b = 10
print(int(a) == b)    #True → ორივე გარდაიქმნა ერთნაირად (10 == 10)
print(a == str(b))    #True → ორივე სტრინგია "10"
print(len("abc") > 2) #True → სტრინგის სიგრძე მეტია 2-ზე
print(len("hi") == 2) #True → სტრინგში 2 სიმბოლოა
