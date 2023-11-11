import turtle
t = turtle.Turtle()
t.speed(9)
t.shape('turtle')
turtle.title('MyTurtle')
t.color('purple')

# t.circle(150)
# t.up()
# t.setposition(-50 , 200)
# t.dot(50)
# t.setposition(50 , 200)
# t.dot(50)
# t.setposition(-50 , 100)
# t.down()
# t.width(5)
# t.forward(100)
# t.up()
# t.setposition(0 , 0)
# t.color('blue')

t.forward(100)
t.left(90)
t.color('green')
t.forward(100)
t.left(90)
t.color('orange')



ranglar = ['black' , 'red' , 'green' , 'orange']

for i in range(4):
    t.forward(100)
    t.left(90)
    t.color(ranglar[i])
turtle.exitonclick()




print("Salom dunyo")
print("Salom PdP")



