#2) შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)

# 5 წიგნის თავდაპირველი ფასები (ლარებში)
book_price_1 = 35.50
book_price_2 = 42.00
book_price_3 = 28.75
book_price_4 = 51.20
book_price_5 = 39.90

# ფასდაკლების ოდენობა (მაგალითად, 10%)
discount_percent = 10

# ფასდაკლების გამოთვლა ფორმულით:
# ახალი ფასი = ძველი ფასი - (ძველი ფასი * ფასდაკლება / 100)

discounted_book_1 = book_price_1 - (book_price_1 * discount_percent / 100)
discounted_book_2 = book_price_2 - (book_price_2 * discount_percent / 100)
discounted_book_3 = book_price_3 - (book_price_3 * discount_percent / 100)
discounted_book_4 = book_price_4 - (book_price_4 * discount_percent / 100)
discounted_book_5 = book_price_5 - (book_price_5 * discount_percent / 100)

# დაბეჭდვა ახალი ფასებით
print("ფასდაკლებული წიგნების ფასები:")
print("წიგნი 1:", discounted_book_1, "ლარი")
print("წიგნი 2:", discounted_book_2, "ლარი")
print("წიგნი 3:", discounted_book_3, "ლარი")
print("წიგნი 4:", discounted_book_4, "ლარი")
print("წიგნი 5:", discounted_book_5, "ლარი")
