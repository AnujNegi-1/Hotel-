#from tkinter import *
import tkinter as tk
from tkinter import ttk
Hotel =tk.Tk()
Hotel.geometry("1000x1000")
Hotel.config(bg="#8FE2FF")
Hotel.resizable(False,False)
Hotel.title("First Code")
tk.Label(Hotel,text="DIL WALo KA DHABA", font="Algerian 25",bg="dark red",fg="white").pack(fill="both")

#checkbutton

def cbb():
    if(a.get()==1):
        x.set("80")
    if(b.get()==1):
        x1.set("100")
    if(c.get()==1):
        x2.set("200")
    if(d.get()==1):
        x3.set("40")
    if(e.get()==1):
        x4.set("150")
    if(f.get()==1):
        x5.set("180")
    if(g.get()==1):
        x6.set("400")
    if(h.get()==1):
        x7.set("200")
    if(i.get()==1):
        x8.set("1000")
def su():
    total1=0
    total2=0
    total3=0
    total4=0
    total5=0
    total6=0
    total7=0
    total8=0
    total9=0
    if(a.get()==1):
        rate1=int(x.get())
        qty1= int(qt1.get())
        total1=rate1*qty1
        t.set(str(total1))
        
    if(b.get()==1):
        rate2=int(x1.get())
        qty2= int(qt2.get())
        total2=rate2*qty2    
        t1.set(str(total2))

    if(c.get()==1):
        rate3=int(x2.get())
        qty3= int(qt3.get())
        total3=rate3*qty3
        t2.set(str(total3))

    if(d.get()==1):
        rate4=int(x3.get())
        qty4= int(qt4.get())
        total4=rate4*qty4
        t3.set(str(total4))

    if(e.get()==1):
        rate5=int(x4.get())
        qty5= int(qt5.get())
        total5=rate5*qty5
        t4.set(str(total5))
    if(f.get()==1):
        rate6=int(x5.get())
        qty6= int(qt6.get())
        total6=rate6*qty6
        t5.set(str(total6))
        
    if(g.get()==1):
        rate7=int(x6.get())
        qty7= int(qt7.get())
        total7=rate7*qty7
        t6.set(str(total7))
        
    if(h.get()==1):
        rate8=int(x7.get())
        qty8= int(qt8.get())
        total8=rate8*qty8
        t7.set(str(total8))
        
    if(i.get()==1):
        rate9=int(x8.get())
        qty9= int(qt9.get())
        total9=rate9*qty9
        t8.set(str(total9))
    
    gt.set(str((total1+total2+total3+total4+total5+total6+total7+total8+total9)))
    
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
a = tk.IntVar()
b = tk.IntVar()
c = tk.IntVar()
d = tk.IntVar()
e = tk.IntVar()
f = tk.IntVar()
g = tk.IntVar()
h = tk.IntVar()
i = tk.IntVar()
x = tk.StringVar()
x1 = tk.StringVar()
x2 = tk.StringVar()
x3 = tk.StringVar()
x4 = tk.StringVar()
x5 = tk.StringVar()
x6 = tk.StringVar()
x7 = tk.StringVar()
x8 = tk.StringVar()
t = tk.StringVar()
t1 = tk.StringVar()
t2 = tk.StringVar()
t3 = tk.StringVar()
t4 = tk.StringVar()
t5 = tk.StringVar()
t6 = tk.StringVar()
t7 = tk.StringVar()
t8 = tk.StringVar()
t9 = tk.StringVar()
gt = tk.StringVar()
gt1 = tk.StringVar()


def sc():
    tk.Label(Hotel,text='Menu', font="Algerian 25",bg="dark red",fg="white").place(x=430,y=150)
    #checkbutton
    cb = tk.Checkbutton(Hotel,text='Paneer',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=a, command=cbb).place(x=120,y=355)
    cb1 = tk.Checkbutton(Hotel,text='Egg',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=b, command=cbb).place(x=350,y=355)
    cb2 = tk.Checkbutton(Hotel,text='Handi-Gosh',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=c, command=cbb).place(x=600,y=355)
    cb3 = tk.Checkbutton(Hotel,text='Daal-Fry',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=d, command=cbb).place(x=120,y=410)
    cb4 = tk.Checkbutton(Hotel,text='Matan-Biryani',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=e, command=cbb).place(x=350,y=410)
    cb5 = tk.Checkbutton(Hotel,text='Rumali-Roti',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=f, command=cbb).place(x=600,y=410)
    cb6 = tk.Checkbutton(Hotel,text='Gulab-Jamun',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=g, command=cbb).place(x=120,y=470)
    cb7 = tk.Checkbutton(Hotel,text='Ras-malai',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=h, command=cbb).place(x=350,y=470)
    cb8 = tk.Checkbutton(Hotel,text='56-Bhog',font='algerian 16',fg="Blue",bg="#8FE2FF",variable=i, command=cbb).place(x=600,y=470)


def sc1():
    #Quantity
    tk.Label(Hotel,text="Quantity", font="Algerian 14",fg="Blue",bg="#8FE2FF").place(x=300,y=320)

    qt1=tk.Entry(Hotel,bd="2")
    qt1.place(x=300,y=350)

    qt2=tk.Entry(Hotel,bd="2")
    qt2.place(x=300,y=385)

    qt3=tk.Entry(Hotel,bd="2")
    qt3.place(x=300,y=415)

    qt4=tk.Entry(Hotel,bd="2")
    qt4.place(x=300,y=440)

    qt5=tk.Entry(Hotel,bd="2")
    qt5.place(x=300,y=470)

    qt6=tk.Entry(Hotel,bd="2")
    qt6.place(x=300,y=495)

    qt7=tk.Entry(Hotel,bd="2")
    qt7.place(x=300,y=525)

    qt8=tk.Entry(Hotel,bd="2")
    qt8.place(x=300,y=555)

    qt9=tk.Entry(Hotel,bd="2")
    qt9.place(x=300,y=580)

    #Rate
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

    rt5=tk.Entry(Hotel,bd="2",textvariable=x5)
    rt5.place(x=500,y=495)

    rt6=tk.Entry(Hotel,bd="2",textvariable=x6)
    rt6.place(x=500,y=525)

    rt7=tk.Entry(Hotel,bd="2",textvariable=x7)
    rt7.place(x=500,y=555)

    rt8=tk.Entry(Hotel,bd="2",textvariable=x8)
    rt8.place(x=500,y=580)

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
    tot4.place(x=700,y=470)

    tot5=tk.Entry(Hotel,bd="2",textvariable=t5)
    tot5.place(x=700,y=495)

    tot6=tk.Entry(Hotel,bd="2",textvariable=t6)
    tot6.place(x=700,y=525)

    tot7=tk.Entry(Hotel,bd="2",textvariable=t7)
    tot7.place(x=700,y=555)

    tot9=tk.Entry(Hotel,bd="2",textvariable=t9)
    tot9.place(x=700,y=580)

    #Invoice Label

    tk.Label(Hotel,text='Invoice', font="Algerian 25",bg="dark red",fg="white").place(x=430,y=150)

    tk.Label(Hotel,text='Paneer',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=140,y=350)
    tk.Label(Hotel,text='Egg',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=140,y=385)
    tk.Label(Hotel,text='Handi-Gosh',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=140,y=415)
    tk.Label(Hotel,text='Daal-Fry',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=140,y=440)
    tk.Label(Hotel,text='Matan-Biryani',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=130,y=470)
    tk.Label(Hotel,text='Rumali-Roti',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=140,y=495)
    tk.Label(Hotel,text='Gulab-Jamun',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=140,y=525)
    tk.Label(Hotel,text='Ras-malai',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=140,y=555)
    tk.Label(Hotel,text='56-Bhog',font='algerian 16',fg="Blue",bg="#8FE2FF").place(x=140,y=580)
    
    sub=tk.Button(Hotel,text="Submit",font=("Ariel",12,"bold"),fg='#DB1343',bd=1,height=2,width=6,command=su)
    sub.place(x=440,y=730)

    #Grand Total
    tk.Label(Hotel,text="Grand Total", font="algerian 16", fg="Blue",bg="#8FE2FF").place(x=370, y=650)

    gt1=tk.Entry(Hotel,bd="3",textvariable=gt)
    gt1.place(x=550,y=650)

#Click-Button
sub=tk.Button(Hotel,text="Bill",font=("Ariel",12,"bold"),fg='#DB1343',bd=1,height=2,width=6,command=sc1)
sub.place(x=380,y=640)

sub=tk.Button(Hotel,text="Menu",font=("Ariel",12,"bold"),fg='#DB1343',bd=1,height=2,width=6,command=sc)
sub.place(x=520,y=640)


Hotel.mainloop()  
