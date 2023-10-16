import tkinter as tk
window=tk.Tk()
window.title("Conversion")
window.geometry("1000x500")

frame1 = tk.Frame(master=window, width=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=100, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame4 = tk.Frame(master=window, width=100, bg="green")
frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

aa = tk.Label(master=frame1,bg="red")
aa.pack()
a = tk.Label(master=frame1, text="Centimeter to Feets",height=2,width=17,borderwidth=3, relief="solid",fg="white",bg="red",font=("Arial Black",10))
centi = tk.Entry(master=frame1, width=20,relief="solid")
button = tk.Button(master=frame1, text="Click me!",borderwidth=3, relief="solid",bg="red",fg="white")
one=tk.Label(master=frame1,text="Solution:",fg="white",bg="red")
A = tk.Label(master=frame1, text="",borderwidth=1,width=18, relief="solid")
Aa = tk.Label(master=frame1,bg="red")
def on_click():
    res=float(centi.get())*0.0328
    A.config(text=str(res))
button.config(command=on_click)
a.pack()
centi.pack()
button.pack()
one.pack()
A.pack()
Aa.pack()

bb = tk.Label(master=frame2,bg="yellow")
bb.pack()
b = tk.Label(master=frame2,text="Feet to inches",height=2,width=17,borderwidth=3, relief="solid",bg="yellow",font=("Arial Black",10))
feet = tk.Entry(master=frame2, width=20,relief="solid")
button = tk.Button(master=frame2, text="Click me!",borderwidth=3, relief="solid",bg="yellow")
two=tk.Label(master=frame2,text="Solution:",bg="yellow")
B = tk.Label(master=frame2, text="",borderwidth=1,width=18, relief="solid")
def on_click():
    ress=int(feet.get())*12
    B.config(text=str(ress))
button.config(command=on_click)
b.pack()
feet.pack()
button.pack()
two.pack()
B.pack()

cc = tk.Label(master=frame3,bg="blue")
cc.pack()
c = tk.Label(master=frame3,text="Sqft to Sqmtrs",height=2,width=17,borderwidth=3, relief="solid",bg="blue",fg="white",font=("Arial Black",10))
sqft= tk.Entry(master=frame3, width=20,relief="solid")
button = tk.Button(master=frame3, text="Click me!",borderwidth=3, relief="solid",bg="blue",fg="white")
three=tk.Label(master=frame3,text="Solution:",bg="blue",fg="white")
C = tk.Label(master=frame3, text="",borderwidth=1,width=18, relief="solid")
def on_click():
    resss=float(sqft.get())*0.0929
    C.config(text=str(resss))
button.config(command=on_click)
c.pack()
sqft.pack()
button.pack()
three.pack()
C.pack()

dd = tk.Label(master=frame4,bg="green")
dd.pack()
d = tk.Label(master=frame4,text="Sqft to Acres",height=2,width=17,borderwidth=3, relief="solid",bg="green",font=("Arial Black",10))
sq = tk.Entry(master=frame4,width=20,relief="solid")
button = tk.Button(master=frame4,text="Click me!",borderwidth=3, relief="solid",bg="green")
four=tk.Label(master=frame4,text="Solution:",bg="green")
D = tk.Label(master=frame4,text="",borderwidth=1,width=18, relief="solid")
def on_click():
    ressss=float(sq.get())/43560
    D.config(text=str(ressss))
button.config(command=on_click)
d.pack()
sq.pack()
button.pack()
four.pack()
D.pack()

window.mainloop()