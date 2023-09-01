from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO
import time
from time import sleep

root = Tk()
root.title("MIK-I")
ventana = Canvas(root, bg="white", height=650, width=1200)

pump1=13
pump2=22
pump3=27
pump4=17
pump5=18


pump1=ventana.create_oval(50,40,200,190,outline="black")
c1=ventana.create_oval(120,110,130,120,fill="silver", outline="black")
pump1_label=Label(text="Pump 1",bg='white',font=("Cambria",13))
pump1_label.place(x=90,y=8)
pump2=ventana.create_oval(250,40,400,190,fill="green", outline="black")
c2=ventana.create_oval(320,110,330,120,fill="silver", outline="")
pump2_label=Label(text="Pump 5",bg='white',font=("Cambria",13))
pump2_label.place(x=290,y=8)
pump3=ventana.create_oval(450,40,600,190,fill="green", outline="black")
c3=ventana.create_oval(520,110,530,120,fill="silver", outline="")
pump3_label=Label(text="Pump 2",bg='white',font=("Cambria",13))
pump3_label.place(x=490,y=8)
pump4=ventana.create_oval(650,40,800,190,fill="green", outline="black")
c4=ventana.create_oval(720,110,730,120,fill="silver", outline="")
pump4_label=Label(text="Pump 3",bg='white',font=("Cambria",13))
pump4_label.place(x=690,y=8)
pump5=ventana.create_oval(850,40,1000,190,fill="green", outline="black")
c5=ventana.create_oval(920,110,930,120,fill="silver", outline="")
pump5_label=Label(text="Pump 4",bg='white',font=("Cambria",13))
pump5_label.place(x=890,y=8)
pump6=ventana.create_oval(150,350,300,500,fill="green", outline="black")
c6=ventana.create_oval(220,420,230,430,fill="silver", outline="")
pump6_label=Label(text="Pump 6",bg='white',font=("Cambria",13))
pump6_label.place(x=190,y=320)
pump7=ventana.create_oval(350,350,500,500,fill="green", outline="black")
c7=ventana.create_oval(420,420,430,430,fill="silver", outline="")
pump7_label=Label(text="Pump 7",bg='white',font=("Cambria",13))
pump7_label.place(x=390,y=320)
pump8=ventana.create_oval(550,350,700,500,fill="green", outline="black")
c8=ventana.create_oval(620,420,630,430,fill="silver", outline="")
pump8_label=Label(text="Pump 8",bg='white',font=("Cambria",13))
pump8_label.place(x=590,y=320)
pump9=ventana.create_oval(750,350,900,500,fill="green", outline="black")
c9=ventana.create_oval(820,420,830,430,fill="silver", outline="")
pump9_label=Label(text="Pump 9",bg='white',font=("Cambria",13))
pump9_label.place(x=790,y=320)
pump10=ventana.create_oval(950,350,1100,500,fill="green", outline="black")
c10=ventana.create_oval(1020,420,1030,430,fill="silver", outline="")
pump10_label=Label(text="Pump 10",bg='white',font=("Cambria",13))
pump10_label.place(x=990,y=320)


def bomba1ON():
    GPIO.setmode(GPIO.BCM)
    pump1=13
    GPIO.setup(pump1,GPIO.OUT)
    GPIO.output(pump1,0)
    print("Pump 1 ON")
Button(root, text="ON",command=bomba1ON).place(x=100,y=200)
def bomba2ON():
    GPIO.setmode(GPIO.BCM)
    pump2=22
    GPIO.setup(pump2,GPIO.OUT)
    GPIO.output(pump2,0)
    print("Pump 2 ON")
Button(root, text="ON",command=bomba2ON).place(x=500,y=200)
def bomba3ON():
    GPIO.setmode(GPIO.BCM)
    pump3=27
    GPIO.setup(pump3,GPIO.OUT)
    GPIO.output(pump3,0)
    print("Pump 3 ON")
Button(root, text="ON",command=bomba3ON).place(x=700,y=200)
def bomba4ON():
    GPIO.setmode(GPIO.BCM)
    pump4=17
    GPIO.setup(pump4,GPIO.OUT)
    GPIO.output(pump4,0)
    print("Pump 4 ON")
Button(root, text="ON",command=bomba4ON).place(x=900,y=200)  
def bomba5ON():
    GPIO.setmode(GPIO.BCM)
    pump5=18
    GPIO.setup(pump5,GPIO.OUT)
    GPIO.output(pump5,0)
    print("Pump 5 ON")
Button(root, text="ON",command=bomba5ON).place(x=300,y=200)

"""
Button(root, text="ON",command="").place(x=200,y=510)
Button(root, text="ON",command="").place(x=400,y=510)
Button(root, text="ON",command="").place(x=600,y=510)
Button(root, text="ON",command="").place(x=800,y=510)
Button(root, text="ON",command="").place(x=1000,y=510)
"""

def bomba1OFF():
    GPIO.setmode(GPIO.BCM)
    pump1=13
    GPIO.setup(pump1,GPIO.OUT)
    GPIO.output(pump1,1)
    print("Pump 1 OFF")
Button(root, text="OFF",command=bomba1OFF).place(x=98,y=240)
def bomba2OFF():
    GPIO.setmode(GPIO.BCM)
    pump2=22
    GPIO.setup(pump2,GPIO.OUT)
    GPIO.output(pump2,1)
    print("Pump 2 OFF")
Button(root, text="OFF",command=bomba2OFF).place(x=498,y=240)
def bomba3OFF():
    GPIO.setmode(GPIO.BCM)
    pump3=27
    GPIO.setup(pump3,GPIO.OUT)
    GPIO.output(pump3,1)
    print("Pump 3 OFF")
Button(root, text="OFF",command=bomba3OFF).place(x=698,y=240)
def bomba4OFF():
    GPIO.setmode(GPIO.BCM)
    pump4=17
    GPIO.setup(pump4,GPIO.OUT)
    GPIO.output(pump4,1)
    print("Pump 4 OFF")
Button(root, text="OFF",command=bomba4OFF).place(x=898,y=240)
def bomba5OFF():
    GPIO.setmode(GPIO.BCM)
    pump5=18
    GPIO.setup(pump5,GPIO.OUT)
    GPIO.output(pump5,1)
    print("Pump 5 OFF")
Button(root, text="OFF",command=bomba5OFF).place(x=298,y=240)

"""
Button(root, text="OFF",command="").place(x=198,y=550)
Button(root, text="OFF",command="").place(x=398,y=550)
Button(root, text="OFF",command="").place(x=598,y=550)
Button(root, text="OFF",command="").place(x=798,y=550)
Button(root, text="OFF",command="").place(x=998,y=550)
"""

ventana.pack()
mainloop()
GPIO.cleanup()

#the lines that are commented 