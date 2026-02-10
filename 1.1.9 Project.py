#1.1.9 Project
import turtle as trtl

sky = trtl.Turtle()
sky.speed(100)

#create sky background
sky.pencolor("skyblue")
sky.fillcolor("skyblue")
sky.begin_fill()
sky.goto(-400, -100)
sky.goto(400, -100)
sky.goto(400, 400)
sky.goto(-400, 400)
sky.goto(-400, -100)
sky.end_fill()

#create sun
sky.penup()
sky.goto(200, 200)
sky.pencolor("lemonchiffon")
sky.fillcolor("lemonchiffon")
sky.pendown()
sky.begin_fill()
sky.circle(50)
sky.end_fill()
sky.hideturtle()


#create list of wave colors
wave = trtl.Turtle()
wave.speed(100)
wave_colors = ["teal", "lightseagreen", "mediumturquoise", "turquoise", "paleturquoise", "powderblue", "turquoise"]

#create the back of the wave
wave.pensize(5)
wave.penup()
wave.goto(-80,-150)
wave.pendown()
wave.color("turquoise")
wave.fillcolor("turquoise")
wave.begin_fill()
wave.forward(350)
wave.setheading(90)
wave.circle(250, 120)
wave.setheading(300)
wave.forward(350)
wave.end_fill()
#create wave
n=0
while n < 7:
    wave.pensize(30)
    wave.setheading(0)
    wave.penup()
    wave.goto(-200+n*30, -100)
    wave.pendown()
    wave.color(wave_colors[n])
    wave.circle(100,240)

    #add white cirlces to make it look like waves
    wave.color("white")
    wave.pensize(40)
    wave.circle(10, 360)
    
    n += 1
wave.penup()
#create water background
wave.pensize(1)
wave.pencolor("mediumturquoise")
wave.fillcolor("mediumturquoise")
wave.begin_fill()
wave.goto(-400, -100)
wave.pendown()
wave.goto(400, -100)
wave.goto(400, -350)
wave.goto(-400, -350)
wave.goto(-400, -100)
wave.end_fill()
wave.hideturtle()

#make variable for the water surface
water_surface = trtl.Turtle()

water_surface.penup()
water_surface.goto(-400, -100)
water_surface.pendown()
water_surface.fillcolor("mediumturquoise")  
water_surface.pencolor("mediumturquoise")
water_surface.pensize(2)
water_surface.setheading(0)
water_surface.forward(800)
water_surface.hideturtle()

#make surfer
surfer = trtl.Turtle()
surfer.speed(5)
surfer_image = "surfer.gif"
wn = trtl.Screen()
wn.addshape(surfer_image)
surfer.shape(surfer_image)


#make surfer postion and trail
surfer.penup()
surfer.pensize(2)
surfer.goto(45, 45)
surfer.pendown()
surfer.pencolor("lightcyan")
surfer.pensize(5)
surfer.setheading(130)

#make surfer move around the wave and hide when it reaches the surface of the water
turn=1

while turn < 20:
    for step in range (100):
     if surfer.ycor() > water_surface.ycor():
        if step < 50:
            surfer.circle(10, -180)
            surfer.setheading(130)
            surfer.circle(10,180)
            surfer.setheading(130)

    
     else:
        surfer.hideturtle()




wn = trtl.Screen()
wn.mainloop()