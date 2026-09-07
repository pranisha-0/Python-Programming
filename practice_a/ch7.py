import math as m
print(m.pow(2,3))
print(m.ceil(2.3)) #> rounds to nearest integer greater than or equal to the number
print(m.floor(2.3)) #> rounds to nearest integer less than or equal to the number 

print(m.pi) #value of pi
print(m.e) #value of e

#trigo values radian ma return garxa
print(m.sin(45)) #value one didaina
#if degree ma chahiyo vane 
print(m.sin(m.pi/2)) #value one dinxa

#degree to radian or vice versa
print(m.degrees(m.pi/2)) #> 90.0
print(m.radians(90)) #> 1.5707963267948966

import random as r
lst = ["rock", "paper", "scissors"]
print(r.choice(lst)) 

print(r.randint(1, 277)) #> 1 to 6 bata random number dinxa 1 and 6 included

#statistics import garyo vane mean median haru calculate garna sakinxa
#datetime import garyo vane date and time ko calculation garna sakinxa

import datetime as dt
print(dt.datetime.now()) #> current date and time
