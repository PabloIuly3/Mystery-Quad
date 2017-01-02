import time
import pigpio

# Product: Mystery Quad library
# Version: 1.3.0
# Author: PabloIuly3
# Year: 2017
# License: MIT License

# Copyright (c) 2017 Pablo
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# WARNING! Mystery Quad use 'pigpio' to send servo pulses to ESCs.
# Please download it (http://abyz.co.uk/rpi/pigpio/) and run before run Mystery Quad library.

def exit():
	pi.set_servo_pulsewidth(motor1, 0)
	pi.set_servo_pulsewidth(motor2, 0)
	pi.set_servo_pulsewidth(motor3, 0)
	pi.set_servo_pulsewidth(motor4, 0)
	print "#EXIT: I stopped the motors and I'm exit."
	print "#EXIT: Goodbye."
	repeat = 0
def stop():
	pi.set_servo_pulsewidth(motor1, 0)
	pi.set_servo_pulsewidth(motor2, 0)
	pi.set_servo_pulsewidth(motor3, 0)
	pi.set_servo_pulsewidth(motor4, 0)
	print "#STOP: I stopped the motors.\n"
def calibrate():
	print "Start to calibrate. This process was approximate 30 seconds.\n"

	print "Start to calibrate motor one."
	pi.set_servo_pulsewidth(motor1, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor1, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor1, 0)
	time.sleep(2)
	print "Finish motor one.\n"
	
	print "Start to calibrate motor two."
	pi.set_servo_pulsewidth(motor2, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor2, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor2, 0)
	time.sleep(2)
	print "Finish motor two.\n"
	
	print "Start to calibrate motor three."
	pi.set_servo_pulsewidth(motor3, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor3, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor3, 0)
	time.sleep(2)
	print "Finish motor three.\n"
	
	print "Start to calibrate motor four."
	pi.set_servo_pulsewidth(motor4, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor4, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor4, 0)
	time.sleep(2)
	print "Finish motor four.\n"
	
	time.sleep(2)	
	print "Finish to calibrate motors.\n"
def initialization():
	print "Start to initiate motors. This process was approximate 15 seconds.\n"
	
	print "Start to initiate motor one."
	pi.set_servo_pulsewidth(motor1, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor1, 1000)
    print "Finish motor one.\n"
	
	print "Start to initiate motor two."
	pi.set_servo_pulsewidth(motor2, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor2, 1000)
    print "Finish motor two.\n"
	
	print "Start to initiate motor three."
	pi.set_servo_pulsewidth(motor3, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor3, 1000)
    print "Finish motor three.\n"
	
	print "Start to initiate motor four."
	pi.set_servo_pulsewidth(motor4, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor4, 1000)
    print "Finish motor four.\n"	
	time.sleep(2)	
	
	stop()
	print "Finish to initaite motors.\n"
def test():
	pi.set_servo_pulsewidth(motor1, 0)
	pi.set_servo_pulsewidth(motor2, 0)
	pi.set_servo_pulsewidth(motor3, 0)
	pi.set_servo_pulsewidth(motor4, 0)
	time.sleep(2)
	
	#MOTOR 1
	print "Test motor one. Maximum power: 1400."
	print "Start.. 500."
	val1 = 500
	val2 = 1400
	while (val1 < val2) :
        val1 = val1 + 1
        pi.set_servo_pulsewidth(motor1, val1)	
	time.sleep(3)
	
	val1 = 1400
	val2 = 1100
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor1, val1)
	time.sleep(2)	
	
	val1 = 1100
	val2 = 900
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor1, val1)
        pi.set_servo_pulsewidth(motor1, 0)
	time.sleep(2)
	
	
	#MOTOR 2
	print "Test motor two. Maximum power: 1400."
	print "Start.. 500."
	val1 = 500
	val2 = 1400
	while (val1 < val2) :
        val1 = val1 + 1
        pi.set_servo_pulsewidth(motor2, val1)	
	time.sleep(3)
	
	val1 = 1400
	val2 = 1100
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor2, val1)
	time.sleep(2)
	
	val1 = 1100
	val2 = 900
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor2, val1)
        pi.set_servo_pulsewidth(motor2, 0)
	time.sleep(2)
	
	
	#MOTOR 3
	print "Test motor three. Maximum power: 1400."
	print "Start.. 500."
	val1 = 500
	val2 = 1400
	while (val1 < val2) :
        val1 = val1 + 1
        pi.set_servo_pulsewidth(motor3, val1)	
	time.sleep(3)
	
	val1 = 1400
	val2 = 1100
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor3, val1)
	time.sleep(2)
	
	val1 = 1100
	val2 = 900
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor3, val1)
        pi.set_servo_pulsewidth(motor3, 0)
	time.sleep(2)
	
	
	#MOTOR 4
	print "Test motor four. Maximum power: 1400."
	print "Start.. 500."
	val1 = 500
	val2 = 1400
	while (val1 < val2) :
        val1 = val1 + 1
        pi.set_servo_pulsewidth(motor1, val1)	
	time.sleep(3)
	
	val1 = 1400
	val2 = 1100
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor1, val1)
	time.sleep(2)
	
	val1 = 1100
	val2 = 900
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor1, val1)
        pi.set_servo_pulsewidth(motor1, 0)
	time.sleep(2)
	
	#ALL MOTORS
	print "Test all motors. Maximum power: 1500."
	print "Start.. 500."
	val1 = 500
	val2 = 1300
	while (val1 < val2) :
        val1 = val1 + 1
        pi.set_servo_pulsewidth(motor1, val1)	
        pi.set_servo_pulsewidth(motor2, val1)	
        pi.set_servo_pulsewidth(motor3, val1)	
        pi.set_servo_pulsewidth(motor4, val1)	
	time.sleep(3)
	
	val1 = 1300
	val2 = 1500
	while (val1 < val2) :
        val1 = val1 + 1
        pi.set_servo_pulsewidth(motor1, val1)	
        pi.set_servo_pulsewidth(motor2, val1)	
        pi.set_servo_pulsewidth(motor3, val1)	
        pi.set_servo_pulsewidth(motor4, val1)	
	time.sleep(2)
	
	val1 = 1500
	val2 = 900
	while (val1 > val2) :
        val1 = val1 - 1
        pi.set_servo_pulsewidth(motor1, val1)
        pi.set_servo_pulsewidth(motor2, val1)
        pi.set_servo_pulsewidth(motor3, val1)
        pi.set_servo_pulsewidth(motor4, val1)
        pi.set_servo_pulsewidth(motor1, 0)
        pi.set_servo_pulsewidth(motor2, 0)
        pi.set_servo_pulsewidth(motor3, 0)
        pi.set_servo_pulsewidth(motor4, 0)
	time.sleep(2)
	
	print "Test finished"
def help():
	print "#########################################"
	print "Product: Mystery Quad"
	print "Version: 1.3.0"
	print "Author: PabloIuly3"
	print "Year: 2017"
	print "License: MIT License"
	print "Copyright (c) 2017 PabloIuly3"
	print "#########################################\n"
	
	print "Command:"
	print "-calibrate: calibrate ESCs"
	print "-initialization: make initialization for ESCs"
	print "-test: make a test before fly"
	print "-exit: stop the motors and exit"
	print "-stop: stop the motors\n"	
	
	print "For control:"
	print "-up: increase speed for all motors"
	print "-down: decrease speed for all motors"
	print "-m1: increase/decrease speed for motor one"
	print "-m2: increase/decrease speed for motor two"
	print "-m3: increase/decrease speed for motor three"
	print "-m4: increase/decrease speed for motor four\n"
def values():
	if m1val2 == "":
		m1val2 = 500
	if m2val2 == "":
		m2val2 = 500
	if m3val2 == "":
		m3val2 = 500
	if m4val2 == "":
		m4val2 = 500
def gpio():
	pi = pigpio.pi()
	print "Enter GPIO PINs number:"
	motor1 = input("-> motor one: ")
	motor2 = input("-> motor two: ")
	motor3 = input("-> motor three: ")
	motor4 = input("-> motor four: ")
	
def control(command):
	if command == "calibrate":
		calibrate()
	elif command == "initialization":
		initialization()
	elif command == "test":
		test()
	elif command == "exit":
		exit()
	elif command == "stop":
		stop()		
	elif command == "up":
		values()
		print "Current speed: ", m1val1, m2val1, m3val1, m4val1
		m1val2 = input("Increase speed at: ")
		while (m1val1 < m1val2) :
			m1val1 = m1val1 + 1
			m2val1 = m2val1 + 1
			m3val1 = m3val1 + 1
			m4val1 = m4val1 + 1
			pi.set_servo_pulsewidth(motor1, m1val1)
			pi.set_servo_pulsewidth(motor2, m2val1)
			pi.set_servo_pulsewidth(motor3, m3val1)
			pi.set_servo_pulsewidth(motor4, m4val1)
		m2val2 = m2val1
		m3val2 = m3val1
		m4val2 = m4val1
	elif command == "down":
		values()
		print "Curent speed ", m1val1, m2val1, m3val1, m4val1
		m1val2 = input("Decrease speed at: ")		
		while (m1val1 > m1val2) :
			m1val1 = m1val1 - 1
			m2val1 = m2val1 - 1
			m3val1 = m3val1 - 1
			m4val1 = m4val1 - 1
			pi.set_servo_pulsewidth(motor1, m1val1)
			pi.set_servo_pulsewidth(motor2, m2val1)
			pi.set_servo_pulsewidth(motor3, m3val1)
			pi.set_servo_pulsewidth(motor4, m4val1)
		m2val2 = m2val1
		m3val2 = m3val1
		m4val2 = m4val1		
	elif command == "m1":
		m1 = input("Enter a command for motor one:")
		if m1 == "stop":
			if m1val2 == "":
				m1val2 = 500
			m1val1 = m1val2
			m1val2 = 500
			while (m1val1 > m1val2) :
				m1val1 = m1val1 - 1
				pi.set_servo_pulsewidth(motor1, m1val1)
			pi.set_servo_pulsewidth(motor1, 0)
		elif m1 == "up":
			if m1val2 == "":
				m1val2 = 500
			m1val1 = m1val2
			print "Current speed: ", m1val1
			m1val2 = input("Increase speed at: ")
			print "Start..", m1val1
			while (m1val1 < m1val2) :
				m1val1 = m1val1 + 1
				pi.set_servo_pulsewidth(motor1, m1val1)
		elif m1 == "down":
			if m1val2 == "":
				m1val2 = 500
			m1val1 = m1val2
			print "Current speed: ", m1val1
			m1val2 = input("Decrease speed at: ")
			print "Start..", m1val1
			while (m1val1 > m1val2) :
				m1val1 = m1val1 - 1
				pi.set_servo_pulsewidth(motor1, m1val1)
	elif command == "m2":
		m2 = input("Enter a command for motor two: ")
		if m2 == "stop":
			if m2val2 == "":
				m2val2 = 500
			m2val1 = m2val2
			m2val2 = 500
			while (m2val1 > m2val2) :
				m2val1 = m2val1 - 1
				pi.set_servo_pulsewidth(motor2, m2val1)
			pi.set_servo_pulsewidth(motor2, 0)
		elif m2 == "up":
			if m2val2 == "":
				m2val2 = 500
			m2val1 = m2val2
			print "Current speed:  ", m2val1
			m2val2 = input("Increase at: ")
			print "Start..", m2val1
			while (m2val1 < m2val2) :
				m2val1 = m2val1 + 1
				pi.set_servo_pulsewidth(motor2, m2val1)
		elif m2 == "down":
			if m2val2 == "":
				m2val2 = 500
			m2val1 = m2val2
			print "Current speed:  ", m2val1
			m2val2 = input("Decrease at: ")
			print "Start..", m2val1
			while (m2val1 > m2val2) :
				m2val1 = m2val1 - 1
				pi.set_servo_pulsewidth(motor2, m2val1)
	elif command == "m3":
		m3 = input("Enter a command for motor three: ")
		if m3 == "stop":
			if m3val2 == "":
				m3val2 = 500
			m3val1 = m3val2
			m3val2 = 500
			while (m3val1 > m3val2) :
				m3val1 = m3val1 - 1
				pi.set_servo_pulsewidth(motor3, m3val1)
			pi.set_servo_pulsewidth(motor3, 0)
		elif m3 == "up":
			if m3val2 == "":
				m3val2 = 500
			m3val1 = m3val2
			print "Current speed:  ", m3val1
			m3val2 = input("Increase at: ")
			print "Start..", m3val1
			while (m3val1 < m3val2) :
				m3val1 = m3val1 + 1
				pi.set_servo_pulsewidth(motor3, m3val1)
		elif m3 == "down":
			if m3val2 == "":
				m3val2 = 500
			m3val1 = m3val2
			print "Current speed:  ", m3val1
			m3val2 = input("Decrease at: ")
			print "Start..", m3val1
			while (m3val1 > m3val2) :
				m3val1 = m3val1 - 1
				pi.set_servo_pulsewidth(motor3, m3val1)
	elif command == "m4":
		m4 = input("Enter a command for motor four: ")
		if m4 == "stop":
			if m4val2 == "":
				m4val2 = 500
			m4val1 = m4val2
			m4val2 = 500
			while (m4val1 > m4val2) :
				m4val1 = m4val1 - 1
				pi.set_servo_pulsewidth(motor4, m4val1)
			pi.set_servo_pulsewidth(motor4, 0)
		elif m4 == "up":
			if m4val2 == "":
				m4val2 = 500
			m4val1 = m4val2
			print "Current speed:  ", m4val1
			m4val2 = input("Increase at: ")
			print "Start..", m4val1
			while (m4val1 < m4val2) :
				m4val1 = m4val1 + 1
				pi.set_servo_pulsewidth(motor4, m4val1)
		elif m4 == "down":
			if m4val2 == "":
				m4val2 = 500
			m4val1 = m4val2
			print "Current speed:  ", m4val1
			m4val2 = input("Decrease at: ")
			print "Start..", m4val1
			while (m4val1 > m4val2) :
				m4val1 = m4val1 - 1
				pi.set_servo_pulsewidth(motor4, m4val1)
	else:
		help()
		
# Simple example for use MQ #		
gpio()
a = input("Do you want to calibrate and initiate ESCs? [recommanded] (y/n)")
if a == "y":
	calibrate()
	initialization()

b = input("Do you want to make a test before fly? (y/n)")
if b == "y":
	test()
	
print "Ready to fly!"

repeat = 1
while repeat == 1:
	c = input("Enter command to do: ")
	control(c)
