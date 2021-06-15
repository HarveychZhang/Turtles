import turtle as t
t.bgcolor("light blue")
t.pensize(3)
t.speed(100)

def snowman():

    def hat():
        t.penup()
        t.left(90)
        t.forward(200)
        t.right(90)
        t.pendown()
        t.begin_fill()
        t.forward(110)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(70)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.fillcolor("black")
        t.end_fill()
        
    

    def face():
        t.penup()
        t.forward(12.05)
        t.right(90)
        t.forward(35)
        t.pendown()
        t.circle(45)
        
        
    def eye1():
        t.left(180)
        t.penup()
        t.forward(5)
        t.right(90)
        t.forward(30)
        t.pendown()
        t.begin_fill()
        t.circle(5)
        t.fillcolor("white")
        t.end_fill()
        
        
    def eye2():
        t.penup()
        t.forward(25)
        t.pendown()
        t.begin_fill()
        t.fillcolor("white")
        t.circle(5)
        t.end_fill()
        
        
    def mouse():
        t.penup()
        t.right(90)
        t.forward(20)
        t.right(90)
        t.pendown()
        t.forward(25)
        
    
    def body():
        t.penup()
        t.forward(73)
        t.left(180)
        t.forward(18)
        t.right(90)
        t.forward(100)
        t.pendown()
        t.circle(70)
        
    
    def hand1():
        t.right(110)
        t.forward(50)
        t.right(50)
        t.forward(40)
        t.right(10)
        t.forward(17)
        t.penup()
        t.backward(17)
        t.left(65)
        t.pendown()
        t.forward(17)
        t.backward(17)
        
    def hand2():
        t.left(105)
        t.penup()
        t.forward(55)
        t.left(90)
        t.forward(200)
        t.left(30)
        t.pendown()
        t.forward(60)
        t.left(50)
        t.forward(16)
        t.backward(16)
        t.right(90)
        t.forward(16)
        t.right(180)
        t.forward(16)
        t.right(320)
        t.forward(60)
        t.left(60)
        t.penup()
        t.forward(270)
        t.right(90)
        t.forward(70)
        t.right(180)
        t.pendown()
        
        
    def legs():
        t.circle(100)
        
        
        
        

    hat()
    face()
    eye1()
    eye2()
    mouse()
    body()
    hand1()
    hand2()
    legs()
    t.done()

snowman()