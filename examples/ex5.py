#!/usr/bin/python

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
eyes = 'blue'
teeth = 'White'
hair = 'Brown'
weight = 180

height_cm = height * 2.54
weight_kg = weight / 2.2

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d cm tall." % height_cm
print "He's %d pounds heavy." % weight
print "He's %d kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is tricky, try to get it exactly right.
print "If I add %d, %d and %d I get %d." % (
    age, height, weight, age + height + weight)
