from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

blue = False    # variable for blue dot
left = Motor(Port.A)
right = Motor(Port.D)
leftc = ColorSensor(Port.S1)
rightc = ColorSensor(Port.S4)
finderM = Motor(Port.B)


def follow():
    if(rightc.color() != Color.RED and leftc.color() != Color.RED):
        left.run_target(200, 20)
        right.run_target(200, 20)
    if(rightc.color() != Color.RED and leftc.color() == Color.RED):
        left.run_target(200, 15)
        right.run_target(200, 20)
    if(rightc.color() == Colo.RED and leftc.color() != Color.RED):
        left.run_target(200, 20)
        right.run_target(200, 15)
    left.reset_angle(0)
    right.reset_angle(0)

def scan():
    for i in range(46):
        finderM.run_target(200, i * 10)
        if(leftc.color() == Color.BLUE):
            blue = True
    i = 0
    for i in range(46):
        finderM.run_target(200 ,480 - (i * 10))
        if(leftc.color() == Color.BLUE):
            blue = True
    i = 0

def reset():
    left.reset_angle(0)
    right.reset_angle(0)
