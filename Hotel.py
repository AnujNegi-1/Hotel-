#from tkinter import *
import tkinter as tk
from tkinter import ttk
Hotel =tk.Tk()
Hotel.geometry("1000x1000")
Hotel.resizable(False,False)
Hotel.title("First Code")
tk.Label(Hotel,text="Bill", font="Algerian 25",bg="dark red",fg="white").pack(fill="both")

tk.Label(Hotel,text="Customer Name", font="Algerian 16",fg="black").place(x=120,y=125)
tk.Label(Hotel,text="Bill No.", font="algerian 16", fg="black").place(x=120, y=200)
tk.Label(Hotel,text="Contact No.", font="algerian 16", fg="black").place(x=120, y=275)


#checkbutton

def cbb():
    
    if(p.get()==1):
        x.set("80")
        t.set(val(qt)*80)
    if(e.get()==1):
        x1.set("100")
        t1=val(tot1=x1*rt1)
    if(h.get()==1):
        x2.set("200")
        t2=val(tot2=x2*rt2)
        

nm=tk.StringVar()
nm1=tk.StringVar()
bl=tk.StringVar()
bl1=tk.StringVar()
cn=tk.StringVar()
qt=tk.StringVar()
qt1=tk.StringVar()
qt2=tk.StringVar()
qt3=tk.StringVar()
rt=tk.StringVar()
rt1=tk.StringVar()
rt2=tk.StringVar()
tot=tk.StringVar()
tot1=tk.StringVar()
tot2=tk.StringVar()
p = tk.IntVar()
e = tk.IntVar()
h = tk.IntVar()
x = tk.StringVar()
x1 = tk.StringVar()
x2 = tk.StringVar()
t = tk.StringVar()
t1 = tk.StringVar()
t2 = tk.StringVar()

#checkbutton
cb = tk.Checkbutton(Hotel,text='Paneer',font='algerian 16',fg='black',variable=p, command=cbb).place(x=120,y=355)
cb1 = tk.Checkbutton(Hotel,text='Egg',font='algerian 16',fg='black',variable=e, command=cbb).place(x=120,y=385)
cb2 = tk.Checkbutton(Hotel,text='Handi-Gosh',font='algerian 16',fg='black',variable=h, command=cbb).place(x=120,y=410)


#Combobox

#Name
nm=tk.StringVar()
name = ttk.Combobox(Hotel, width = 10, textvariable = nm)
name['values'] = (' Mr'
                  ' Ms'
                  ' Mrs')

name.place(x=350,y=125)
name.current()

nm1=tk.Entry(Hotel,bd="2",textvariable=nm1)
nm1.place(x=450,y=125)

#Bill no.

bl1=tk.Entry(Hotel,bd="1",textvariable=bl1)
bl1.place(x=300,y=200)

#Contact N0.
cn1=tk.Entry(Hotel,bd="2",textvariable=cn)
cn1.place(x=300,y=275)

#Quantity
tk.Label(Hotel,text="Quantity", font="Algerian 14",fg="black").place(x=300,y=320)

qt1=tk.Entry(Hotel,bd="2",textvariable=qt)
qt1.place(x=300,y=350)

qt2=tk.Entry(Hotel,bd="2",textvariable=qt1)
qt2.place(x=300,y=385)

qt3=tk.Entry(Hotel,bd="2",textvariable=qt2)
qt3.place(x=300,y=415)

tk.Label(Hotel,text="Rate", font="Algerian 14",fg="black").place(x=520,y=320)

rt=tk.Entry(Hotel,bd="2",textvariable=x)
rt.place(x=500,y=350)

rt1=tk.Entry(Hotel,bd="2",textvariable=x1)
rt1.place(x=500,y=385)

rt2=tk.Entry(Hotel,bd="2",textvariable=x2)
rt2.place(x=500,y=415)

tk.Label(Hotel,text="Total", font="Algerian 14",fg="black").place(x=720,y=320)

tot=tk.Entry(Hotel,bd="2",textvariable=t)
tot.place(x=700,y=350)

tot1=tk.Entry(Hotel,bd="2",textvariable=t1)
tot1.place(x=700,y=385)

tot2=tk.Entry(Hotel,bd="2",textvariable=t2)
tot2.place(x=700,y=415)

Hotel.mainloop()
