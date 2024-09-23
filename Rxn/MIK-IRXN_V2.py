from tkinter import *
from tkinter import messagebox, ttk
import tkinter.font as font
#import RPi.GPIO as GPIO
import time
from time import sleep
import threading

pps = [13,24,22,27,17,23,18,12,4,7] #Cambiar el numero de pines que corresponde al circuito!!!
strpins = [12, 20] 

root = Tk()
root.title('MIK-I')
ventana = Canvas(root, bg="white", height=660, width=1100)
init_var = ["var_s","var_1","var_2","var_3","var_4","var_5","var_6","var_7","var_8","var_9","addt","sttr","strtm"]
var_int = []
for var in init_var:
    var = IntVar()
    var_int.append(var)

ordrLabel = Label(text="Addition",bg="white",font=("Arial Nova",13))
ordrLabel.place(x=290,y=585)
radio1 = Radiobutton(ventana, text="Parallel", variable=var_int[10],bg="white",value=1)
radio1.place(x=240,y=615)
radio2 = Radiobutton(ventana, text="In-Order", variable=var_int[10],bg="white", value=2)
radio2.place(x=340,y=615)
strLabel = Label(text="Stirring",bg="white",font=("Arial Nova",13))
strLabel.place(x=600,y=585)
stgstr = Label(text="Stage",bg="white",font=("Arial Nova",10))
stgstr.place(x=475,y=615)
tmstr = Label(text="Time (min)",bg="white",font=("Arial Nova",10))
tmstr.place(x=685,y=615)

chkstr = Checkbutton(ventana, text="No  ",variable=var_int[11],onvalue=0,offvalue=0, height=1,width=2, bg= "white")
chkstr.place(x=520,y=615)
chkstr = Checkbutton(ventana, text="1",variable=var_int[11],onvalue=1,offvalue=0, height=1,width=2, bg= "white")
chkstr.place(x=560,y=615)
chkstr = Checkbutton(ventana, text="2",variable=var_int[11],onvalue=2,offvalue=0, height=1,width=2, bg= "white")
chkstr.place(x=600,y=615)
chkstr = Checkbutton(ventana, text="3",variable=var_int[11],onvalue=3,offvalue=0, height=1,width=2, bg= "white")
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
volents = Entry(ventana,  width=8, textvariable=var_int[0])
volents.place(x=90,y=248)
volent1 = Entry(ventana,  width=8, textvariable=var_int[1])
volent1.place(x=290,y=248)
volent2=Entry(ventana,  width=8, textvariable=var_int[2])
volent2.place(x=490,y=248)
volent3 = Entry(ventana,  width=8, textvariable=var_int[3])
volent3.place(x=690,y=248) 
volent4 = Entry(ventana,  width=8, textvariable=var_int[4])
volent4.place(x=890,y=248)

for p in range(4):
    global pumpi
    pumpi = ventana.create_oval(250+200*p,60,400+200*p,210,fill="green",outline="black")
    pumpi_lbl = Label(text="Pump "+str(p+1),bg='white',font=("Arial Nova",13))
    pumpi_lbl.place(x=300+200*p,y=25)
    ci = ventana.create_oval(320+200*p,130,330+200*p,140,fill="silver", outline="")

volent5 = Entry(ventana,  width=8, textvariable=var_int[5])
volent5.place(x=150,y=548)
volent6 = Entry(ventana,  width=8, textvariable=var_int[6])
volent6.place(x=350,y=548)
volent7 = Entry(ventana,  width=8, textvariable=var_int[7])
volent7.place(x=550,y=548)
volent8 = Entry(ventana,  width=8, textvariable=var_int[8])
volent8.place(x=750,y=548)
volent9 = Entry(ventana,  width=8, textvariable=var_int[9])
volent9.place(x=950,y=548)
velentstr = Entry(ventana, width=7, textvariable=var_int[12])
velentstr.place(x=765,y=613)

for q in range(5):
    global pmpi 
    pmpi = ventana.create_oval(110+200*q,350,260+200*q,500,fill="green",outline="black")
    pmpi_lbl = Label(text="Pump "+str(q+5),bg="white",font=("Arial Nova",13))
    pmpi_lbl.place(x=160+200*q,y=320)
    cii = ventana.create_oval(180+200*q,420,190+200*q,430,fill="silver", outline="")

def process_input(entry, var_name):
    value = entry.get()
    if value.isdigit():
        globals()[var_name] = sum(float(digit) * 10 ** i for i, digit in enumerate(value[::-1]))
    else:
        messagebox.showerror("Error", "Only numbers !!")
        return False
    return True

def chyorn():
    global mroot, vs, v1, v2, v3, v4, v5, v6, v7, v8, v9, tmstr
    
    if not process_input(volents, 'vs'): return
    if not process_input(volent1, 'v1'): return
    if not process_input(volent2, 'v2'): return
    if not process_input(volent3, 'v3'): return
    if not process_input(volent4, 'v4'): return
    if not process_input(volent5, 'v5'): return
    if not process_input(volent6, 'v6'): return
    if not process_input(volent7, 'v7'): return
    if not process_input(volent8, 'v8'): return
    if not process_input(volent9, 'v9'): return
    if not process_input(velentstr, 'tmstr'): return

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
    def workingPumpWtc(number_pump,volume):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pps[number_pump],GPIO.OUT)
        GPIO.output(pps[number_pump],0)
        print("Pump",number_pump,"ON")
        sleep(volume/flow[number_pump]+tc[number_pump])
        print("Pump",number_pump,"OFF")
        GPIO.output(pps[number_pump],1)
        sleep(1)
    def pumpWorkWPause(number_pump,waiting_time,working_time_w_tc):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pps[number_pump],GPIO.OUT)
        GPIO.output(pps[number_pump],1)
        sleep(waiting_time)
        GPIO.output(pps[number_pump],0)
        sleep(working_time_w_tc)
        GPIO.output(pps[number_pump],1)
        sleep(1)
    def stiringTms(timeForReaction):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(strpins[0],GPIO.OUT)
        GPIO.setup(strpins[1],GPIO.OUT)
        pw_s = GPIO.PWM(strpins[1],500)
        pw_s.start(0)
        GPIO.output(strpins[1],0)
        pw_s.ChangeDutyCycle(65)
        sleep(timeForReaction)
        GPIO.output(strpins[1],1)
        sleep(1)
    def bye():
        messagebox.showinfo(message="Reaction finished")
        srtButton.config(state="active")

    def wmk():
        if tmstr != 0:
            def stir1():
                stiringTms(tmstr*60+(v1/flow[1]+tc[1])+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
            def stir():
                stiringTms(tmstr*60+(v1/flow[1]+tc[1])+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
            def stir2():
                stiringTms((tmstr*60)+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
            def stir3():
                stiringTms(tmstr*60+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
        elif tmstr == 0:
            def stir():
                stiringTms(30+(v1/flow[1]+tc[1])+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
            def stir1():
                stiringTms(30+(v1/flow[1]+tc[1])+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
            def stir2():
                stiringTms(30+(v2/flow[2]+tc[2])+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
            def stir3():
                stiringTms(30+(v3/flow[3]+tc[3])+(v4/flow[4]+tc[4])+(v5/flow[5]+tc[5])+(v6/flow[6]+tc[6])+(v7/flow[7]+tc[7])+(v8/flow[8]+tc[8])+(v9/flow[9]+tc[9]))
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
                workingPumpWtc(0,vs)
            def PmpsTD():
                pumpWorkWPause(0,(v2/flow[2])+(v1/flow[1]),vs/flow[0]+tc[0])
        elif vs == 0:
            def Pmps():
                a=1
            def PmpsTD():
                ax=1
        if v1 != 0:
            def Pmp1():
                workingPumpWtc(1,v1)
        elif v1 == 0:
            def Pmp1():
                b=1
        if v2 != 0:
            def Pmp2():
                workingPumpWtc(2,v2)
            def Pmp2TD():
                pumpWorkWPause(2,v1/flow[1],v2/flow[2]+tc[2])
        elif v2 == 0:
            def Pmp2():
                c=1
            def Pmp2TD():
                cd=1
        if v3 != 0:
            def Pmp3():
                workingPumpWtc(3,v3)
            def Pmp3TD():
                pumpWorkWPause(3,(v1/flow[1])+(v2/flow[2])+(vs/flow[0]),v3/flow[3]+tc[3])
        elif v3 == 0:
            def Pmp3():
                d=1
            def Pmp3TD():
                sd=1
        if v4 != 0:
            def Pmp4():
                workingPumpWtc(4,v4)
            def Pmp4TD():
                pumpWorkWPause(4,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3]),v4/flow[4]+tc[4])
        elif v4 == 0:
            def Pmp4():
                e=1
            def Pmp4TD():
                es=1
        if v5 != 0:
            def Pmp5():
                workingPumpWtc(5,v5)
            def Pmp5TD():
                pumpWorkWPause(5,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4]),v5/flow[5]+tc[5])
        elif v5 == 0:
            def Pmp5():
                f=1
            def Pmp5TD():
                fd=1
        if v6 != 0:
            def Pmp6():
                workingPumpWtc(6,v6)
            def Pmp6TD():
                pumpWorkWPause(6,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5]),
                               v6/flow[6]+tc[6])
        elif v6 == 0:
            def Pmp6():
                g=1
            def Pmp6TD():
                gs=1
        if v7 != 0:
            def Pmp7():
                workingPumpWtc(7,v7)
            def Pmp7TD():
                pumpWorkWPause(7,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6]),
                               v7/flow[7]+tc[7])
        elif v7 == 0:
            def Pmp7():
                h=1
            def Pmp7TD():
                hs=1
        if v8 != 0:
            def Pmp8():
                workingPumpWtc(8,v8)
            def Pmp8TD():
                pumpWorkWPause(8,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7]),
                               v8/flow[8]+tc[8])
        elif v8 == 0:
            def Pmp8():
                j=1
            def Pmp8TD():
                js=1
        if v9 != 0:
            def Pmp9():
                workingPumpWtc(9,v9)
            def Pmp9TD():
                pumpWorkWPause(9,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8]),
                               v9/flow[9]+tc[9])
        elif v9 == 0:
            def Pmp9():
                k=1
            def Pmp9TD():
                ks=1
        hilos = ["hilo_ms","hilo_ms1","hilo_ms2","hilo_ms3","hilo_s","hilo_1","hilo_2",
                 "hilo_3","hilo_4","hilo_5","hilo_6","hilo_7","hilo_8","hilo_9"]
        funcs = [stir,stir1,stir2,stir3,Pmps,Pmp1,Pmp2,Pmp3,Pmp4,Pmp5,Pmp6,Pmp7,Pmp8,Pmp9]
        hilos_N = []
        for hilo in hilos:
            hilo = threading.Thread(target=funcs[hilos.index(hilo)])
            hilos_N.append(hilo)
        hs = ["h_2","h_3","h_4","h_5","h_6","h_7","h_8","h_9"]
        fnct = [Pmp2TD,Pmp3TD,Pmp4TD,Pmp5TD,Pmp6TD,Pmp7TD,Pmp8TD,Pmp9TD]
        h_N = []
        for h in hs:
            h = threading.Thread(target=fnct[hs.index(h)])
            h_N.append(h)
        if var_int[10].get() == 1:
            hilos_N[1].start()
            hilos_N[1].join()
            for i in range(4,14):
                hilos_N[i].start()
                hilos_N[i].join()
            bye()
        if var_int[10].get() == 2:
            if var_int[11].get() == 1:
                hilos_N[1].start()
                hilos_N[1].join()
                hilos_N[4].start()
                hilos_N[4].join()
                for h in h_N:
                    h.start()
                    h.join()
                bye()
            elif var_int[11].get() == 2:
                Pmp1()
                hilos_N[2].start()
                hilos_N[2].join()
                for h in h_N:
                    h.start()
                    h.join()
                bye()
            elif var_int[11].get() == 3:
                Pmp1()
                Pmp2()
                hilos_N[3].start()
                hilos_N[3].join()
                for i in range(1,8):
                    h_N[i].start()
                    h_N[i].join()
                bye()
            elif var_int[11].get() == 0:
                pps_list = ["Pmp1","Pmp2","Pmp3","Pmp4","Pmp5","Pmp6","Pmp7","Pmp8","Pmp9"]
                for pump in pps_list:
                    pump()
                bye()
            else:
                messagebox.showerror("","Select the stage for starting stirring")
                return
        if var_int[10].get() == 0:
            bye()
    cfm = messagebox.askokcancel("Confirmation","Do you want to start the reaction ?")
    if cfm:
        wmk()

def rxnN():
    mroot.destroy()
    flow = [28,0.265,0.2345,0.21,0.2642,0.22,0.22,0.22,0.22,0.22]
    def workingPump(number_pump,volume):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pps[number_pump],GPIO.OUT)
        GPIO.output(pps[number_pump],0)
        print("Pump",number_pump,"ON")
        sleep(volume/flow[number_pump])
        print("Pump",number_pump,"OFF")
        GPIO.output(pps[number_pump],1)
        sleep(1)
    def pumpWorkWPause(number_pump,waiting_time,working_time):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pps[number_pump],GPIO.OUT)
        GPIO.output(pps[number_pump],1)
        sleep(waiting_time)
        GPIO.output(pps[number_pump],0)
        sleep(working_time)
        GPIO.output(pps[number_pump],1)
        sleep(1)
    def stiringTms(timeForReaction):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(strpins[0],GPIO.OUT)
        GPIO.setup(strpins[1],GPIO.OUT)
        pw_s = GPIO.PWM(strpins[1],500)
        pw_s.start(0)
        GPIO.output(strpins[1],0)
        pw_s.ChangeDutyCycle(65)
        sleep(timeForReaction)
        GPIO.output(strpins[1],1)
        sleep(1)
    def bye():
        messagebox.showinfo(message="Reaction finished")
        srtButton.config(state="active")

    def wmk2():
        if tmstr != 0:
            def stir():
                stiringTms(tmstr*60+(v1/flow[1])+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
            def stir1():
                stiringTms(tmstr*60+(v1/flow[1])+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
            def stir2():
                stiringTms(tmstr*60+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
            def stir3():
                stiringTms(tmstr*60+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
        elif tmstr == 0:
            def stir():
                stiringTms(30+(v1/flow[1])+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
            def stir1():
                stiringTms(30+(v1/flow[1])+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
            def stir2():
                stiringTms(30+(v2/flow[2])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
            def stir3():
                stiringTms(30+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8])+(v9/flow[9]))
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
                workingPump(0,vs)
            def PmpsTD():
                pumpWorkWPause(0,(v2/flow[2])+(v1/flow[1]),vs/flow[0])
        elif vs == 0:
            def Pmps():
                a=1
            def PmpsTD():
                af=1
        if v1 != 0:
            def Pmp1():
                workingPump(1,v1)
        elif v1 == 0:
            def Pmp1():
                b=1
        if v2 != 0:
            def Pmp2():
                workingPump(2,v2)
            def Pmp2TD():
                pumpWorkWPause(2,0,v2/flow[2])
        elif v2 == 0:
            def Pmp2():
                c=1
            def Pmp2TD():
                cs=1
        if v3 != 0:
            def Pmp3():
                workingPump(3,v3)
            def Pmp3TD():
                pumpWorkWPause(3,(v1/flow[1])+(v2/flow[2])+(vs/flow[0]),v3/flow[3])
        elif v3 == 0:
            def Pmp3():
                d=1
            def Pmp3TD():
                gd=1
        if v4 != 0:
            def Pmp4():
                workingPump(4,v4)
            def Pmp4TD():
                pumpWorkWPause(4,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3]),v4/flow[4])
        elif v4 == 0:
            def Pmp4():
                e=1
            def Pmp4TD():
                et=1
        if v5 != 0:
            def Pmp5():
                workingPump(5,v5)
            def Pmp5TD():
                pumpWorkWPause(5,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4]),v5/flow[5])
        elif v5 == 0:
            def Pmp5():
                f=1
            def Pmp5TD():
                df=1
        if v6 != 0:
            def Pmp6():
                workingPump(6,v6)
            def Pmp6TD():
                pumpWorkWPause(6,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5]),v6/flow[6])
        elif v6 == 0:
            def Pmp6():
                g=1
            def Pmp6TD():
                dg=1
        if v7 != 0:
            def Pmp7():
                workingPump(7,v7)
            def Pmp7TD():
                pumpWorkWPause(7,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6]),v7/flow[7])
        elif v7 == 0:
            def Pmp7():
                h=1
            def Pmp7TD():
                sh=1
        if v8 != 0:
            def Pmp8():
                workingPump(8,v8)
            def Pmp8TD():
                pumpWorkWPause(8,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7]),v8/flow[8])
        elif v8 == 0:
            def Pmp8():
                j=1
            def Pmp8TD():
                fj=1
        if v9 != 0:
            def Pmp9():
                workingPump(9,v9)
            def Pmp9TD():
                pumpWorkWPause(9,(v1/flow[1])+(v2/flow[2])+(vs/flow[0])+(v3/flow[3])+(v4/flow[4])+(v5/flow[5])+(v6/flow[6])+(v7/flow[7])+(v8/flow[8]),v9/flow[9])
        elif v9 == 0:
            def Pmp9():
                k=1
            def Pmp9TD():
                ks=1
        hilos = ["hilo_ms","hilo_ms1","hilo_ms2","hilo_ms3","hilo_s","hilo_1","hilo_2",
                 "hilo_3","hilo_4","hilo_5","hilo_6","hilo_7","hilo_8","hilo_9"]
        funcs = [stir,stir1,stir2,stir3,Pmps,Pmp1,Pmp2,Pmp3,Pmp4,Pmp5,Pmp6,Pmp7,Pmp8,Pmp9]
        hilos_N = []
        for hilo in hilos:
            hilo = threading.Thread(target=funcs[hilos.index(hilo)])
            hilos_N.append(hilo)
        hs = ["h_2","h_3","h_4","h_5","h_6","h_7","h_8","h_9"]
        fnct = [Pmp2TD,Pmp3TD,Pmp4TD,Pmp5TD,Pmp6TD,Pmp7TD,Pmp8TD,Pmp9TD]
        h_N = []
        for h in hs:
            h = threading.Thread(target=fnct[hs.index(h)])
            h_N.append(h)
        if var_int[10].get() == 1:
            hilos_N[0].start()
            hilos_N[0].join()
            for i in range(4,14):
                hilos_N[i].start()
                hilos_N[i].join()
            bye()
        if var_int[10].get() == 2:
            if var_int[11].get() == 1:
                hilos_N[5].start()
                hilos_N[1].start()
                hilos_N[5].join()
                hilos_N[1].join()
                for h in h_N:
                    h.start()
                    h.join()
                bye()
            elif var_int[11].get() == 2:
                Pmp1()
                hilos_N[2].start()
                hilos_N[2].join()
                for h in h_N:
                    h.start()
                    h.join()
                bye()
            elif var_int[11].get() == 3:
                Pmp1()
                Pmp2()
                hilos_N[3].start()
                hilos_N[3].join()
                for i in range(1,8):
                    h_N[i].start()
                    h_N[i].join()
                bye()
            elif var_int[11].get() == 0:
                # pps_list = ["Pmp1","Pmp2","Pmp3","Pmp4","Pmp5","Pmp6","Pmp7","Pmp8","Pmp9"]
                # pps_func = []
                # for pump in pps_list:
                #     pps_func.append(pump())
                # for pp in pps_func:
                #     pp
                bye()
            else:
                messagebox.showerror("","Select the stage for starting stirring")
                return
        if var_int[10].get() == 0:
            bye()
    cnf = messagebox.askokcancel("Confirmation","Do you want to start the reaction ?")
    if cnf:
        wmk2()

def clr_text():
    volents_list = [volents, volent1, volent2, volent3, volent4, volent5, volent6, volent7, volent8, volent9]
    
    for vol in volents_list:
        vol.delete(0, END)
        vol.insert(0, 0)
    
    var_int[10].set(None)
    velentstr.delete(0, END)
    velentstr.insert(0, 0)
    var_int[11].set(0)
    srtButton.config(state="active")

startFont = font.Font(family='Arial Black',size=9)
srtButton = Button(root,text="START",height=3,width=24,command=chyorn,bg='#708090')
srtButton.place(x=850,y=580)
clnButton = Button(root,command=clr_text,text="RESET",height=2,width=10)
clnButton.place(x=100,y=590)

ventana.pack()
mainloop() 

