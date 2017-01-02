import time
import pigpio

def exit():
	pi.set_servo_pulsewidth(motor1, 0)
	pi.set_servo_pulsewidth(motor2, 0)
	pi.set_servo_pulsewidth(motor3, 0)
	pi.set_servo_pulsewidth(motor4, 0)
	print "#EXIT: I stopped the motors and I'm exit."
	print "#EXIT: Goodbye."

def stop():
	pi.set_servo_pulsewidth(motor1, 0)
	pi.set_servo_pulsewidth(motor2, 0)
	pi.set_servo_pulsewidth(motor3, 0)
	pi.set_servo_pulsewidth(motor4, 0)
	print "#STOP: I stopped the motors.\n"
	
def calibrate(ok):
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
	
def initialization(ok):
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

def control(command):

def main():
	pi = pigpio.pi()
	auto = input("Do you want to set up GPIO PINs numbers to default values? ")
	if auto == 1:
		motor1 = 4
		motor2 = 17
		motor3 = 22
		motor4 = 10
		print motor1, motor2, motor3, motor4
	elif auto == 0:
		print "Enter GPIO PINs number:"
		motor1 = input("-> motor one: ")
		motor2 = input("-> motor two: ")
		motor3 = input("-> motor three: ")
		motor4 = input("-> motor four: ")
	print "GPIO PINs numbers are set up."