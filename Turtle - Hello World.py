# Turtle Project - 'Hello World'
# Tanner Bullock
# 30 June 2018
# Visit my GitHub for more - https://github.com/KiLL3Rw0lF
#

import turtle

#Say hello to Bob
bob = turtle.Turtle()

#This is the outline
bob.penup
bob.forward (400)
bob.left (90)
bob.pendown
bob.forward (400)
bob.left (90)
bob.forward (800)
bob.left (90)
bob.forward (400)
bob.left (90)
bob.forward (400)

bob.forward (400)
bob.left (90)
bob.forward (50)
bob.left (90)
bob.forward (800)

bob.left (135)
bob.forward (70)
bob.left (45)
bob.forward (700)
bob.left (45)
bob.forward (70)

bob.right (135)
bob.forward (50)
bob.right (90)
bob.forward (800)
bob.right (90)
bob.forward (50)
bob.right(90)
bob.forward (1)
bob.left (90)
bob.forward (325)

#This is the 'H' in 'HELLO'
bob.right (90) #From the wall
bob.up ()
bob.forward (20)
bob.down ()
bob.right (90) #Left leg
bob.forward (125)
bob.right (180)
bob.forward (62)
bob.right (90) #Bridge
bob.forward (75)
bob.left (90) #Right leg
bob.forward (63)
bob.right (180)
bob.forward (125)
bob.left (90)

#Space
bob.up ()
bob.forward (50)
bob.down ()

#This is the 'E' in 'HELLO'
bob.forward (100) #Bottom bridge
bob.right (180)
bob.forward (100)
bob.right (90)
bob.forward (62) #Lower back
bob.right (90)
bob.forward (75) #Middle bridge
bob.left (180)
bob.forward (75)
bob.right (90)
bob.forward (63) #Upper back
bob.right (90)
bob.forward (100) #Top bridge

#Space
bob.up ()
bob.forward (50)
bob.down ()

#This is the first 'L' in 'HELLO'
bob.left (270) #For fun we make bob spin around
bob.forward (125) #Back
bob.left (90)
bob.forward (80) #Bridge

#Space
bob.up ()
bob.forward (50)
bob.down ()

#This is the second 'L' in 'HELLO'
bob.left (90)
bob.forward (125)
bob.left (180) #For fun we make Bob spin around... again (Poor Bob:)
bob.forward (125) #Back
bob.left (90)
bob.forward (80) #Bridge

#Space
bob.up ()
bob.forward (100)
bob.down ()

#This is the 'O' in 'HELLO'
bob.right (180)
for i in range (100):
    bob.forward (4.1)
    bob.right (3.6)

bob.up ()
bob.right (180)
bob.forward (195)
bob.down ()
bob.right (90)
bob.forward (110)

#Now onto 'WORLD'...

#Space
bob.up ()
bob.right (90)
bob.forward (20)
bob.down ()

#This is the 'D' in 'WORLD'
bob.left (90)
bob.up ()
for a in range (25):
    bob.forward (4.1)
    bob.right (3.5)

bob.right (180)
bob.down ()
for b in range (50):
    bob.forward (4.1)
    bob.left (3.55)

bob.left (90)
bob.forward (132)

#Space
bob.up ()
bob.right (90)
bob.forward (50)
bob.down ()

#This is the 'L' in 'WORLD'
bob.forward (80) #Bridge
bob.right (90)
bob.forward (125) #Back
bob.right (180)
bob.forward (125)

#Space
bob.right (90)
bob.up ()
bob.forward (50)
bob.down ()

#This is the 'R' in 'WORLD
bob.right (50)
bob.forward (80) #Arm
bob.left (140)
bob.forward (65) #Leg
bob.right (180)
bob.forward (110)
bob.right (35)

for c in range (25):
    bob.forward (7)
    bob.right (12)
bob.left (155)
bob.forward (70)

#Space
bob.right (90)
bob.up ()
bob.forward (100)
bob.down ()

#This is the 'O' in 'WORLD
for d in range (100):
    bob.forward (4.1)
    bob.right (3.6)

#Space
bob.up ()
bob.forward (145)
bob.left (12) #To straighten the 'W'
bob.down ()

#This is the 'W' in 'WORLD'
bob.right (125)
bob.forward (130) #Right high arm
bob.right (180)
bob.forward (130) #Right high arm retrace
bob.right (135)
bob.forward (80) #Right low arm
bob.left (135)
bob.forward (80) #Left low arm
bob.right (125)
bob.forward (130) #Left high arm

#Let's let Bob run home now
bob.up ()
bob.left (30)
bob.forward (500)

print ("Press enter to continue...")
input ()
