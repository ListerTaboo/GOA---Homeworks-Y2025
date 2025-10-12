from turtle import *

speed(500000)
bgcolor("green")

#ცა ცისფერი ( ჩემი ძმაკაცივით )
penup()
goto(-400, -100)
pendown()
color("deepskyblue")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

#მზე
penup()
goto(-320, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()

#ღრუბელი
penup()
color("white")
for pos in [(200,200),(220,240),(230,215),(180,225)]:
    goto(pos)
    pendown()
    begin_fill()
    circle(25)
    end_fill()
    penup()

#სასახლე ( მთავარი კედელი )
penup()
goto(-150, -100)
pendown()
color("gray20", "lightgray")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(180)
    left(90)
end_fill()

#ზედა ბლოკები
penup()
goto(-150, 80)
pendown()
color("black", "darkgray")
for i in range(6):
    begin_fill()
    for j in range(4):
        forward(30)
        left(90)
    end_fill()
    penup()
    forward(50)
    pendown()

#მარცხენა კოშკი
penup()
goto(-220, -100)
pendown()
color("gray20", "darkgray")
begin_fill()
for i in range(2):
    forward(70)
    left(90)
    forward(240)
    left(90)
end_fill()

#მარჯვენა კოშკი
penup()
goto(150, -100)
pendown()
begin_fill()
for i in range(2):
    forward(70)
    left(90)
    forward(240)
    left(90)
end_fill()

#პატარა კოშკების ზედა ბლოკები
for x in [-220, 150]:
    penup()
    goto(x, 140)
    pendown()
    for i in range(3):
        begin_fill()
        for j in range(4):
            forward(20)
            left(90)
        end_fill()
        penup()
        forward(25)
        pendown()

#კარები
penup()
goto(-40, -100)
pendown()
setheading(0)
color("black", "saddlebrown")
begin_fill()
forward(80)        #წინა მხარე
left(90)
forward(100)       #გვერდითა მხარე
circle(40, 180)    #მომრგვალო თავი ზემოდან
forward(100)       #მეორე მხარე
left(90)
end_fill()

#კარის სახელური
penup()
goto(25, -40)
pendown()
color("black")
begin_fill()
circle(4)
end_fill()

#აქ ვიწყებ დროშის აწყობას მარცხენა კოშკურაზე მე ილია ტაბატაძე ბარბარეს რაზმელი 😎
#ძელი
penup()
goto(185, 140)
pendown()
color("black")
width(4)
setheading(90)
forward(100)

#დროშის ფორმა
penup()
goto(185, 240)
pendown()
color("black", "limegreen")
begin_fill()
for i in range(2):
    forward(70)
    right(90)
    forward(105)
    right(90)
end_fill()

#GOA - ს ტექსტი დროშაზე
penup()
goto(220, 265)
pendown()
color("black")
write("GOA", font=("Arial", 12, "bold")) #აქ შეცვალე ფონტი, არ ვიცოდი როგორ იყო მარა მოვიძიე.

hideturtle()
exitonclick()
