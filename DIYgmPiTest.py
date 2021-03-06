#James Seekamp, Jeffery Xiao, Issa El-Amir, Regina Tuey
#11/16/2018
#DIY Geiger Kit for RPi Zero W


#Library Imports
import RPi.GPIO as GPIO
#import bluetooth
import socket
import time
import math
import os


#Declares pins and disables error message
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(32, GPIO.IN)
GPIO.setup(8, GPIO.OUT) # alarm
GPIO.setup(31, GPIO.OUT) 
GPIO.setup(3, GPIO.OUT) # LED
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)

pwm = GPIO.PWM(12, 1000) #Set the frequency and GPIO pin. Keep pin to 12.
                         #Frequency has limited effect on the voltage. 

tube=input("Enter type of tube:  ")
name=input("Enter label of tube:  ")
levl=int(input("PWM Level: "))

if not os.path.exists(tube):
    os.makedirs(tube)

#os.system("cd /home/pi/Desktop/"+tube+"/")
os.system("git init")
os.system("git remote add origin https://github.com/Ceonei/TubeTesting")
os.system("git ls-files --deleted -z | git update-index --assume-unchanged -z --stdin")
#os.system("git clone https://github.com/Ceonei/TubeTesting")

if not os.path.exists(tube+"/"+name):
    os.makedirs(tube+"/"+name)


pwm.start(levl) #Set duty cycle. Higher the number, higher the voltage

flname=tube+"/"+name+"/"+name+"_Background.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

GPIO.add_event_detect(32,GPIO.RISING)

#Sets alarm to off by default
GPIO.output(8, GPIO.LOW)



def detection():
    cpm = 0
    endtime = time.time() + 1 #Change the number in this line to change time (Seconds)
    while time.time() < endtime:
        if GPIO.event_detected(32):
            cpm = cpm + 1
    return cpm

#fileoption = int(input("Choose One of the Following Options \n 1: Print Data \n 2: Write to File \n"))

#graphical user interface(GUI)
#root = Tk()
#root.title("Geiger Counter")
x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
    #if fileoption == 2:    
        
        #file.write(str(x))
        #file.write("\n")
        #file.write("Counts Per Second: ")
        #file.write(str(detection()))
        #file.write("\n")
        #file.write(str(session.stream))
    

dose = int
#doserate = ttk.Entry(mainframe, width=5, textvariable=dose).grid(column=5, row=5)

file.close()
#for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#root.mainloop()
pwm.stop(12)

os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in Photo Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_Photo.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in LongCat Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_LongCat.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in Long1 Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_Long1.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in Long2 Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_Long2.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in Long3 Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_Long3.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in Long4 Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_Long4.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in LongA Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_LongA.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in Dead1 Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_Dead1.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in Dead12 Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_Dead12.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()
pwm.stop(12)


os.system("omxplayer analog-watch-alarm_daniel-simion.wav")
pss="N"
while pss != "y":
    pss=input("Tube is in Dead2 Test Configuration? (y/n)")

flname=tube+"/"+name+"/"+name+"_Dead2.txt"
#file = open("R55_Dead2.txt", "w+")
file = open(flname, "w+")

pwm.start(levl) 

x=0
tot=1
ave =tot
sig=1
per=1

while tot <= 10000 or per>0.01: #or per>0.01 or x<75:

    x = x+1
    cps=detection()
    tot=tot+cps
    ave=tot/x
    sig=math.sqrt(ave/x)
    per=sig/ave
    print(x)
    print('Counts Per Second: ', str(cps))
    print(str(tot))
    #print()
    file.write(str(cps))
    file.write("\n")
    
file.close()

pwm.stop(12)

os.system("cd /home/pi/Desktop/TubeTesting")
os.system("git add .")
os.system("git commit -m 'test'")
os.system("git push -u origin master")

GPIO.cleanup()
#
    