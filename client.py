# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:01:05 2020

@author: elifaskvav
"""
from tkinter import * 
from ftplib import FTP
import time
from ftplib import error_perm
from tkinter import messagebox


top = Tk() #tkinter.Tk()
ftp = FTP('')
ky=65
kx=0
label222 = Label


def connect():
    
    rtn=ftp.connect(mystring9.get(),int(mystring10.get()))
    messagebox.showinfo( 'connection',rtn)
    
    
def signIn():
    txt=ftp.login(mystring2.get(),mystring3.get())
    label=Label(top, text= txt,fg='red').place(x=0, y=5)



def uploadFile():    
    filename = mystring5.get()
    #ftp.cwd('/home')
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    #ftp.quit()
    #ftp.cwd('/')

def downloadFile():   
    filename = mystring6.get()
    #ftp.cwd('/home') 
    ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
    #ftp.quit()
    #ftp.cwd('/')
    
def subList():
    labelSil()
    all_dirs = get_all_dirs_ftp()
    all_dirs.append('')
    for dir in all_dirs:
        listele(dir)

def labelSil(): 
    global ky
    global kx
    ky=65
    kx=0
    global label222
    files = []
    try:
        files=ftp.nlst('/'+dir)
    except :
        print ("No files in this directory")
        
    for f in files:
        print (f)
        label222 =Label(top, text = "", bg='#856ff8',width=16, height=1)
        label222.place(x=kx, y=ky)
        ky+=25
    kx+=10
def listele(dir):
    global ky
    global kx
    global label222
    files = []
    try:
        files=ftp.nlst('/'+dir)
    except :
        print ("No files in this directory")
        
    
    baslik = Label(top, text= 'Tüm Dizinler ', bg='black',fg='white',width=16, height=2).place(x=0, y=5)
    for f in files:
        print (f)
        txtf=f
        label222 = Label(top, text = txtf, bg='black',fg='white',width=16, height=1)
        label222.place(x=kx, y=ky)
        ky+=25
    kx+=10
 
def get_dirs_ftp(folder=""): 
    contnts = []
    try:  
        contnts = ftp.nlst(folder)
    except :        
        print ("No files in this directory")
   
    folders = []
    if(contnts != 0):  
        for item in contnts:
            if "." not in item:
                folders.append(item)
        
    return folders

def get_all_dirs_ftp(folder=""):
    dirs = []
    new_dirs = []

    new_dirs = get_dirs_ftp()

    while len(new_dirs) > 0:
        for dir in new_dirs:
            dirs.append(dir)

        old_dirs = new_dirs[:]
        new_dirs = []
        for dir in old_dirs:
            for new_dir in get_dirs_ftp(dir):
                new_dirs.append(new_dir)

    dirs.sort()
    return dirs



def rename():
    #ftp.cwd('/home')
    resp = ftp.rename(mystring7.get(), mystring8.get());
    messagebox.showinfo( 'yeniden adlandirma',resp)    
    #ftp.cwd('/')



label9 = Label(top, text= 'baglanilacak ip adresi', bg='#856ff8', font=("Courier", 9)).place(x=630, y=2)
mystring9 =StringVar(top)
mystring9.set('127.0.0.1')
label10 = Label(top, text= 'baglanilacak port', bg='#856ff8', font=("Courier", 9)).place(x=630, y=40)
mystring10 =StringVar(top)
mystring10.set('1026')
ee2 = Entry(top,textvariable = mystring9,width=20,fg="blue",bd=3,selectbackground='violet').place(x=630, y=20)
ee2 = Entry(top,textvariable = mystring10,width=20,fg="blue",bd=3,selectbackground='violet').place(x=630, y=57)
B = Button(top, text ="Baglan", width=16, height=4,bg='black',fg='white', font=("Courier", 10), command = connect).place(x=800, y=15)



mystring2 =StringVar(top)
mystring2.set('user')
label3 = Label(top, text= 'kull. adı', bg='#856ff8', font=("Courier", 9)).place(x=630, y=80)
mystring3 =StringVar(top)
mystring3.set('12345')
label4 = Label(top, text= 'parola', bg='#856ff8', font=("Courier", 10)).place(x=630, y=120)
e1 = Entry(top,textvariable = mystring2,width=20,fg="blue",bd=3,selectbackground='violet').place(x=630, y=100)
e2 = Entry(top,textvariable = mystring3,width=20,fg="blue",bd=3,selectbackground='violet').place(x=630, y=140)
B2 = Button(top, text ="oturum ac ", width=16, height=4,bg='black',fg='white', font=("Courier", 10), command = signIn).place(x=800, y=95)
B3 = Button(top, text ="Dizinleri Listele ", width=16, height=4,bg='black',fg='white', font=("Courier", 10), command = subList).place(x=800, y=175)



label5 = Label(top, text= 'upload edilecek dosya adı', bg='#856ff8', font=("Courier", 9)).place(x=630, y=255)
mystring5 =StringVar(top)
mystring5.set('')
e1 = Entry(top,textvariable = mystring5,width=20,fg="blue",bd=3,selectbackground='violet').place(x=630, y=273)
B4 = Button(top, text ="Dosya Upload", width=16, height=4,bg='black',fg='white', font=("Courier", 10), command = uploadFile).place(x=800, y=255)


label6 = Label(top, text= 'download edilecek dosya adı', bg='#856ff8', font=("Courier", 9)).place(x=630, y=335)
mystring6 =StringVar(top)
mystring6.set('')
ee1 = Entry(top,textvariable = mystring6,width=20,fg="blue",bd=3,selectbackground='violet').place(x=630, y=353)
B4 = Button(top, text ="Dosya Download", width=16, height=4,bg='black',fg='white', font=("Courier", 10), command = downloadFile).place(x=800, y=335)


label7 = Label(top, text= 'degistirilecek dosya adı', bg='#856ff8', font=("Courier", 9)).place(x=630, y=415)
mystring7 =StringVar(top)
mystring7.set('dosya adi')
ee2 = Entry(top,textvariable = mystring7,width=20,fg="blue",bd=3,selectbackground='violet').place(x=630, y=438)

label8 = Label(top, text= 'degisecek dosya adi', bg='#856ff8', font=("Courier", 9)).place(x=630, y=465)
mystring8 =StringVar(top)
mystring8.set('dosya adi')
ee2 =Entry(top,textvariable = mystring8,width=20,fg="blue",bd=3,selectbackground='violet').place(x=630, y=485)
B7 = Button(top, text ="Dosya adi değistir", width=16, height=4,bg='black',fg='white', font=("Courier", 10), command = rename).place(x=800, y=425)





label4 = Label(top, text= 'Ftp In Python', bg='#856ff8',font=("Courier", 20))
label4.place(x=365, y=15)



top.title("Ftp Options")
top.geometry("945x580")
top.configure(bg='#856ff8')

top.mainloop()








"""

resp = ftp.mkd("/b")


istenenDizin='food'
if istenenDizin in ftp.nlst() : 
    ftp.cwd(istenenDizin)  
    ftp.retrlines('LIST')

else : 
    ftp.mkd(istenenDizin) 
    ftp.cwd(istenenDizin) 
    ftp.retrlines('LIST') 
"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    