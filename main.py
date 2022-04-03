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
	KIPR.msleep(3000)
	KIPR.set_servo_position(ARM, ARM_START)
	KIPR.set_servo_position(CLAW,CLAW_OPEN)
	KIPR.enable_servos()
	print("PRESS A TO BEGIN!!!")
	while KIPR.a_button() == 0:
		pass
	print("GOOOOOOOOOOOOOOOOOO!!!!")
	#make sure not to hit red poms, turn and then move
	KIPR.msleep(1000)
	backward(300,256)
	CW(200,53)  #TURN TO BOTGUY
	
	move_servo_to_position(ARM, ARM_BOTGUY,50)
	move_servo_to_position(ARM, ARM_UP, 50)
	backward(300,720)
	KIPR.msleep(500)
	KIPR.set_servo_position(CLAW,CLAW_CLOSED)
	KIPR.msleep(500)
	KIPR.set_servo_position(ARM, ARM_UP-50) #WE GOT BOTGUY
	KIPR.msleep(500)
            
	forward(500,50) #back up from botguy
	CW(200,50)
	drive_to_bump(200)  #HIT THE TRANSPORTER!!
	KIPR.msleep(300)
	forward(100, 100)
	#CW(230,4)
	KIPR.msleep(200)
	#drive_to_bump(100)
	move_servo_to_position(ARM, ARM_DOWN,10)
	KIPR.set_servo_position(CLAW,CLAW_OPEN)
	KIPR.msleep(1000)
	KIPR.set_servo_position(ARM, ARM_UP)
	forward(200,100)
	KIPR.msleep(200)
            
	#GET OUT OF THE WAY!!!
	forward(300, 780)
	CW(200,10)
	forward(200, 500)
	
            
            
            

	#KIPR.set_servo_position(ARM, ARM_BOTGUY)
	#KIPR.msleep(1000)
	#print "Performing computations.."
	#CW(100,87)
	#backward(100,400)
	#KIPR.msleep(300)
	#print "now going to black line"
	#backward_to_black(200)
	#KIPR.msleep(500)
	#CW(100,81)
	#forward(100,500)
	#KIPR.msleep(1000)
	#KIPR.set_servo_position(CLAW,CLAW_CLOSED)
	#KIPR.msleep(1000)
	#CW(100,110)  #TURN TO LAZY SUSAN
	#forward(150,250)
	#KIPR.msleep(1000)
	#KIPR.set_servo_position(CLAW,CLAW_OPEN)
	#KIPR.msleep(1000)
	#CCW(100,90)
	KIPR.create_disconnect();
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
