import serial
import turtle
import random
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Chaedu")
screen.tracer(0)

# Create a pen for displaying score, game over, etc.
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-280, 270)
pen.write("Score: 0", align="left", font=("Courier", 14, "normal"))

# Player setup
class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("triangle")
        self.color("blue")
        self.goto(0, -270)
        self.setheading(90)

    def move_left(self):
        x = self.xcor()
        if x > -270:
            self.setx(x - 10)

    def move_right(self):
        x = self.xcor()
        if x < 270:
            self.setx(x + 10)

    def move_up(self):
        y = self.ycor()
        if y < 270:
            self.sety(y + 10)

    def move_down(self):
        y = self.ycor()
        if y > -270:
            self.sety(y - 10)

    def shoot(self):
        bullet.fire(self.xcor(), self.ycor() + 10)

player = Player()

# Bullet setup
class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape('triangle')
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.hideturtle()
        self.setheading(90)

    def fire(self, x, y):
        self.goto(x, y)
        self.showturtle()

bullet = Bullet()

# Enemies setup
class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()    # ... (collision detection, enemy movement, game    # ... (collision detection, enemy movement, game-over logic, and win condition)

# Close the game and serial connection-over logic, and win condition)

# Close the game and serial connection
        self.shape('circle')
        self.color("red")
        self.goto(random.randint(-270, 270), random.randint(200, 265))
        self.setheading(0)

enemies = [Enemy() for _ in range(10)]

# Serial communication setup
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()

# Game settings
bullet_state = "ready"
score = 0
enemy_speed = 10
num_enemies = 10
TheGameIsRunning = True

# Game loop
while TheGameIsRunning:
    # Read data from Arduino
    ser_bytes = ser.readline()
    decoded_bytes = ser_bytes.decode("utf-8").strip()

    print("Received:", decoded_bytes)  # Debug print statement

    if decoded_bytes == "left":
        print("Moving left")  # Debug print statement
        player.move_left()
    elif decoded_bytes == "right":
        print("Moving right")  # Debug print statement
        player.move_right()
    elif decoded_bytes == "up":
        print("Moving up")  # Debug print statement
        player.move_up()
    elif decoded_bytes == "down":
        print("Moving down")  # Debug print statement
        player.move_down()
    elif decoded_bytes == "shoot":
        print("Shooting")  # Debug print statement
        player.shoot()

    # Update the screen
    screen.update()

screen.bye()
ser.close()
