#bismillah
import tkinter as tk
from tkinter import *

pencere = tk.Tk()
pencere.geometry("345x550+630+150")
pencere.title("Calculater")

def press_button(giris):
    global denklem
    denklem = denklem + str(giris)
    denklem_degeri.set(denklem)

def result():
    global denklem
    try:
        islem_sonucu = str(eval(denklem))
        denklem_degeri.set(islem_sonucu)
        denklem = islem_sonucu
    except:
        denklem_degeri.set("ERROR")
        denklem = ""

def clear():
    global denklem
    denklem_degeri.set("")
    denklem = ""

denklem = ""

denklem_degeri = StringVar()

denklem_yazisi = tk.Label(pencere,textvariable=denklem_degeri,font="consolas 20",bg="black",fg="white",width=24,height=2)
denklem_yazisi.pack()

cerceve = tk.Frame(pencere)
cerceve.pack(pady=5)


buton1= tk.Button(cerceve,text="1",bg="orange",height=4,width=7,font=35,command= lambda: press_button(1))
buton1.grid(row=0,column=0)

buton2= tk.Button(cerceve,text="2",bg="orange",height=4,width=7,font=35,command= lambda: press_button(2))
buton2.grid(row=0,column=1)

buton3= tk.Button(cerceve,text="3",bg="orange",height=4,width=7,font=35,command= lambda: press_button(3))
buton3.grid(row=0,column=2)

buton4= tk.Button(cerceve,text="4",bg="orange",height=4,width=7,font=35,command= lambda: press_button(4))
buton4.grid(row=1,column=0)

buton5= tk.Button(cerceve,text="5",bg="orange",height=4,width=7,font=35,command= lambda: press_button(5))
buton5.grid(row=1,column=1)

buton6= tk.Button(cerceve,text="6",bg="orange",height=4,width=7,font=35,command= lambda: press_button(6))
buton6.grid(row=1,column=2)

buton7= tk.Button(cerceve,text="7",bg="orange",height=4,width=7,font=35,command= lambda: press_button(7))
buton7.grid(row=2,column=0)

buton8= tk.Button(cerceve,text="8",bg="orange",height=4,width=7,font=35,command= lambda: press_button(8))
buton8.grid(row=2,column=1)

buton9= tk.Button(cerceve,text="9",bg="orange",height=4,width=7,font=35,command= lambda: press_button(9))
buton9.grid(row=2,column=2)

buton0= tk.Button(cerceve,text="0",bg="orange",height=4,width=7,font=35,command= lambda: press_button(0))
buton0.grid(row=3,column=1)

toplama= tk.Button(cerceve,text="+",bg="silver",height=4,width=7,font=35,command= lambda: press_button("+"))
toplama.grid(row=0,column=3)

cikarma= tk.Button(cerceve,text="-",bg="silver",height=4,width=7,font=35,command= lambda: press_button("-"))
cikarma.grid(row=1,column=3)

carpma= tk.Button(cerceve,text="x",bg="silver",height=4,width=7,font=35,command= lambda: press_button("*"))
carpma.grid(row=2,column=3)

bolme= tk.Button(cerceve,text="/",bg="silver",height=4,width=7,font=35,command= lambda: press_button("/"))
bolme.grid(row=3,column=3)

esittir= tk.Button(cerceve,text="=",bg="silver",height=4,width=7,font=35,command=result)
esittir.grid(row=3 ,column=2)

virgul= tk.Button(cerceve,text=",",bg="silver",height=4,width=7,font=35,command= lambda: press_button("."))
virgul.grid(row=3,column=0)

temizle = tk.Button(pencere,text="AC",bg="gray",height=2,width=31,font=35,command=clear)
temizle.pack()


pencere.mainloop()