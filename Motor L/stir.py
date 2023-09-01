import RPi.GPIO as GPIO
import time
from time import sleep

motor_A=12
lstir=16
rstir=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_A,GPIO.OUT)
GPIO.setup(lstir,GPIO.OUT)
GPIO.setup(rstir,GPIO.OUT)

pw_A=GPIO.PWM(motor_A,500)
pw_A.start(0)

print("-Choose direction L or R \n -Choose velocity 0-100")
print("Example for a command: 'L50' (direction, velocity) \n \n")
cmd=input("Insert command: ")
tim=int(input("Operation time (s): "))
cmd=cmd.lower()
direct=cmd[0]
velocity=cmd[1:3]

def Dir_L_motor():
	GPIO.output(lstir,0)
	print("Stir Left ON")
	sleep(tim)
	GPIO.output(lstir,1)
	print("Stir Left OFF")
	sleep(1)
def Dir_R_motor():
	GPIO.output(rstir,1)
	print("Stir Right ON")
	sleep(tim)
	GPIO.output(rstir,0)
	print("Stir Rigth OFF")
	sleep(1)



if direct == 'L':
	print("vel=+velocity")
	pw_A.ChangeDutyCycle(int(velocity))
	Dir_L_motor()
elif direct == "R":
	print("vel=+velocity")
	pw_A.ChangeDutyCycle(int(velocity))
	Dir_R_motor()
else:
	print("You are not selecting a corresponding direction, please, only choose 'L' or 'R'")

pw_A.stop()
GPIO.cleaunup()
