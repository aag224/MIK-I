from tkinter import *
from tkinter import messagebox, ttk
import tkinter.font as font
import RPi.GPIO as GPIO
import time
from time import sleep
import threading

pps = [13,24,22,27,17,23,18,12,4,7]
strpins = [12, 20] 

root = Tk()
root.title('MIK-I')
ventana = Canvas(root, bg="white", height=660, width=1100)
var_s = IntVar()
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
var_5 = IntVar()
var_6 = IntVar()
var_7 = IntVar()
var_8 = IntVar()
var_9 = IntVar()
addt = IntVar()
sttr = IntVar()
strtm = IntVar()

ordrLabel = Label(text="Addition",bg="white",font=("Arial Nova",13))
ordrLabel.place(x=290,y=585)
radio1 = Radiobutton(ventana, text="Parallel", variable=addt,bg="white",value=1)
radio1.place(x=240,y=615)
radio2 = Radiobutton(ventana, text="In-Order", variable=addt,bg="white", value=2)
radio2.place(x=340,y=615)
strLabel = Label(text="Stirring",bg="white",font=("Arial Nova",13))
strLabel.place(x=600,y=585)
stgstr = Label(text="Stage",bg="white",font=("Arial Nova",10))
stgstr.place(x=475,y=615)
tmstr = Label(text="Time (min)",bg="white",font=("Arial Nova",10))
tmstr.place(x=685,y=615)
chkstr = Checkbutton(ventana, text="No  ",variable=sttr,onvalue=0,offvalue=0, height=1,width=2, bg= "white")
chkstr.place(x=520,y=615)
chkstr = Checkbutton(ventana, text="1",variable=sttr,onvalue=1,offvalue=0, height=1,width=2, bg= "white")
chkstr.place(x=560,y=615)
chkstr = Checkbutton(ventana, text="2",variable=sttr,onvalue=2,offvalue=0, height=1,width=2, bg= "white")
chkstr.place(x=600,y=615)
chkstr = Checkbutton(ventana, text="3",variable=sttr,onvalue=3,offvalue=0, height=1,width=2, bg= "white")
chkstr.place(x=640,y=615)



for z in range(4):
    labvol = Label(ventana, text = "Vol (ml): ")
    labvol.place(x=231+200*z,y=248)
    labvolb = Label(ventana, text = "Vol (ml): ")
    labvolb.place(x=91+200*(z+1),y=548)
labvols=Label(ventana, text=" Vol (ml):")
labvols.place(x=28,y=248)
labvolc = Label(ventana, text="Vol (ml): ")
labvolc.place(x=91,y=548)

pump1 = ventana.create_oval(50,60,200,210,outline="black")
pump1_label = Label(text="Service Pump",bg='white',font=("Arial Nova",13))
pump1_label.place(x=85,y=25)
c1=ventana.create_oval(120,130,130,140,fill="silver", outline="black")
volents = Entry(ventana,  width=8, textvariable=var_s)
volents.place(x=90,y=248)
volent1 = Entry(ventana,  width=8, textvariable=var_1)
volent1.place(x=290,y=248)
volent2=Entry(ventana,  width=8, textvariable=var_2)
volent2.place(x=490,y=248)
volent3 = Entry(ventana,  width=8, textvariable=var_3)
volent3.place(x=690,y=248) 
volent4 = Entry(ventana,  width=8, textvariable=var_4)
volent4.place(x=890,y=248)

for p in range(4):
    global pumpi
    pumpi = ventana.create_oval(250+200*p,60,400+200*p,210,fill="green",outline="black")
    pumpi_lbl = Label(text="Pump "+str(p+1),bg='white',font=("Arial Nova",13))
    pumpi_lbl.place(x=300+200*p,y=25)
    ci = ventana.create_oval(320+200*p,130,330+200*p,140,fill="silver", outline="")

volent5 = Entry(ventana,  width=8, textvariable=var_5)
volent5.place(x=150,y=548)
volent6 = Entry(ventana,  width=8, textvariable=var_6)
volent6.place(x=350,y=548)
volent7 = Entry(ventana,  width=8, textvariable=var_7)
volent7.place(x=550,y=548)
volent8 = Entry(ventana,  width=8, textvariable=var_8)
volent8.place(x=750,y=548)
volent9 = Entry(ventana,  width=8, textvariable=var_9)
volent9.place(x=950,y=548)
velentstr = Entry(ventana, width=7, textvariable=strtm)
velentstr.place(x=765,y=613)

for q in range(5):
    global pmpi 
    pmpi = ventana.create_oval(110+200*q,350,260+200*q,500,fill="green",outline="black")
    pmpi_lbl = Label(text="Pump "+str(q+5),bg="white",font=("Arial Nova",13))
    pmpi_lbl.place(x=160+200*q,y=320)
    cii = ventana.create_oval(180+200*q,420,190+200*q,430,fill="silver", outline="")

def chyorn():
    global mroot
    global vs
    vols = volents.get()
    if vols.isdigit():
        vs = sum(float(digit) * 10 ** i for i, digit in enumerate(vols[::-1]))
        vs = vs
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global v1
    vol1 = volent1.get()
    if vol1.isdigit():
        v1 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol1[::-1]))
        v1 = v1
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global v2
    vol2 = volent2.get()
    if vol2.isdigit():
        v2 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol2[::-1]))
        v2 = v2        
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global v3
    vol3 = volent3.get()
    if vol3.isdigit():
        v3 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol3[::-1]))
        v3 = v3            
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global v4
    vol4 = volent4.get()
    if vol4.isdigit():
        v4 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol4[::-1]))
        v4 = v4
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global v5
    vol5 = volent5.get()
    if vol5.isdigit():
        v5 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol5[::-1]))
        v5 = v5
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global v6
    vol6 = volent6.get()
    if vol6.isdigit():
        v6 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol6[::-1]))
        v6 = v6
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global v7
    vol7 = volent7.get()
    if vol7.isdigit():
        v7 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol7[::-1]))
        v7 = v7
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global v8
    vol8 = volent8.get()
    if vol8.isdigit():
        v8 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol8[::-1]))
        v8 = v8
    else:
        messagebox.showerror("Error","Only numbers !!")   
        return     
    global v9
    vol9 = volent9.get()
    if vol9.isdigit():
        v9 = sum(float(digit) * 10 ** i for i, digit in enumerate(vol9[::-1]))
        v9 = v9
    else:
        messagebox.showerror("Error","Only numbers !!")
        return
    global tmstr
    velstr = velentstr.get()
    if velstr.isdigit():
        tmstr = sum(float(digit) * 10 ** i for i, digit in enumerate(velstr[::-1]))
        tmstr = tmstr
    else:
        messagebox.showerror("Error", "Only numbers !!")
    
    mroot = Tk()
    mroot.title(" ")
    mroot.geometry(f"200x110+{550}+{350}")
    labelr1 = Label(mroot, text="    Consider the load time ?")
    labelr1.grid(row=0, column=0, columnspan=2, ipady=10)
    button1 = Button(mroot, command=rxnY, text="YES")
    button1.grid(row=1, column=1, ipadx=15, padx=20)
    button2 = Button(mroot, command=rxnN, text="NO")
    button2.grid(row=2, column=1, ipadx=15, padx=20)
    srtButton.config(state='disable')
def rxnY():
    mroot.destroy()
    flow=[28,0.265,0.2345,0.21,0.262,0.22,0.22,0.22,0.22,0.22]
    tc=[2,16,17,21,15,18,17,18,19,10]

    def wmk():
        if tmstr != 0:
            def stir1():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(tmstr*60+(v1/flow[1]+tc[1])+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(tmstr*60+(v1/flow[1]+tc[1])+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir2():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep((tmstr*60)+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir3():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(tmstr*60+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
        elif tmstr == 0:
            def stir():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(30+(v1/flow[1]+tc[1])+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir1():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(30+(v1/flow[1]+tc[1])+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir2():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(30+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir3():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(30+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
        else:
            def stir():
                d=1
            def stir1():
                xd=1
            def stir2():
                fd=1
            def stir3():
                sd=1
        if vs != 0: 
            def Pmps():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[0],GPIO.OUT)
                GPIO.output(pps[0],0)
                print("PumpService_ON")
                sleep(vs/flow[0]+tc[0])
                print("PumpService_OFF")
                GPIO.output(pps[0],1)
                sleep(1)
            def PmpsTD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[0],GPIO.OUT)
                GPIO.output(pps[0],1)
                sleep((v2/flow[2])+(v1/flow[1]))
                GPIO.output(pps[0],0)
                sleep(vs/flow[0]+tc[0])
                GPIO.output(pps[0],1)
                sleep(1)
        elif vs == 0:
            def Pmps():
                a=1
            def PmpsTD():
                ax=1
        if v1 != 0:
            def Pmp1():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[1],GPIO.OUT)
                GPIO.output(pps[1],0)
                print("Pump1_ON")
                sleep(v1/flow[1]+tc[1])
                print("Pump1_OFF")
                GPIO.output(pps[1],1)
                sleep(1)
        elif v1 == 0:
            def Pmp1():
                b=1
        if v2 != 0:
            def Pmp2():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[2],GPIO.OUT)
                GPIO.output(pps[2],0)
                print("Pump2_ON")
                sleep(v2/flow[2]+tc[2])
                print("Pump2_OFF")
                GPIO.output(pps[2],1)
                sleep(1)
            def Pmp2TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[2],GPIO.OUT)
                GPIO.output(pps[2],1)
                sleep(v1/flow[1])
                GPIO.output(pps[2],0)
                sleep(v2/flow[2]+tc[2])
                GPIO.output(pps[2],1)
                sleep(1)
        elif v2 == 0:
            def Pmp2():
                c=1
            def Pmp2TD():
                cd=1
        if v3 != 0:
            def Pmp3():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[3],GPIO.OUT)
                GPIO.output(pps[3],0)
                print("Pump3_ON")
                sleep(v3/flow[3]+tc[3])
                print("Pump3_OFF")
                GPIO.output(pps[3],1)
                sleep(1)
            def Pmp3TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[3],GPIO.OUT)
                GPIO.output(pps[3],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0]))
                GPIO.output(pps[3],0)
                sleep(v3/flow[3]+tc[3])
                GPIO.output(pps[3],1)
                sleep(1)
        elif v3 == 0:
            def Pmp3():
                d=1
            def Pmp3TD():
                sd=1
        if v4 != 0:
            def Pmp4():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[4],GPIO.OUT)
                GPIO.output(pps[4],0)
                print("Pump4_ON")
                sleep(v4/flow[4]+tc[4])
                print("Pump4_OFF")
                GPIO.output(pps[4],1)
                sleep(1)
            def Pmp4TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[4],GPIO.OUT)
                GPIO.output(pps[4],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3]))
                GPIO.output(pps[4],0)
                sleep(v4/flow[4]+tc[4])
                GPIO.output(pps[4],1)
                sleep(1)
        elif v4 == 0:
            def Pmp4():
                e=1
            def Pmp4TD():
                es=1
        if v5 != 0:
            def Pmp5():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[5],GPIO.OUT)
                GPIO.output(pps[5],0)
                print("Pump5_ON")
                sleep(v5/flow[5]+tc[5])
                print("Pump5_OFF")
                GPIO.output(pps[5],1)
                sleep(1)
            def Pmp5TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[5],GPIO.OUT)
                GPIO.output(pps[5],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4]))
                GPIO.output(pps[5],0)
                sleep(v5/flow[5]+tc[5])
                GPIO.output(pps[5],1)
                sleep(1)
        elif v5 == 0:
            def Pmp5():
                f=1
            def Pmp5TD():
                fd=1
        if v6 != 0:
            def Pmp6():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[6],GPIO.OUT)
                GPIO.output(pps[6],0)
                print("Pump6_ON")
                sleep(v6/flow[6]+tc[6])
                print("Pump6_OFF")
                GPIO.output(pps[6],1)
                sleep(1)
            def Pmp6TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[6],GPIO.OUT)
                GPIO.output(pps[6],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5]))
                GPIO.output(pps[6],0)
                sleep(v6/flow[6]+tc[6])
                GPIO.output(pps[6],1)
                sleep(1)
        elif v6 == 0:
            def Pmp6():
                g=1
            def Pmp6TD():
                gs=1
        if v7 != 0:
            def Pmp7():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[7],GPIO.OUT)
                GPIO.output(pps[7],0)
                print("Pump7_ON")
                sleep(v7/flow[7]+tc[7])
                print("Pump7_OFF")
                GPIO.output(pps[7],1)
                sleep(1)
            def Pmp7TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[7],GPIO.OUT)
                GPIO.output(pps[7],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6]))
                GPIO.output(pps[7],0)
                sleep(v7/flow[7]+tc[7])
                GPIO.output(pps[7],1)
                sleep(1)
        elif v7 == 0:
            def Pmp7():
                h=1
            def Pmp7TD():
                hs=1
        if v8 != 0:
            def Pmp8():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[8],GPIO.OUT)
                GPIO.output(pps[8],0)
                print("Pump8_ON")
                sleep(v8/flow[8]+tc[8])
                print("Pump8_OFF")
                GPIO.output(pps[8],1)
                sleep(1)
            def Pmp8TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[8],GPIO.OUT)
                GPIO.output(pps[8],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7]))
                GPIO.output(pps[8],0)
                sleep(v8/flow[8]+tc[8])
                GPIO.output(pps[8],1)
                sleep(1)
        elif v8 == 0:
            def Pmp8():
                j=1
            def Pmp8TD():
                js=1
        if v9 != 0:
            def Pmp9():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[9],GPIO.OUT)
                GPIO.output(pps[9],0)
                print("Pump9_ON")
                sleep(v9/flow[9]+tc[9])
                print("Pump9_OFF")
                GPIO.output(pps[9],1)
                sleep(1)
            def Pmp9TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[9],GPIO.OUT)
                GPIO.output(pps[9],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8]))
                GPIO.output(pps[9],0)
                sleep(v9/flow[9]+tc[9])
                GPIO.output(pps[9],1)
                sleep(1)
        elif v9 == 0:
            def Pmp9():
                k=1
            def Pmp9TD():
                ks=1
        hilo_ms=threading.Thread(target=stir)
        hilo_ms1=threading.Thread(target=stir1)
        hilo_ms2=threading.Thread(target=stir2)
        hilo_ms3=threading.Thread(target=stir3)
        hilo_s=threading.Thread(target=Pmps)
        hilo_1=threading.Thread(target=Pmp1)
        hilo_2=threading.Thread(target=Pmp2)
        hilo_3=threading.Thread(target=Pmp3)
        hilo_4=threading.Thread(target=Pmp4)
        hilo_5=threading.Thread(target=Pmp5)
        hilo_6=threading.Thread(target=Pmp6)
        hilo_7=threading.Thread(target=Pmp7)
        hilo_8=threading.Thread(target=Pmp8)
        hilo_9=threading.Thread(target=Pmp9)
        h_2=threading.Thread(target=Pmp2TD)
        h_3=threading.Thread(target=Pmp3TD)
        h_4=threading.Thread(target=Pmp4TD)
        h_5=threading.Thread(target=Pmp5TD)
        h_6=threading.Thread(target=Pmp6TD)
        h_7=threading.Thread(target=Pmp7TD)
        h_8=threading.Thread(target=Pmp8TD)
        h_9=threading.Thread(target=Pmp9TD)
        
        r1 = addt.get()
        u1 = sttr.get()
        if addt.get() == 1:
            hilo_s.start()
            hilo_ms1.start()
            hilo_1.start()
            hilo_2.start()
            hilo_3.start()
            hilo_4.start()
            hilo_5.start()
            hilo_6.start()
            hilo_7.start()
            hilo_8.start()
            hilo_9.start()

            hilo_s.join()
            hilo_ms1.join()
            hilo_1.join()
            hilo_2.join()
            hilo_3.join()
            hilo_4.join()
            hilo_5.join()
            hilo_6.join()
            hilo_7.join()
            hilo_8.join()
            hilo_9.join()
            
            messagebox.showinfo(message="Reaction finished")
            srtButton.config(state="active")
        if addt.get() == 2:
            if sttr.get() == 1:
                hilo_1.start()
                h_2.start()
                hilo_ms1.start()
                h_3.start()
                h_4.start()
                h_5.start()
                h_6.start()
                h_7.start()
                h_8.start()
                h_9.start()

                hilo_1.join()
                h_2.join()
                hilo_ms1.join()
                h_3.join()
                h_4.join()
                h_5.join()
                h_6.join()
                h_7.join()
                h_8.join()
                h_9.join()
                messagebox.showinfo(message="Reaction finished")
                srtButton.config(state="active")
            elif sttr.get() == 2:
                Pmp1()
                hilo_ms2.start()
                h_2.start()
                h_3.start()
                h_4.start()
                h_5.start()
                h_6.start()
                h_7.start()
                h_8.start()
                h_9.start()

                hilo_ms2.join()
                h_2.join()
                h_3.join()
                h_4.join()
                h_5.join()
                h_6.join()
                h_7.join()
                h_8.join()
                h_9.join()
                messagebox.showinfo(message="Reaction finished")
                srtButton.config(state="active")
            elif sttr.get() == 3:
                Pmp1()
                Pmp2()
                hilo_ms3.start()
                h_3.start()
                h_4.start()
                h_5.start()
                h_6.start()
                h_7.start()
                h_8.start()
                h_9.start()

                hilo_ms3.join()
                h_3.join()
                h_4.join()
                h_5.join()
                h_6.join()
                h_7.join()
                h_8.join()
                h_9.join()
                messagebox.showinfo(message="Reaction finished")
                srtButton.config(state="active")
            elif sttr.get() == 0:
                Pmp1()
                Pmp2()
                Pmp3()
                Pmp4()
                Pmp5()
                Pmp6()
                Pmp7()
                Pmp8()
                Pmp9()
                messagebox.showinfo(message="Reaction finished")
                srtButton.config(state="active")
            else:
                messagebox.showerror("","Select the stage for starting stirring")
                return
        if addt.get() == 0:
            messagebox.showerror("","Select the addition")
            srtButton.config(state="active")
    cfm = messagebox.askokcancel("Confirmation","Do you want to start the reaction ?")
    if cfm:
        wmk()
def rxnN():
    mroot.destroy()
    flow=[28,0.265,0.2345,0.21,0.2642,0.22,0.22,0.22,0.22,0.22]
    
    def wmk2():
        if tmstr != 0:
            def stir1():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(tmstr*60+(v1/flow[1])+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(tmstr*60+(v1/flow[1])+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir2():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(tmstr*60+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir3():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(tmstr*60+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
        elif tmstr == 0:
            def stir():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(30+(v1/flow[1])+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir1():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(30+(v1/flow[1])+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir2():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(30+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
            def stir3():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(strpins[0],GPIO.OUT)
                GPIO.setup(strpins[1],GPIO.OUT)
                pw_s = GPIO.PWM(strpins[1],500)
                pw_s.start(0)
                GPIO.output(strpins[1],0)
                pw_s.ChangeDutyCycle(65)
                sleep(30+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
                GPIO.output(strpins[1],1)
                sleep(1)
        else:
            def stir():
                d=1
            def stir1():
                xd=1
            def stir2():
                fd=1
            def stir3():
                sd=1
        if vs != 0: 
            def Pmps():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[0],GPIO.OUT)
                GPIO.output(pps[0],0)
                print("PumpService_ON")
                sleep(vs/flow[0])
                print("PumpService_OFF")
                GPIO.output(pps[0],1)
                sleep(1)
            def PmpsTD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[0],GPIO.OUT)
                GPIO.output(pps[0],1)
                sleep((v2/flow[2])+(v1/flow[1]))
                GPIO.output(pps[0],0)
                sleep(vs/flow[0])
                GPIO.output(pps[0],1)
                sleep(1)
        elif vs == 0:
            def Pmps():
                a=1
            def PmpsTD():
                af=1
        if v1 != 0:
            def Pmp1():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[1],GPIO.OUT)
                GPIO.output(pps[1],0)
                print("Pump1_ON")
                sleep(v1/flow[1])
                print("Pump1_OFF")
                GPIO.output(pps[1],1)
                sleep(1)
        elif v1 == 0:
            def Pmp1():
                b=1
        if v2 != 0:
            def Pmp2():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[2],GPIO.OUT)
                GPIO.output(pps[2],0)
                print("Pump2_ON")
                sleep(v2/flow[2])
                print("Pump2_OFF")
                GPIO.output(pps[2],1)
                sleep(1)
            def Pmp2TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[2],GPIO.OUT)
                GPIO.output(pps[2],1)
                sleep(0)
                GPIO.output(pps[2],0)
                sleep(v2/flow[2])
                GPIO.output(pps[2],1)
                sleep(1)
        elif v2 == 0:
            def Pmp2():
                c=1
            def Pmp2TD():
                cs=1
        if v3 != 0:
            def Pmp3():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[3],GPIO.OUT)
                GPIO.output(pps[3],0)
                print("Pump3_ON")
                sleep(v3/flow[3])
                print("Pump3_OFF")
                GPIO.output(pps[3],1)
                sleep(1)
            def Pmp3TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[3],GPIO.OUT)
                GPIO.output(pps[3],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0]))
                GPIO.output(pps[3],0)
                sleep(v3/flow[3])
                GPIO.output(pps[3],1)
                sleep(1)
        elif v3 == 0:
            def Pmp3():
                d=1
            def Pmp3TD():
                gd=1
        if v4 != 0:
            def Pmp4():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[4],GPIO.OUT)
                GPIO.output(pps[4],0)
                print("Pump4_ON")
                sleep(v4/flow[4])
                print("Pump4_OFF")
                GPIO.output(pps[4],1)
                sleep(1)
            def Pmp4TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[4],GPIO.OUT)
                GPIO.output(pps[4],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3]))
                GPIO.output(pps[4],0)
                sleep(v4/flow[4])
                GPIO.output(pps[4],1)
                sleep(1)
        elif v4 == 0:
            def Pmp4():
                e=1
            def Pmp4TD():
                et=1
        if v5 != 0:
            def Pmp5():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[5],GPIO.OUT)
                GPIO.output(pps[5],0)
                print("Pump5_ON")
                sleep(v5/flow[5])
                print("Pump5_OFF")
                GPIO.output(pps[5],1)
                sleep(1)
            def Pmp5TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[5],GPIO.OUT)
                GPIO.output(pps[5],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4]))
                GPIO.output(pps[5],0)
                sleep(v5/flow[5])
                GPIO.output(pps[5],1)
                sleep(1)
        elif v5 == 0:
            def Pmp5():
                f=1
            def Pmp5TD():
                df=1
        if v6 != 0:
            def Pmp6():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[6],GPIO.OUT)
                GPIO.output(pps[6],0)
                print("Pump6_ON")
                sleep(v6/flow[6])
                print("Pump6_OFF")
                GPIO.output(pps[6],1)
                sleep(1)
            def Pmp6TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[6],GPIO.OUT)
                GPIO.output(pps[6],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5]))
                GPIO.output(pps[6],0)
                sleep(v6/flow[6])
                GPIO.output(pps[6],1)
                sleep(1)
        elif v6 == 0:
            def Pmp6():
                g=1
            def Pmp6TD():
                dg=1
        if v7 != 0:
            def Pmp7():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[7],GPIO.OUT)
                GPIO.output(pps[7],0)
                print("Pump7_ON")
                sleep(v7/flow[7])
                print("Pump7_OFF")
                GPIO.output(pps[7],1)
                sleep(1)
            def Pmp7TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[7],GPIO.OUT)
                GPIO.output(pps[7],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6]))
                GPIO.output(pps[7],0)
                sleep(v7/flow[7])
                GPIO.output(pps[7],1)
                sleep(1)
        elif v7 == 0:
            def Pmp7():
                h=1
            def Pmp7TD():
                sh=1
        if v8 != 0:
            def Pmp8():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[8],GPIO.OUT)
                GPIO.output(pps[8],0)
                print("Pump8_ON")
                sleep(v8/flow[8])
                print("Pump8_OFF")
                GPIO.output(pps[8],1)
                sleep(1)
            def Pmp8TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[8],GPIO.OUT)
                GPIO.output(pps[8],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7]))
                GPIO.output(pps[8],0)
                sleep(v8/flow[8])
                GPIO.output(pps[8],1)
                sleep(1)
        elif v8 == 0:
            def Pmp8():
                j=1
            def Pmp8TD():
                fj=1
        if v9 != 0:
            def Pmp9():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[9],GPIO.OUT)
                GPIO.output(pps[9],0)
                print("Pump9_ON")
                sleep(v9/flow[9])
                print("Pump9_OFF")
                GPIO.output(pps[9],1)
                sleep(1)
            def Pmp9TD():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pps[9],GPIO.OUT)
                GPIO.output(pps[9],1)
                sleep((v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8]))
                GPIO.output(pps[9],0)
                sleep(v9/flow[9])
                GPIO.output(pps[9],1)
                sleep(1)
        elif v9 == 0:
            def Pmp9():
                k=1
            def Pmp9TD():
                ks=1
        hilo_ms=threading.Thread(target=stir)
        hilo_ms1=threading.Thread(target=stir1)
        hilo_ms2=threading.Thread(target=stir2)
        hilo_ms3=threading.Thread(target=stir3)
        hilo_s=threading.Thread(target=Pmps)
        hilo_1=threading.Thread(target=Pmp1)
        hilo_2=threading.Thread(target=Pmp2)
        hilo_3=threading.Thread(target=Pmp3)
        hilo_4=threading.Thread(target=Pmp4)
        hilo_5=threading.Thread(target=Pmp5)
        hilo_6=threading.Thread(target=Pmp6)
        hilo_7=threading.Thread(target=Pmp7)
        hilo_8=threading.Thread(target=Pmp8)
        hilo_9=threading.Thread(target=Pmp9)
        h_2=threading.Thread(target=Pmp2TD)
        h_3=threading.Thread(target=Pmp3TD)
        h_4=threading.Thread(target=Pmp4TD)
        h_5=threading.Thread(target=Pmp5TD)
        h_6=threading.Thread(target=Pmp6TD)
        h_7=threading.Thread(target=Pmp7TD)
        h_8=threading.Thread(target=Pmp8TD)
        h_9=threading.Thread(target=Pmp9TD)
        r1 = addt.get()
        if addt.get() == 1:
            hilo_ms.start()
            hilo_s.start()
            hilo_1.start()
            hilo_2.start()
            hilo_3.start()
            hilo_4.start()
            hilo_5.start()
            hilo_6.start()
            hilo_7.start()
            hilo_8.start()
            hilo_9.start()


            hilo_s.join()
            hilo_ms.join()
            hilo_1.join()
            hilo_2.join()
            hilo_3.join()
            hilo_4.join()
            hilo_5.join()
            hilo_6.join()
            hilo_7.join()
            hilo_8.join()
            hilo_9.join()
            
            messagebox.showinfo(message="Reaction finished")
            srtButton.config(state="active")
        if addt.get() == 2:
            if sttr.get() == 1:
                hilo_1.start()
                h_2.start()
                hilo_ms1.start()
                h_3.start()
                h_4.start()
                h_5.start()
                h_6.start()
                h_7.start()
                h_8.start()
                h_9.start()

                hilo_1.join()
                h_2.join()
                hilo_ms1.join()
                h_3.join()
                h_4.join()
                h_5.join()
                h_6.join()
                h_7.join()
                h_8.join()
                h_9.join()
                messagebox.showinfo(message="Reaction finished")
                srtButton.config(state="active")
            elif sttr.get() == 2:
                Pmp1()
                hilo_ms2.start()
                h_2.start()
                h_3.start()
                h_4.start()
                h_5.start()
                h_6.start()
                h_7.start()
                h_8.start()
                h_9.start()

                hilo_ms2.join()
                h_2.join()
                h_3.join()
                h_4.join()
                h_5.join()
                h_6.join()
                h_7.join()
                h_8.join()
                h_9.join()
                messagebox.showinfo(message="Reaction finished")
                srtButton.config(state="active")
            elif sttr.get() == 3:
                Pmp1()
                Pmp2()
                hilo_ms3.start()
                h_3.start()
                h_4.start()
                h_5.start()
                h_6.start()
                h_7.start()
                h_8.start()
                h_9.start()

                hilo_ms3.join()
                h_3.join()
                h_4.join()
                h_5.join()
                h_6.join()
                h_7.join()
                h_8.join()
                h_9.join()
                messagebox.showinfo(message="Reaction finished")
                srtButton.config(state="active")
            elif sttr.get() == 0:
                Pmp1()
                Pmp2()
                Pmp3()
                Pmp4()
                Pmp5()
                Pmp6()
                Pmp7()
                Pmp8()
                Pmp9()
                messagebox.showinfo(message="Reaction finished")
                srtButton.config(state="active")
            else:
                messagebox.showerror("","Select the stage for starting stirring")
                return
        if addt.get() == 0:
            messagebox.showerror("","Select the addition form")
            srtButton.config(state="active")
    cnf = messagebox.askokcancel("Confirmation","Do you want to start the reaction ?")
    if cnf:
        wmk2()
def clr_text():
    volents.delete(0,END)
    volents.insert(0,0)
    volent1.delete(0,END)
    volent1.insert(0,0)
    volent2.delete(0,END)
    volent2.insert(0,0)
    volent3.delete(0,END)
    volent3.insert(0,0)
    volent4.delete(0,END)
    volent4.insert(0,0)
    volent5.delete(0,END)
    volent5.insert(0,0)
    volent6.delete(0,END)
    volent6.insert(0,0)
    volent7.delete(0,END)
    volent7.insert(0,0)
    volent8.delete(0,END)
    volent8.insert(0,0)
    volent9.delete(0,END)
    volent9.insert(0,0)
    addt.set(None)
    velentstr.delete(0,END)
    velentstr.insert(0,0)
    sttr.set(0)
    srtButton.config(state="active")

startFont = font.Font(family='Arial Black',size=9)
srtButton = Button(root,text="START",height=3,width=24,command=chyorn,bg='#708090')
srtButton.place(x=850,y=580)
clnButton = Button(root,command=clr_text,text="RESET",height=2,width=10)
clnButton.place(x=100,y=590)

ventana.pack()
mainloop() 

