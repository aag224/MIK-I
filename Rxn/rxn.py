import RPi.GPIO as GPIO
import time
from time import sleep

pin_pumps = {"1" : 13,    # Pines para cada bomba
         "2" : 22,
         "3" : 27,
         "4" : 17,
         "5" : 18}
pin_stiring = {"stir" : 12,	# Pin para la parrilla de agitación 
               "r" : 20,	# Pines de dirección de agitación
               "l" : 21}

GPIO.setmode(GPIO.BCM)		# Modo del llamado de pines
for pin in pin_pumps:		# Pines de las bombas declarados como pines de salida
    GPIO.setup(pin_pumps.get(pin),GPIO.OUT)
GPIO.setup(pin_stiring.get("stir"),GPIO.OUT) # Pin de la parrilla como pin de salida
GPIO.setup(pin_stiring.get("r"),GPIO.OUT)	 # Pines direcciones 
GPIO.setup(pin_stiring.get("l"),GPIO.OUT)
pw_s=GPIO.PWM(pin_stiring.get("stir"),500)  # Configuración de la parrilla; pin de salida y frecuencia
pw_s.start(0)                               # Corriente inicial

for pump in pin_pumps:                  # Declaración para iniciar desactivado todo los pines
    GPIO.output(pin_pumps.get(pump),1)

vol_entry = ["volp1","volp2","volp3","volp4"]
volp5 = 100
vol_assg = []
for ventry in vol_entry:                # Asignación de los volumenes a adicionar por cada bomba
    ventry = float(input("Volume_to_Add_Pump_",vol_entry.index(ventry) ,"(mL): "))
    vol_assg.append(ventry)
charge=str(input("Consider the load time? (Y/N) "))     # Definir si se considerará el tiempo de carga o no durante la adición
flow=[28,0.24,0.21,0.27,0.28]           # Lista de flujos volumetricos
tc=[1,17,18,18,17]                      # Lista de tiempos de carga

def PumpsWorkWChrg(numberPump,volume,flow,chargeTime): # Función modular para la adición de una disolución considerando el tiempo de carga
    GPIO.output(pin_pumps[str(numberPump)],0)
    print("Pump",numberPump,"_ON")
    print("Adding reactive",numberPump)
    sleep(volume/flow+chargeTime)
    print("Pump",numberPump,"_OFF")
    GPIO.output(pin_pumps[str(numberPump)],1)
    sleep(1)

def PumpsWork(numberPump,volume,flow):  # Función modular para la adición de una disolución
    GPIO.output(pin_pumps[str(numberPump)],0)
    print("Pump",numberPump,"_ON")
    print("Adding reactive",numberPump)
    sleep(volume/flow)
    print("Pump",numberPump,"_OFF")
    GPIO.output(pin_pumps[str(numberPump)],1)
    sleep(1)

def MixReac(direction,time):    # Función modular para la agitación 
    GPIO.output(pin_stiring[str(direction)],0)
    print("Stir_ON ...")
    pw_s.ChangeDutyCycle(65)
    sleep(1)
    pw_s.ChangeDutyCycle(55)
    sleep(1)
    pw_s.ChangeDutyCycle(50)
    sleep(time)
    print("Stir_OFF")
    GPIO.output(pin_stiring[str(direction)],1)
    sleep(1)

while True:     # Ciclo para la ejecución de la reacción
    if charge == "Y":   
        PumpsWorkWChrg(1,vol_assg[1],flow[1],tc[1]) # Adición del reactivo 1
        PumpsWorkWChrg(2,vol_assg[2],flow[2],tc[2])	# Adición del reactivo 2
        MixReac("r",5)					            # Inicio de la agitación
        PumpsWorkWChrg(3,vol_assg[3],flow[3],tc[3])	# Adición del reactivo 3
        PumpsWorkWChrg(4,vol_assg[4],flow[4],tc[4])	# Adición del reactivo 4
        PumpsWorkWChrg(5,volp5,flow[0],tc[0])	    # Enfriamiento
        MixReac("r",10)					            # Fin de la agitación
        break
    elif charge == "N":
        PumpsWork(1,vol_assg[1],flow[1]) 
        PumpsWork(2,vol_assg[2],flow[2]) 
        MixReac("r",5)                   
        PumpsWork(3,vol_assg[3],flow[3])  
        PumpsWork(4,vol_assg[4],flow[4])
        PumpsWork(5,volp5,flow[0])
        MixReac("r",10)
        break
    else: 
        print("Only Y or N")
        charge = str(input("Consider the load time? (Y/N) "))

GPIO.cleanup()  

