#5) შექმენით 10 string ტიპის და 10 ინტეჯერ ტიპის ცვლადი, გააკეთეთ 5 კონკატინაციისა (სტრინგების შეერთების) და 5 მათემატიკური ჯამის მაგალითი

#სტრინგ ტიპის ცვლადები (10)
first_name = "Alex"
last_name = "Johnson"
city = "New York"
country = "USA"
book_title = "The Alchemist"
movie_title = "Inception"
favorite_color = "Blue"
hobby = "Playing guitar"
company = "TechCorp"
position = "Engineer"

#ინტეგერი ტიპის ცვლადები (10)
age = 25
current_year = 2025
quantity = 3
price = 20          #ერთი ნივთის ფასი
discount = 5
score = 80
level = 2
count = 7
pages = 320
temperature = 22


#5 მაგალითი — სტრინგების კონკატენაცია (+ ოპერატორი)
#1) სრული სახელი (სახელი + გვარი)
full_name = first_name + " " + last_name
print("1) Full name:", full_name)

#2) ლოკაციის სტრინგი (ქალაქი, ქვეყანა)
location_str = city + ", " + country
print("2) Location:", location_str)

#3) საყვარელი კომბინაცია (ჰობი + ფილმი)
fav_combo = hobby + " and " + movie_title
print("3) Favorite combo:", fav_combo)

#4) პროდუქციის აღწერა — ციფრის განსაცვიფრებლად კონვერტაცია str()-ით
product_description = str(quantity) + " x " + book_title
print("4) Product description:", product_description)

#5) პროფილის მოკლე ტექსტი (გამოყენებულია + ოპერატორი)
profile = first_name + " works as a " + position + " at " + company + "."
print("5) Profile:", profile)

#5 მათემატიკური (არის სხვადასხვა ნივთების ჯამი / გამოთვლები)
#1) ასაკის და დონეს ჯამი (მაგ., ასაკთან დამატებითი 'level' ინტერაქცია)
age_plus_level = age + level
print("Math 1) age + level =", age_plus_level)

#2) გვერდების ჯამი — დამატებით 100 გვერდს ვამატებთ
pages_plus_extra = pages + 100
print("Math 2) pages + 100 =", pages_plus_extra)

#3) ფასის და ფასდაკლების ჯამი (აქ უბრალოდ რაოდენობრივი დამატება)
price_plus_discount = price + discount
print("Math 3) price + discount =", price_plus_discount)

#4) ორი რაოდენობის (quantity და count) ჯამი
total_items = quantity + count
print("Math 4) quantity + count =", total_items)

#5) ქულა ზრდის შემდეგ (level*10 როგორც ბონუსი)
new_score = score + (level * 10)
print("Math 5) score + (level * 10) =", new_score)
