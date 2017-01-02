import time
import pigpio

def bug(motor):
	pi.set_servo_pulsewidth(motor, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor, 0)
	time.sleep(2)
	print "#BUG: Am recalibrat motorasul."
	pi.set_servo_pulsewidth(motor, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor, 1000)
	print "#BUG: Am reinitiat motorasul."
	
def exit():
	pi.set_servo_pulsewidth(motor1, 0)
	pi.set_servo_pulsewidth(motor2, 0)
	pi.set_servo_pulsewidth(motor3, 0)
	pi.set_servo_pulsewidth(motor4, 0)
	print "#EXIT: Am oprit solicitarile."

print "Mystery Quad release 1.2.0 #pabloiuly"
time.sleep(1)

print "Incarcarc programul..."
time.sleep(2)

print "Ma conectez la reteaua de pini GPIO locali."
pi = pigpio.pi()
time.sleep(3)

#GPIO PINs
print "Introdu numarul pinului GPIO pentru:"
motor1 = input("-> motorul numarul 1: ")
motor2 = input("-> motorul numarul 2: ")
motor3 = input("-> motorul numarul 3: ")
motor4 = input("-> motorul numarul 4: ")
print "Pinii de date sunt setati!"
time.sleep(3)

#ESCs CALIBRATION
calibrate = "Doresti sa calibrez controalele de viteza? (1 for YES/0 for NO) "
if calibrate == 1:
	print "Incep calibrajul. Acest proces dureaza 30 de secunde."
	time.sleep(2)

	print "Incep calibrajul pentru motorul 1."
	pi.set_servo_pulsewidth(motor1, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor1, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor1, 0)
	time.sleep(2)
	print "Am calibrat motorul 1 cu succes."
	
	print "Incep calibrajul pentru motorul 2."
	pi.set_servo_pulsewidth(motor2, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor2, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor2, 0)
	time.sleep(2)
	print "Am calibrat motorul 2 cu succes."
	
	print "Incep calibrajul pentru motorul 3."
	pi.set_servo_pulsewidth(motor3, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor3, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor3, 0)
	time.sleep(2)
	print "Am calibrat motorul 3 cu succes."
	
	print "Incep calibrajul pentru motorul 4."
	pi.set_servo_pulsewidth(motor4, 2000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor4, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(motor4, 0)
	time.sleep(2)
	print "Am calibrat motorul 4 cu succes."
	
	time.sleep(2)	
	print "Am calibrat controalele de viteza!"
elif calibrate == 0:
	print "Ok.. nu efectuez calibrajul."
else:
	print "ATENTIE! Nu am efectuat calibrajul!"
	
#ESCs INITIALIZATION
initialization = "Doresti sa initializez controalele de viteza? (1 for YES/0 for NO) "
if calibrate == 1:
	print "Incep initializarea. Acest proces dureaza 16 secunde."
	time.sleep(2)
	
	print "Incepe initializarea pentru motorul 1."
	pi.set_servo_pulsewidth(motor1, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor1, 1000)
    print "Am initializat motorul 1 cu succes."
	
	print "Incepe initializarea pentru motorul 2."
	pi.set_servo_pulsewidth(motor2, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor2, 1000)
    print "Am initializat motorul 2 cu succes."
	
	print "Incepe initializarea pentru motorul 3."
	pi.set_servo_pulsewidth(motor3, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor3, 1000)
    print "Am initializat motorul 3 cu succes."
	
	print "Incepe initializarea pentru motorul 4."
	pi.set_servo_pulsewidth(motor4, 1000)
    time.sleep(4)
    pi.set_servo_pulsewidth(motor4, 1000)
    print "Am initializat motorul 4 cu succes."
	
	time.sleep(2)	
	print "Am initializat controalele de viteza!"	 
elif calibrate == 0:
	print "Ok.. nu efectuez initializarea."
else:
	print "ATENTIE! Nu am efectuat initializarea."

test = "Doresti sa efectuezi un test inainte de utilizare? (1 for YES/0 for NO) "
if test == 1:
	print "Incep testul de functionare..."
	time.sleep(2)
	
	print "Setez variabilele de initiere la 0"
	pi.set_servo_pulsewidth(motor1, 0)
	pi.set_servo_pulsewidth(motor2, 0)
	pi.set_servo_pulsewidth(motor3, 0)
	pi.set_servo_pulsewidth(motor4, 0)
	time.sleep(4)
	
	#MOTOR 1
	print "Solicitez motorul 1. Puterea nu va urca mai mult de 1400."
	print "Incep.. 500."
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
	print "Solicitez motorul 2. Puterea nu va urca mai mult de 1400."
	print "Incep.. 500."
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
	print "Solicitez motorul 3. Puterea nu va urca mai mult de 1400."
	print "Incep.. 500."
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
	print "Solicitez motorul 4. Puterea nu va urca mai mult de 1400."
	print "Incep.. 500."
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
	
	
	#MOTORS PERFORMANCE	
	print "Solicitez toate motoarele pentru a testa performanta. Puterea nu va urca mai mult de 1500."
	print "Incep.. 500."
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
	
	print "Am efectuat testul de performanta inainte de utilizare."
	time.sleep(3)
elif test == 0:
	print "Ok.. nu efectuez testul."
else:
	print "ATENTIE! Nu am efectuat testul!"

print "Setarile au fost finalizate. Acum sa rezolvam problemele aparute la motorase."
time.sleep(2)

repeat = 1
while repeat < 1:
	command = input("Introdu un numar de comanda 1->6 (6 for help) ")
	if command == 0:
		exit()
		time.sleep(2)
		print "Goodbye!"
		pi.stop
	elif command == 1:
		m1 = input("Introdu comanda pentru motorul 1: ")
		if m1 == 0:
			print "Opresc motorul unu."
			if m1val2 == "":
				m1val2 = 500
			m1val1 = m1val2
			m1val2 = 500
			while (m1val1 > m1val2) :
				m1val1 = m1val1 - 1
				pi.set_servo_pulsewidth(motor1, m1val1)
			pi.set_servo_pulsewidth(motor1, 0)
			print "Am oprit motul unu."
		elif m1 == 1:
			if m1val2 == "":
				m1val2 = 500
			m1val1 = m1val2
			print "Plecam de la ", m1val1
			m1val2 = input("Urcam la: ")
			print "Incep..", m1val1
			while (m1val1 < m1val2) :
				m1val1 = m1val1 + 1
				pi.set_servo_pulsewidth(motor1, m1val1)
		elif m1 == 2:
			if m1val2 == "":
				m1val2 = 500
			m1val1 = m1val2
			print "Plecam de la ", m1val1
			m1val2 = input("Coboram la: ")
			print "Incep..", m1val1
			while (m1val1 > m1val2) :
				m1val1 = m1val1 - 1
				pi.set_servo_pulsewidth(motor1, m1val1)
	elif command == 2:
		m2 = input("Introdu comanda pentru motorul 2: ")
		if m2 == 0:
			print "Opresc motorul doi."
			if m2val2 == "":
				m2val2 = 500
			m2val1 = m2val2
			m2val2 = 500
			while (m2val1 > m2val2) :
				m2val1 = m2val1 - 1
				pi.set_servo_pulsewidth(motor2, m2val1)
			pi.set_servo_pulsewidth(motor2, 0)
			print "Am oprit motul doi."
		elif m2 == 1:
			if m2val2 == "":
				m2val2 = 500
			m2val1 = m2val2
			print "Plecam de la ", m2val1
			m2val2 = input("Urcam la: ")
			print "Incep..", m2val1
			while (m2val1 < m2val2) :
				m2val1 = m2val1 + 1
				pi.set_servo_pulsewidth(motor2, m2val1)
		elif m2 == 2:
			if m2val2 == "":
				m2val2 = 500
			m2val1 = m2val2
			print "Plecam de la ", m2val1
			m2val2 = input("Coboram la: ")
			print "Incep..", m2val1
			while (m2val1 > m2val2) :
				m2val1 = m2val1 - 1
				pi.set_servo_pulsewidth(motor2, m2val1)
	elif command == 3:
		m3 = input("Introdu comanda pentru motorul 3: ")
		if m3 == 0:
			print "Opresc motorul trei."
			if m3val2 == "":
				m3val2 = 500
			m3val1 = m3val2
			m3val2 = 500
			while (m3val1 > m3val2) :
				m3val1 = m3val1 - 1
				pi.set_servo_pulsewidth(motor3, m3val1)
			pi.set_servo_pulsewidth(motor3, 0)
			print "Am oprit motul trei."
		elif m3 == 1:
			if m3val2 == "":
				m3val2 = 500
			m3val1 = m3val2
			print "Plecam de la ", m3val1
			m3val2 = input("Urcam la: ")
			print "Incep..", m3val1
			while (m3val1 < m3val2) :
				m3val1 = m3val1 + 1
				pi.set_servo_pulsewidth(motor3, m3val1)
		elif m3 == 2:
			if m3val2 == "":
				m3val2 = 500
			m3val1 = m3val2
			print "Plecam de la ", m3val1
			m3val2 = input("Coboram la: ")
			print "Incep..", m3val1
			while (m3val1 > m3val2) :
				m3val1 = m3val1 - 1
				pi.set_servo_pulsewidth(motor3, m3val1)
	elif command == 4:
		m4 = input("Introdu comanda pentru motorul 4: ")
		if m4 == 0:
			print "Opresc motorul patru."
			if m4val2 == "":
				m4val2 = 500
			m4val1 = m4val2
			m4val2 = 500
			while (m4val1 > m4val2) :
				m4val1 = m4val1 - 1
				pi.set_servo_pulsewidth(motor4, m4val1)
			pi.set_servo_pulsewidth(motor4, 0)
			print "Am oprit motul patru."
		elif m4 == 1:
			if m4val2 == "":
				m4val2 = 500
			m4val1 = m4val2
			print "Plecam de la ", m4val1
			m4val2 = input("Urcam la: ")
			print "Incep..", m4val1
			while (m4val1 < m4val2) :
				m4val1 = m4val1 + 1
				pi.set_servo_pulsewidth(motor4, m4val1)
		elif m4 == 2:
			if m4val2 == "":
				m4val2 = 500
			m4val1 = m4val2
			print "Plecam de la ", m4val1
			m4val2 = input("Coboram la: ")
			print "Incep..", m4val1
			while (m4val1 > m4val2) :
				m4val1 = m4val1 - 1
				pi.set_servo_pulsewidth(motor4, m4val1)
	elif command == 5:
		m5 = input("Introdu comanda pentru simultan: ")
		if m5 == 1:
			if m5val2 == "":
				m5val2 = 500
			m5val1 = m5val2
			print "Plecam de la ", m5val1
			m5val2 = input("Urcam la: ")
			print "Incep..", m5val1
			while (m5val1 < m5val2) :
				m5val1 = m5val1 + 1
				pi.set_servo_pulsewidth(motor1, m5val1)
				pi.set_servo_pulsewidth(motor2, m5val1)
				pi.set_servo_pulsewidth(motor3, m5val1)
				pi.set_servo_pulsewidth(motor4, m5val1)
		elif m5 == 2:
			if m5val2 == "":
				m5val2 = 500
			m5val1 = m5val2
			print "Plecam de la ", m5val1
			m5val2 = input("Coboram la: ")
			print "Incep..", m5val1
			while (m5val1 > m5val2) :
				m5val1 = m5val1 - 1
				pi.set_servo_pulsewidth(motor1, m5val1)
				pi.set_servo_pulsewidth(motor2, m5val1)
				pi.set_servo_pulsewidth(motor3, m5val1)
				pi.set_servo_pulsewidth(motor4, m5val1)
	elif command == 6:
		print "Welcome to Help Menu"
		time.sleep(2)
		print "#########################################"
		print "Product: Mystery Quad"
		print "Version: 1.2.0 RELEASE"
		print "Author: PabloIuly"
		print "Year: 2016"
		print "#########################################"
		print "Lista cu comenzi:"
		print "->0 pentru a opri toate motoarele"
		
		print "->1 comenzi pentru motorul unu:"
		print "-0 pentru a opri motorul:"
		print "-1 pentru a mari puterea motorului:"
		print "-2 pentru a micsora puterea motorului:"
		
		print "->2 comenzi pentru motorul doi:"
		print "-0 pentru a opri motorul:"
		print "-1 pentru a mari puterea motorului:"
		print "-2 pentru a micsora puterea motorului:"
		
		print "->3 comenzi pentru motorul trei:"
		print "-0 pentru a opri motorul:"
		print "-1 pentru a mari puterea motorului:"
		print "-2 pentru a micsora puterea motorului:"
		
		print "->4 comenzi pentru motorul patru:"
		print "-0 pentru a opri motorul:"
		print "-1 pentru a mari puterea motorului:"
		print "-2 pentru a micsora puterea motorului:"
		
		print "->5 comenzi pentru toate motoarele:"
		print "-1 pentru a mari puterea motoarelor:"
		print "-2 pentru a micsora puterea motoarelor:"
		
		print "->6 pentru meniul de ajutor"

#pi.set_servo_pulsewidth(motor1, val1)
#while (val1 < max) :