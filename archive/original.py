import time
import pigpio

SERVO = input("pin nr: ")

pi = pigpio.pi()

pi.set_servo_pulsewidth(SERVO, 2000)
time.sleep(3)
pi.set_servo_pulsewidth(SERVO, 1000)
time.sleep(3)
pi.set_servo_pulsewidth(SERVO, 0)
time.sleep(2)

pi.stop

