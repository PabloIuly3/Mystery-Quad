import time
import pigpio


SERVO = input("pin nr1: ")
SERVO2 = input("pin nr2: ")
SERVO3 = input("pin nr3: ")

pi = pigpio.pi()

var = 1
while var == 1 :
   ser = input("select an esc to control it: ")
   if ser == 1:
      op = input("0 to stop, 1 to high, 2 for initialization, everything else to low: ")
      if op == 1:
         min = input("high min value 0 or 500-2500: ")
         max = input("max value 0 or 500-2500: ")
         while (min < max) :
            min = min + 1
            print min
            pi.set_servo_pulsewidth(SERVO, min)
      elif op == 0:
         pi.set_servo_pulsewidth(SERVO, 0)
         print "stop"
      elif op == 2:
         pi.set_servo_pulsewidth(SERVO, 1000)
         print "start innitialization"
         time.sleep(4)
         pi.set_servo_pulsewidth(SERVO, 1000)
         print "finish initialization"
      else:
         min = input("low min value 0 or 500-2500: ")
         max = input("max value 0 or 500-2500: ")
         while (min > max) :
            min = min - 1
            print min
            pi.set_servo_pulsewidth(SERVO, min)
   elif ser == 2:
      op = input("0 to stop, 1 to high, 2 for initialization, everything else to low: ")
      if op == 1:
         min = input("high min value 0 or 500-2500: ")
         max = input("max value 0 or 500-2500: ")
         while (min < max) :
            min = min + 1
            print min
            pi.set_servo_pulsewidth(SERVO2, min)
      elif op == 0:
         pi.set_servo_pulsewidth(SERVO2, 0)
         print "stop"
      elif op == 2:
         pi.set_servo_pulsewidth(SERVO2, 1000)
         print "start innitialization"
         time.sleep(4)
         pi.set_servo_pulsewidth(SERVO2, 1000)
         print "finish initialization"
      else:
         min = input("low min value 0 or 500-2500: ")
         max = input("max value 0 or 500-2500: ")
         while (min > max) :
            min = min - 1
            print min
            pi.set_servo_pulsewidth(SERVO2, min)
   elif ser == 3:
      op = input("0 to stop, 1 to high, 2 for initialization, everything else to low: ")
      if op == 1:
         min = input("high min value 0 or 500-2500: ")
         max = input("max value 0 or 500-2500: ")
         while (min < max) :
            min = min + 1
            print min
            pi.set_servo_pulsewidth(SERVO3, min)
      elif op == 0:
         pi.set_servo_pulsewidth(SERVO3, 0)
         print "stop"
      elif op == 2:
         pi.set_servo_pulsewidth(SERVO3, 1000)
         print "start innitialization"
         time.sleep(4)
         pi.set_servo_pulsewidth(SERVO3, 1000)
         print "finish initialization"
      else:
         min = input("low min value 0 or 500-2500: ")
         max = input("max value 0 or 500-2500: ")
         while (min > max) :
            min = min - 1
            print min
            pi.set_servo_pulsewidth(SERVO3, min)

pi.stop
