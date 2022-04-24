#!/usr/bin/python
import os, sys
import ctypes
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
from motion import *
from effectors import *

def main():
	print "ATTEMPTING TO CONNECT TO CREATE..."
	KIPR.create_connect()
	print "CONNECTED"
	KIPR.create_full()
	KIPR.set_servo_position(ARM, ARM_START)
	KIPR.set_servo_position(CLAW,CLAW_CLOSED)
	KIPR.enable_servos()

	print("PRESS A TO BEGIN!!!")
	while KIPR.a_button() == 0:
		pass
	print("GOOOOOOOOOOOOOOOOOO!!!!")
	#make sure not to hit red poms, turn and then move
	KIPR.msleep(1500)
	backward(400,100)
	CW(200,50)  #TURN TO BOTGUY
	
	move_servo_to_position(ARM, ARM_BOTGUY,50)
	move_servo_to_position(ARM, ARM_UP, 50)
	KIPR.set_servo_position(CLAW,CLAW_OPEN)
	backward(400,880) 
	KIPR.msleep(500)
	CCW(100, 10) # TURN TO BOTGUY
	backward(200,60)
	
	KIPR.set_servo_position(CLAW,CLAW_CLOSED)
	KIPR.msleep(250)
	KIPR.set_servo_position(ARM, ARM_UP-50) #WE GOT BOTGUY
	KIPR.msleep(250)

	forward(500,10) #back up from botguy
	KIPR.msleep(750)
	CW(200,65)  #turn to transporter
	KIPR.msleep(750)
	backward(200,600)
	CW(100,30)
	backward(100,200)
	CCW(100,30)
	drive_to_bump(200)  #HIT THE TRANSPORTER!!
	forward(200,30)
	CCW(100,105)
	forward(100,500) #DRIVE TO PIPE
	backward(100, 50)
	CW(100,50)
	backward(100, 100)
	move_servo_to_position(ARM, ARM_DOWN,10)
	KIPR.set_servo_position(CLAW,CLAW_OPEN)
	KIPR.msleep(1000)
            
	#DELIVERED GET OUT OF THE WAY!!!
	forward(200, 100)
	KIPR.set_servo_position(ARM, ARM_UP)
	KIPR.msleep(200)
	CCW(100, 90) 
	drive_to_bump(200) 
	
            
            
            
            
            	
	#THE OLD ROUTINEE!
	
	"""
	CW(100, 25)
	KIPR.msleep(300)
	forward(100, 100)
	#CW(230, 30)
	KIPR.msleep(750)
	#drive_to_bump(100)
	move_servo_to_position(ARM, ARM_DOWN,10)
	KIPR.set_servo_position(CLAW,CLAW_OPEN)
	KIPR.msleep(1000)
	forward(200,75)
	KIPR.set_servo_position(ARM, ARM_UP)
	KIPR.msleep(200)
            
	#GET OUT OF THE WAY!!!
	forward(300, 100)
	CW(200, 70)
	forward(200, 500)
	backward(200,200)
	CW(200,50)
	move_servo_to_position(ARM, ARM_DOWN,10)
	KIPR.set_servo_position(CLAW,CLAW_OPEN)
            
    """
	KIPR.create_disconnect();
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
