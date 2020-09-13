import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import Menu
import os
import sys
import time


#code for main screen goes here

win=tk.Tk()
win.geometry('660x240+150+150')
win.resizable(False,True)
#win.iconbitmap("C:/Users/User/Desktop/Folders/PYTHON/myicon.ico")

#creating tabs
tabcontrol=ttk.Notebook(win)
tab1=ttk.Frame(tabcontrol)
tab2=ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text="INPUT")
tabcontrol.add(tab2,text="SETTING")
tabcontrol.grid(row=0,column=0)
#ppath=os.path.join(sys.path[0]+'/myicon.ico')

#win.iconbitmap(ppath)
win.title("WiFi Hotspot")
win.configure(background="blue")
label11=ttk.Label(tab1 , text="This Program Help You to start a Access Point(AP) in your system")
label11.grid(row=0 , column=0 , columnspan=3)

#defining wifi hotspot code here
def hotspot():
    f1=open("data.txt","r")
    while True:
        value=f1.readline()
        if value[0:1]=="#":
            apname=value[1:]
        if value[0:1]=="*":
            apkey=value[1:]
        if value=="":
            break    
    f1.close()
    os.system("cmd /c netsh wlan set hostednetwork mode=allow ssid="+apname)
    os.system("cmd /c netsh wlan set hostednetwork mode=allow  key="+apkey)
    os.system("cmd /c netsh wlan start hostednetwork")

#Defining the function for network adapter

#Code for closing hotspot 
def closehot():
    os.system("cmd /c netsh wlan stop hostednetwork")


#now writting the entery point

labl=ttk.Label(tab1,text="Enter Access point name:")
labl.grid(row=1,column=0,pady=2)
name=tk.StringVar()
inp=ttk.Entry(tab1,width=20,textvariable=name)
inp.grid(row=1,column=2,pady=1,padx=1)

#now writting the entry Key for AP

labl=ttk.Label(tab1,text="Enter Password:")
labl.grid(row=2,column=0)
passkey=tk.StringVar()
inpkey=ttk.Entry(tab1,width=20,textvariable=passkey)
inpkey.grid(row=2,column=2,pady=1,padx=1)


#writting the value for entery placeholder if available


#writting file if entry has some value
def writefile():
   
    f1=open("data.txt",'w')
    f1.write("#"+name.get()+"\n"+"*"+passkey.get()+"\n")
    f1.close()





#now writting for button
def runme():
    lastcmd()
    apname=name.get()
    apkey=passkey.get()
    a=0
    if (apname=="" and apkey==""):
        hotspot()
    else:
        if(apname==""):
            msg.showwarning("Error","Hotspot name Error/Null")
            a=1
            
        if(apkey==""):
            msg.showwarning("Error","Hotspot key Error/Null")
            a=1  
        if(len(apkey)<8):
            msg.showwarning("Error","Password should be greater than 8 word")
            a=1  
        if (a==0):
            fs=open("data.txt","w")
            fs.writelines("#"+apname+"\n"+"*"+apkey+"\n")
            fs.close()
            previousvalue()
            hotspot()



btn1=ttk.Button(tab1,text="START Hotspot",width=20,command=runme)
btn1.grid(row=3,column=2,pady=2)

#now writing button for closing
def runme2():
    closehot()
   
    

btn2=ttk.Button(tab1,text="STOP Hotspot",width=20,command=runme2)
btn2.grid(row=4,column=2,pady=10)

#label for showing previous Access point and Password
def accesspoint(a):
    fs=open('data.txt','r')
    while True:
        value=fs.readline()
        if (a==1):
            if value[0:1]=="#":
                return value[1:]
        if (a==2):
            if value[0:1]=="*":
                return value[1:]

        if value=="":
            break
            
    fs.close()        
    return value
        
#function defining the previous value output at tkinter window        
def previousvalue():
    Preap = accesspoint(1)
    prekey = accesspoint(2)
    label22 = tk.Label(tab1,background="black",foreground="pink",text="Previous Access Point and  Key Value:\n"+Preap+"\n"+prekey)
    label22.grid(row=1,column=3)



    label31=tk.Label(tab1,text="Note:Recommended to use Password With atleast 8 word")
    label31.grid(row=5,column=3)
previousvalue()

#now defining the setting part tab2 to be used
def network():
    os.system("cmd /c powertobat.bat")
    networkvalue()
labldriver=ttk.Label(tab2,text="Select Driver with internet:")
labldriver.grid(row=3,column=0)
#Combobox for network card name
netname=tk.StringVar()
cmb1 = ttk.Combobox(tab2 , textvariable=netname , state="readonly")
#readfile for hardware value
def networkvalue():
    f2=open('powerdata.txt','r')
    netvalue=[]
    while True:
        value = f2.readlines()
        if value == []:
            break
        netvalue = netvalue+value
    f2.close()
    cmb1['values']=(tuple(netvalue))
    cmb2['values']=(tuple(netvalue))

cmb1.grid(row=3 , column=1)


btn3 = ttk.Button(tab2,text="Refresh Driver",command=network)
btn3.grid(row=3 , column=2)
#driver to share internet with
lablinternet=ttk.Label(tab2,text="Select Driver you want to share internet with:")
lablinternet.grid(row=4,column=0)
#combobox for sharing internet with
sharename = tk.StringVar()
cmb2 = ttk.Combobox(tab2, textvariable=sharename, state="readonly")
cmb2.grid(row=4, column=1)

def lastcmd():
    progrees()
    os.system('cmd /c start powershell "Set-NetIPInterface -Forwarding Enabled;Set-Service SharedAccess -StartupType Automatic;Start-Service SharedAccess"')


def secondlast():
    revprog()
    os.system('cmd /c start powershell "Set-NetIPInterface -Forwarding Disable;Stop-Service SharedAccess"')

btn4 = ttk.Button(tab2,text="START SHARING",command=lastcmd)
btn4.grid(row=5 , column=1)

btn5 = ttk.Button(tab2,text="STOP SHARING",command=secondlast)
btn5.grid(row=6 , column=1)

def alertme():
    msg.showinfo("About me","My Name is Ghanashyam Dhakal.I am Programming Geek.You can visit my github @:www.github.com/ashish17133 for more Program with my own creation.Design and Develope in Nepal")

menu_bar=Menu(win)
win.configure(menu=menu_bar)
#About menu
help_menu=Menu(menu_bar)
help_menu.add_command(label="About",command=alertme)
menu_bar.add_cascade(label="Help",menu=help_menu)
#adding label and stop sharing button here
labl22=ttk.Label(tab2,text="1.If you want to share internet with all other drive just Click 'Start Sharing'         " )
labl22.grid(row=0,column=0,sticky='W',columnspan=3)
labl23=ttk.Label(tab2,text="2.If you want to share internet with specific drive First select the Drive and Click 'Start Sharing'" )
labl23.grid(row=1,column=0,sticky='W',columnspan=3)
labl24=ttk.Label(tab2,text="3.If you want to stop it Click 'Stop Sharing'" )
labl24.grid(row=2,column=0,sticky='W',columnspan=3)
#tab2 progressbar
progressbar=ttk.Progressbar(tab2,orient="horizontal",length=100,mode='determinate')
progressbar.grid(row=7,column=1)
        #progress bar info label
labl31=ttk.Label(tab2,text="testing")
labl31.grid(row=8,column=1)
labl31.grid_forget()

def progrees():
    progressbar['value']=20
    labl31.grid(row=8, column=1)
    labl31.configure(text="starting port forwarding")
    win.update_idletasks()
    time.sleep(0.5)

    progressbar['value'] = 40
    labl31.grid(row=8, column=1)
    labl31.configure(text="starting port forwarding")
    win.update_idletasks()
    time.sleep(1)


    progressbar['value'] = 60
    labl31.grid(row=8, column=1)
    labl31.configure(text="starting internet sharing service")
    win.update_idletasks()
    time.sleep(0.5)

    progressbar['value'] = 80
    labl31.grid(row=8, column=1)
    labl31.configure(text="Finalizing port forwarding")
    win.update_idletasks()
    time.sleep(0.5)

    progressbar['value'] = 100
    labl31.grid(row=8, column=1)
    labl31.configure(text="Completed")
    win.update_idletasks()
    time.sleep(1)
    labl31.grid_forget()

def revprog():
    progressbar['value'] = 100
    labl31.grid(row=8, column=1)
    labl31.configure(text="stoping port forwarding")
    win.update_idletasks()
    time.sleep(0.5)

    progressbar['value'] = 80
    labl31.grid(row=8, column=1)
    labl31.configure(text="Disabling internet sharing service")
    win.update_idletasks()
    time.sleep(1)

    progressbar['value'] = 60
    labl31.grid(row=8, column=1)
    labl31.configure(text="Completing the disabling process")
    win.update_idletasks()
    time.sleep(0.5)

    progressbar['value'] = 20
    labl31.grid(row=8, column=1)
    labl31.configure(text="Finalizing Stop process")
    win.update_idletasks()
    time.sleep(0.5)

    progressbar['value'] = 0
    labl31.grid(row=8, column=1)
    labl31.configure(text="Completed")
    win.update_idletasks()
    time.sleep(1)
    labl31.grid_forget()


win.mainloop()
