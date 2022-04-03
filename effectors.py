#!/usr/bin/python

#FILENAME: effectors.py
#PURPOSE:  All functions to move arms and claws


import os, sys
import ctypes
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
from motion import *
from effectors import *

def move_servo_to_position(port, end_pos,step):
	current_pos = KIPR.get_servo_position(port)
	if end_pos < current_pos:
		step = -step
	for pos in range(current_pos, end_pos, step):
		KIPR.set_servo_position(port, pos)
  		KIPR.msleep(10)
	KIPR.set_servo_position(port,end_pos)
       
            
#def armup(step):
	#move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_U, step)
        
#def armdown(step):
	#move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_D, step)
        
#def armback(step):
	#move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_B, step)
  
#def armstart(step):
	#move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_S, step)
        
def claw_open():
	#move_servo_slow(CLAW_PORT, KIPR.get_servo_position(CLAW_PORT), CLAW_O, step)
	KIPR.set_servo_position(3,CLAW_OPEN)
def claw_close():
	#move_servo_slow(CLAW_PORT, KIPR.get_servo_position(CLAW_PORT), CLAW_C, step)
	KIPR.set_servo_position(3,CLAW_CLOSED)
        
        

