# > (მეტობა)
print(7 > 3)      # True  -> 7 უფრო დიდია ვიდრე 3
print(5 > 10)     # False -> 5 ნაკლებია 10-ზე
print(2.5 > 2)    # True  -> 2.5 უფრო დიდია 2-ზე
print(-1 > 0)     # False -> უარყოფითი რიცხვი ნაკლებია ნულზე
print(len("hello") > len("hi"))  # True -> "hello" 5 სიმბოლოა, "hi" კი 2

# >= (მეტია ან ტოლია)
print(5 >= 5)     # True  -> ტოლია
print(9 >= 10)    # False -> 9 ნაკლებია 10-ზე
print(8 >= 3)     # True  -> 8 უფრო დიდია 3-ზე
print(3.5 >= 3.5) # True  -> ტოლია
print(len("cat") >= len("cats")) # False -> 3 < 4

# < (ნაკლებობა)
print(4 < 7)      # True  -> 4 ნაკლებია 7-ზე
print(10 < 2)     # False -> 10 მეტიაო 2-ზე
print(-5 < 0)     # True  -> უარყოფითი ნაკლებია ნულზე
print(2.5 < 2.4)  # False -> 2.5 ცოტა მეტია 2.4-ზე
print(len("abc") < len("abcd")) # True -> 3 < 4

# <= (ნაკლებია ან ტოლია)
print(10 <= 10)   # True  -> ტოლია
print(9 <= 8)     # False -> 9 უფრო დიდია
print(3 <= 7)     # True  -> 3 ნაკლებია 7-ზე
print(4.1 <= 4.2) # True  -> 4.1 ნაკლებია
print(len("hi") <= len("hello")) # True -> 2 < 5

# == (ტოლობა)
print(5 == 5)     # True  -> ტოლია
print(5 == 6)     # False -> არ არის ტოლი
print("abc" == "abc") # True  -> სტრინგები ტოლია
print("A" == "a") # False -> ასოები განსხვავდება რეგისტრით
print(True == 1)  # True  -> Python-ში True უდრის 1-ს

# != (არათოლობა)
print(3 != 4)     # True  -> განსხვავდებიან
print(5 != 5)     # False -> ტოლია, ამიტომ False
print("hi" != "hello") # True  -> განსხვავებული სტრინგებია
print(10 != 10.0) # False -> Python-ში 10 == 10.0
print(False != 0) # False -> False == 0 Python-ში

temperature = 28
cloudy = True
humidity = 60
age = 18
score = 85

#3)
# 1
result1 = temperature > 30 and not cloudy   
# False -> 28 არ არის მეტი 30-ზე, ამიტომ მთელი გამოსახულება False

# 2
result2 = humidity >= 50 or temperature < 20  
# True -> 60 >= 50 აბრუნებს True, ამიტომ მთლიანად True

# 3
result3 = age >= 18 and score == 85  
# True -> ორივე პირობა მართალია: ასაკი 18-ზე მეტია და ქულა ზუსტად 85

# 4
result4 = not (temperature < 25 or cloudy)  
# False -> (temperature < 25 or cloudy) აბრუნებს True, not -> False

# 5
result5 = (score != 100 and humidity < 70) or (temperature <= 28)  
# True -> პირველი ნაწილი Trueა, რადგან score != 100 და humidity < 70, ამიტომ მთლიანად True


#4)

# 1) 1-იდან 10-მდე რიცხვები
for i in range(1, 11):
    print(i)
# გამოიტანს: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


# 2) ლუწი რიცხვები 2-დან 20-მდე
for i in range(2, 21, 2):
    print(i)
# გამოიტანს: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20


# 3) კენტი რიცხვები 1-იდან 19-მდე
for i in range(1, 20, 2):
    print(i)
# გამოიტანს: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19


# 4) უკუღმა დათვლა 10-იდან 1-მდე
for i in range(10, 0, -1):
    print(i)
# გამოიტანს: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1


# 5) ყოველი მე-3 რიცხვი 0-იდან 30-მდე
for i in range(0, 31, 3):
    print(i)
# გამოიტანს: 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30

