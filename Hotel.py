#from tkinter import *
import tkinter as tk
from tkinter import ttk
Hotel =tk.Tk()
Hotel.geometry("1000x1000")
Hotel.config(bg="#8FE2FF")
Hotel.resizable(False,False)
Hotel.title("First Code")
tk.Label(Hotel,text="Bill", font="Algerian 25",bg="dark red",fg="white").pack(fill="both")
tk.Label(Hotel,text="Customer Name", font="Algerian 16",fg="Blue",bg="#8FE2FF").place(x=120,y=125)
tk.Label(Hotel,text="Bill No.", font="algerian 16",fg="Blue",bg="#8FE2FF").place(x=120, y=200)
tk.Label(Hotel,text="Contact No.", font="algerian 16",fg="Blue",bg="#8FE2FF").place(x=120, y=275)

#checkbutton

def cbb():
    if(p.get()==1):
        x.set("80")
    if(e.get()==1):
        x1.set("100")
    if(h.get()==1):
        x2.set("200")
    if(r.get()==1):
        x3.set("40")
    if(g.get()==1):
        x4.set("150")

def su():
    total1=0
    total2=0
    total3=0
    total4=0
    total5=0
    if(p.get()==1):
        rate1=int(x.get())
        qty1= int(qt1.get())
        total1=rate1*qty1
        t.set(str(total1))
        
    if(e.get()==1):
        rate2=int(x1.get())
        qty2= int(qt2.get())
        total2=rate2*qty2    
        t1.set(str(total2))

    if(h.get()==1):
        rate3=int(x2.get())
        qty3= int(qt3.get())
        total3=rate3*qty3
        t2.set(str(total3))

    if(r.get()==1):
        rate4=int(x3.get())
        qty4= int(qt4.get())
        total4=rate4*qty4
        t3.set(str(total4))

    if(g.get()==1):
        rate5=int(x4.get())
        qty5= int(qt5.get())
        total5=rate5*qty5
        t4.set(str(total5))

    
    gt.set(str((total1+total2+total3+total4+total5)))
    
nm=tk.StringVar()
nm1=tk.StringVar()
bl=tk.StringVar()
bl1=tk.StringVar()
cn=tk.StringVar()

rt=tk.StringVar()
rt1=tk.StringVar()
rt2=tk.StringVar()
tot=tk.StringVar()
tot1=tk.StringVar()
tot2=tk.StringVar()
p = tk.IntVar()
e = tk.IntVar()
h = tk.IntVar()
r = tk.IntVar()
g = tk.IntVar()
x = tk.StringVar()
x1 = tk.StringVar()
x2 = tk.StringVar()
x3 = tk.StringVar()
x4 = tk.StringVar()
t = tk.StringVar()
t1 = tk.StringVar()
t2 = tk.StringVar()
t3 = tk.StringVar()
t4 = tk.StringVar()
gt = tk.StringVar()
gt1 = tk.StringVar()


#checkbutton
cb = tk.Checkbutton(Hotel,text='Paneer',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=p, command=cbb).place(x=120,y=355)
cb1 = tk.Checkbutton(Hotel,text='Egg',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=e, command=cbb).place(x=120,y=385)
cb2 = tk.Checkbutton(Hotel,text='Handi-Gosh',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=h, command=cbb).place(x=120,y=410)
cb3 = tk.Checkbutton(Hotel,text='Rumali-Roti',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=r, command=cbb).place(x=120,y=440)
cb4 = tk.Checkbutton(Hotel,text='Gulab-Jamun',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=g, command=cbb).place(x=120,y=470)


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
tk.Label(Hotel,text="Quantity", font="Algerian 14",fg="Blue",bg="#8FE2FF").place(x=300,y=320)

qt1=tk.Entry(Hotel,bd="2")
qt1.place(x=300,y=350)

qt2=tk.Entry(Hotel,bd="2")
qt2.place(x=300,y=385)

qt3=tk.Entry(Hotel,bd="2")
qt3.place(x=300,y=415)

qt4=tk.Entry(Hotel,bd="2")
qt4.place(x=300,y=445)

qt5=tk.Entry(Hotel,bd="2")
qt5.place(x=300,y=475)



tk.Label(Hotel,text="Rate", font="Algerian 14",fg="Blue",bg="#8FE2FF").place(x=520,y=320)

rt=tk.Entry(Hotel,bd="2",textvariable=x)
rt.place(x=500,y=350)

rt1=tk.Entry(Hotel,bd="2",textvariable=x1)
rt1.place(x=500,y=385)

rt2=tk.Entry(Hotel,bd="2",textvariable=x2)
rt2.place(x=500,y=415)

rt3=tk.Entry(Hotel,bd="2",textvariable=x3)
rt3.place(x=500,y=440)

rt4=tk.Entry(Hotel,bd="2",textvariable=x4)
rt4.place(x=500,y=470)

#Total
tk.Label(Hotel,text="Total", font="Algerian 14",fg="Blue",bg="#8FE2FF").place(x=720,y=320)

tot=tk.Entry(Hotel,bd="2",textvariable=t)
tot.place(x=700,y=350)

tot1=tk.Entry(Hotel,bd="2",textvariable=t1)
tot1.place(x=700,y=385)

tot2=tk.Entry(Hotel,bd="2",textvariable=t2)
tot2.place(x=700,y=415)

tot3=tk.Entry(Hotel,bd="2",textvariable=t3)
tot3.place(x=700,y=440)

tot4=tk.Entry(Hotel,bd="2",textvariable=t4)
tot4.place(x=700,y=475)

#Grand Total
tk.Label(Hotel,text="Grand Total", font="algerian 16", fg="Blue",bg="#8FE2FF").place(x=370, y=530)

gt1=tk.Entry(Hotel,bd="3",textvariable=gt)
gt1.place(x=550,y=530)

#Click-Button
sub=tk.Button(Hotel,text="Submit",font=("Ariel",12,"bold"),fg='#DB1343',bd=1,height=2,width=6,command=su)
sub.place(x=440,y=600)


Hotel.mainloop()  
