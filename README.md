# Mystery Quad library
- Product: Mystery Quad library
- File: [mq1.3.6.py](https://raw.githubusercontent.com/PabloIuly3/mystery-quad/master/src/mq1.3.6.py)
- Newest version: 1.3.6
- Author: PabloIuly3
- License: MIT License
- Copyright (c) 2017 PabloIuly3

## Mystery Quad  1.3.6
### Newest control functions in 1.3.6 version
- Syntax: `control(command)`

`control(forward)` `control(backward)` `control(left)` `control(right)`

1. move to forward

2. move to backward

3. move to left

4. move to right

### Orientation and motors position
`FRONT ^`

`MOTOR 1` | `MOTOR 2`

`MOTOR 3` | `MOTOR 4`

## Mystery Quad  1.3.0
### General functions
`calibrate()` `initialization()` `test()` `stop()` `exit()` `gpio()` `help()`

1. calibrate ESCs

2. make initialization for ESCs

3. make a test before fly

4. stop the motors

5. stop the motors and exit

6. set GPIO PINs to send data

7. show help menu

### Control function
- Syntax: `control(command)`

`control(up)` `control(down)` `control(m1)` `control(m2)` `control(m3)` `control(m4)`

1. increase speed for all motors

2. decrease speed for all motors

3. increase/decrease speed for motor one

4. increase/decrease speed for motor two

5. increase/decrease speed for motor three

6. increase/decrease speed for motor four


## Simple example for usage
```markdown
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
```
