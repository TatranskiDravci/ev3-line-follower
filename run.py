#!/usr/bin/env pybricks-micropython
from libfollow import *

while(blue != True):
    scan()
    follow()
    reset()
