#!/usr/bin/python

#FILENAME: movement.py
#PURPOSE:  holds all of our movement functions

import os, sys
import ctypes
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
from motion import *
from effectors import *
from constants import *

#Function: backward
#Description: move backward at a certain speed a certain distance
#Arguments:
	#speed = speed the robot moves
	#mm = distance in mm to move

def backward(speed, mm):
   	
	KIPR.set_create_distance(0);
	KIPR.create_drive_straight(speed);
	while(KIPR.get_create_distance() < mm):
		pass
  	KIPR.create_drive_straight(0)

#Function: forward
#Description: move forward at a certain speed a certain distance
#Arguments:
	#speed = speed the robot moves
	#mm = distance in mm to move

def forward(speed, mm):
    
	KIPR.set_create_distance(0)
	KIPR.create_drive_direct(-speed, -speed)
	while(KIPR.get_create_distance() > -mm):
		pass
 	KIPR.create_drive_straight(0)

def CW(speed, angle):
    
	KIPR.set_create_total_angle(0)
	KIPR.create_spin_CW(speed)
	while(KIPR.get_create_total_angle() >= -angle):
		pass
 	KIPR.create_spin_CW(0)
        
def CCW(speed, angle):
    
	KIPR.set_create_total_angle(0)
	KIPR.create_spin_CCW(speed)
	while(KIPR.get_create_total_angle() < angle):
		pass
	KIPR.create_spin_CCW(0)
	
def backward_to_black(speed):
	print "invoking the backward to black command"
	KIPR.create_drive_straight(speed)
	while(KIPR.analog(LINE_PORT) <= THRESH):
		pass
 	KIPR.create_drive_straight(0)
        
def turn_CW_to_black(speed=100, port=LINE_PORT, thresh=THRESH):
	KIPR.create_spin_CW(speed)
	while(analog_avg(port, 10) <= thresh):
		pass
 	KIPR.create_spin_CW(0)

def turn_CCW_to_black(speed=100, port=LINE_PORT, thresh=THRESH):
	KIPR.create_spin_CCW(speed)
	while(KIPR.analog(port) <= thresh):
		pass
 	KIPR.create_spin_CCW(0)
            
def drive_to_bump(speed):
	KIPR.create_drive_straight(speed)
	while KIPR.get_create_lbump()== 0 and KIPR.get_create_rbump()==0:
		pass
 	KIPR.create_drive_direct(0,0)
            
def move_servo_slow(port, current_pos, end_pos,step):
	if end_pos < current_pos:
		step = -step
	for pos in range(current_pos, end_pos, step):
		KIPR.set_servo_position(port, pos)
  		KIPR.msleep(40)
	KIPR.set_servo_position(port,end_pos)
    
            
            

            
            
            
            
            
            
            
            