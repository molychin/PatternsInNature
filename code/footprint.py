"""
Created on Wed Jun  5 13:59:28 2019
code/footprint.py
@author: molychin
"""

print("Working...")
import turtle
t = turtle.Pen()
turtle.Turtle().screen.delay(0)   #绘画没有延迟
t.width(2)
for x in range(100):
    t.forward(x*2)
    t.left(89)  