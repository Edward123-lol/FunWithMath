# We are going to be looking at approximations of Pi
# as well as looking at the math module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfsides = math.sin(math.radians(halfAngleA))
    sides = oneHalfsides * 2
    polygpmCircumfernce = numSides * sides
    pi = polygpmCircumfernce / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# See the loop above. In addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi.
# How many sides does it to make the two close.

print(math.pi)

# Accumulators

acc = 0
for val in range(1, 6):
    acc = acc + val

print(acc)


# Compute the sum of the first 100 even numbers
# Compute the sum of the first 50 odd numbers
# Compute the average of the first 100 odd numbers
# Write a function that returns the average of the first N numbers where N is a parameter
# Write a function called factorial that computes the product of the first N numbers, where N is a parameter
# Each number in the Fibonacci sequence is the sum of the previous two numbers
# The first two numbers in the sequence are 1 in 1. Compute the 18th fibonacci number
# Write a function to compute the Nth Fibonacci number where N is a parameter

# here is the sum of the first 100 even numbers

acc = 0
for val in range(0, 201, 2):
    acc = acc + val

print(acc)

# It is 10100


# average of the first 50 odd numbers

acc = 0
for val in range(1, 100, 2):
    acc = acc + val

print(acc)

# It is 2500

# average of the first 100 odd numbers

acc = 0
for val in range(1, 200, 2):
    acc = acc + val / 100

print(acc)

# it is 100
# A Monte Carlo Simulation

# random numbers

import random

print(random.random())

# Boolean Expressions
# <, <=, >, >=, ==, !=
# Compound Boolean expressions
# and, or, not

dogWeight = 25
print(dogWeight < 25)
catWeight = 12
print(dogWeight > 25 or catWeight <= 10)
print(not catWeight <= 10)

# Decision making skills

alice = 20
bob = 15
carol = 25
ans = 0
if alice > 20:
    if bob < 50:
        ans = 150
    else:
        ans = 300
else:
    if carol > 500:
        ans = 200
    else:
        ans = 75
print(ans)

value = 75
if value > 100:
    print("bigger than 100")
elif value > 80:
    print("bigger than 80")
elif value > 45:
    print("bigger than 45")
else:
    print("not bigger than much")

# function for the average of N numbers where N is a parameter

def average(N):
    acc = 0
    for average in range(0, 37, N):
        acc = acc + average
    print(acc/N)

# N = 6, average = 21

# this is a function fot the average of N numbers, N is the parameter

def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(10000))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        t.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi
import turtle
a = turtle.Turtle()
b = turtle.Turtle()
f = turtle.Turtle()

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        t.goto(x, y)
        f.goto(-x, -y)
        a.goto(x, -y)
        b.goto(-x, y)
        a.penup()
        f.penup()
        b.penup()

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")
        if distance <= 1:
            inCircle = inCircle + 1
            f.color("blue")
        else:
            f.color("red")
        if distance <= 1:
            inCircle = inCircle + 1
            a.color("blue")
        else:
            a.color("red")
        if distance <= 1:
            inCircle = inCircle + 1
            b.color("blue")
        else:
            b.color("red")

        t.dot()
        a.dot()
        b.dot()
        f.dot()
        a.penup()
        f.penup()
        b.penup()
    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi

print(showMontePi(100000))
turtle.exitonclick()
