#1) while ციკლის გამოყენებით გამოიტანეთ რიცხვები, კომენტარებით დაწერეთ რა არის counter ცვლადი და შესაძლოა თუ არა რომ while ციკლი გაგრძელდეს უსასრულოდ, მოიყვანეთ მაგალითი

#counter — ეს არის მრიცხველი, რომელიც ითვლის რამდენჯერ ტარდება ციკლი
#თუ counter არ გაიზრდება ან არ შეიცვლება, while შეიძლება უსასრულოდ გაგრძელდეს

counter = 20  # საწყისი მნიშვნელობა

while counter <= 40:
    print(counter)
    counter += 1

counter = 50

while counter <= 100:
    if counter % 2 == 0:
        print(counter)
    counter += 1

counter = 20

while counter >= 0:
    print(counter)
    counter -= 1 

counter = 1

# while counter > 0:  #ეს პირობა ყოველთვის True იქნება
#     print("Endless")

