#2) შექმენით პროგრამა რომელშიც გექნებათ თქვენი საყვარელი ბოსტნეულის ცვლადი, შემდეგ განაახლეთ ამ ცვლადის მნიშვნლობა ჯერ უბრალო გზით შემდეგ კი მინჭბის ოპერატორით (გამოიყენეთ ორივე ოპერაცია +, *), ასევე გააკეთეთ int ტიპის ცვლადი რომლის მნიშვნელობასაც განაახლებთ უბრალო ფორმით და შემდეგ assignment ოპერატორით. ასევე კომენტარებით დაწერეთ ცვლადის სახელის წესებით, თქვენ მიერ შექმნილი ცვლადები fstring-ის მეშვეობით დაბეჭდეთ, პირველი ცვლადის fstring ჯერ ახალ message ცვლადში შეინახეთ უნდა გამოიტანოთ my favourite vegetable is <vegetable>, შემდეგ კი მეორე ცვლადისთვის პირდაპირ დაბეჭდეთ fstring-ით fstring ახსენთ კომენტარებით

Fav_Vegetable = "Carrot"
Fav_Vegetable = " Tomato"
Fav_Fruit = " Watermelon"

Fav_Vegetable = Fav_Vegetable + " and Cucumber"
Fav_Vegetable *= 2
Fav_Vegetable += Fav_Fruit

message = f"My favourite vegetable is {Fav_Vegetable}"
print(message)

my_number = 5
my_number = my_number + 10

my_number *= 3

print(f"My updated number is {my_number}") # პირდაპირ f-string-ით დაბეჭდვა