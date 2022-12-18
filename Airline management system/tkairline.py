import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import mysql.connector as ms

f=("Passport number","Customer name","Father's name","Address","Phone number")
f1=("Flight name", "Flight code","Class","Total seats","Source","Destination","Departure Time","Arrival Time","Fare")
f3=("Passport number","Flight code","Flight name","Class","Source","Destination","Arrival Time","Departure Time","Fare","Current Date(YYYY/MM/DD)","Name","Age","Gender","Seat no")

#to close the window
def cw():
    root.destroy()
    
#clear entry of customer
def cec(entries):
    entries['Passport number'].delete(0,tk.END)
    entries['Customer name'].delete(0,tk.END)
    entries["Father's name"].delete(0,tk.END)
    entries['Address'].delete(0,tk.END)
    entries['Phone number'].delete(0,tk.END)

#form of customer details   
def form(t,f):
    entries={}
    for i in f:
        row = tk.Frame(t)
        lab = tk.Label(row,width=25, text=i,font='Century 15 bold', anchor='w')
        ent = tk.Entry(row,font='Century 15 bold')
        ent.insert(0, "")
        row.pack(side=tk.TOP, 
                    fill=tk.X, 
                    padx=25, 
                    pady=20)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, 
                     expand=tk.NO, 
                     fill=tk.X)
        entries[i] = ent
    return entries

#to fetch/add details of customer
def fetch(entries):
    pn=str(entries["Passport number"].get())
    cn=str(entries["Customer name"].get())
    fn=str(entries["Father's name"].get())
    ad=str(entries["Address"].get())
    phn=int(entries["Phone number"].get())
    l="insert into customer values(%s,%s,%s,%s,%s)"
    k=(pn,cn,fn,ad,phn)
    cur=db.cursor()
    cur.execute(l,k)
    cur.execute('commit')
    messagebox.showinfo("Add","Details inserted Successfully \n       :) ")
    cur.execute('select * from customer')
    for x in cur:
        print(x)

# to update customer detail
def update(entries):
    pn=str(entries["Passport number"].get())
    cn=str(entries["Customer name"].get())
    fn=str(entries["Father's name"].get())
    ad=str(entries["Address"].get())
    phn=int(entries["Phone number"].get())
    l="update customer set full_name=%s,father_name=%s,address=%s,phone_no=%s where passport_no=%s"
    k=(cn,fn,ad,phn,pn)
    cur=db.cursor()
    cur.execute(l,k)
    cur.execute('commit')
    messagebox.showinfo("Update","Details updated/changed succesfully \n         :)")
    cur.execute('select * from customer')
    for x in cur:
        print(x)

#to delete customer details
def delc(entries):
    pn=entries["Passport number"].get()
    cnf=messagebox.askyesno('Verify', 'Sure to delete')
    cur=db.cursor()
    if cnf==True:
        cur.execute("delete from customer where passport_no='%s'"%pn)
        messagebox.showinfo("Delete"," Record Deleted Successfully \n         :) ")
        cur.execute('commit')
    else:
        messagebox.showinfo('Cancel', 'Deletion has been cancelled \n         :) ')
    cur.execute('select * from customer')
    for x in cur:
        print(x)

#to make customer window
def open_window1():
    global f
    top1=Toplevel()
    top1.title("Customer details")
    top1.geometry('1350x690+0+0')
    top1.configure(background="lightpink")
    l=Label(top1,text="Customer Details",bg='yellow',fg='red',font="Century 40 bold")
    l.pack( side=tk.TOP,
                 fill=tk.X,
                 padx=5, 
                 pady=10)
    l1=Label(top1,text=" => To delete any customer detail only required to type passport number and then click delete",fg='green',bg='lightyellow',font="Century 15 bold")
    l1.pack( side=tk.TOP,
                 fill=tk.X,
                 padx=5, 
                 pady=10)
    ents =form(top1,f)
    b1=Button(top1,text='ADD',bg="blue" ,fg="white",font="Century 16 bold" ,command=(lambda e=ents: fetch(e)))
    b1.pack( side=tk.LEFT,
                     padx=80, 
                     pady=5)
    b2=Button(top1,text='UPDATE',bg="blue" ,fg="white",font="Century 16 bold",command=(lambda e=ents: update(e)))
    b2.pack(side=tk.LEFT,
                     padx=80,
                     pady=5)
    b3=Button(top1,text='DELETE',bg="blue" ,fg="white",font="Century 16 bold" ,command=(lambda e=ents: delc(e)))
    b3.pack(side=tk.LEFT, 
                     padx=80,
                     pady=5)
    b4=Button(top1, text=" CLOSE ",bg="blue",fg="white",font="Century 16 bold", command=cw)
    b4.pack(side=tk.LEFT, 
                 padx=80, 
                 pady=5)
    b5=Button(top1,text=" CLEAR ", bg="blue", fg="white", font="Century 16 bold", command=(lambda e=ents: cec(e)))
    b5.pack(side=tk.LEFT, 
                 padx=80, 
                 pady=5)
    top1.mainloop()

#form of flight details   
def form1(t1,f1):
    entries1={}
    for i in f1:
        row = tk.Frame(t1)
        lab = tk.Label(row,width=25, text=i,font='Century 15 bold', anchor='w')
        ent = tk.Entry(row,font='Century 15 bold')
        ent.insert(0, "")
        row.pack(side=tk.TOP, 
                    fill=tk.X, 
                    padx=20, 
                    pady=10)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, 
                     expand=tk.NO, 
                     fill=tk.X)
        entries1[i] = ent
    return entries1

#to fetch/add details of flight
def fetch1(entries1):
    fln=str(entries1["Flight name"].get())
    fc=str(entries1["Flight code"].get())
    cls=str(entries1["Class"].get())
    ts=int(entries1["Total seats"].get())
    sr=str(entries1["Source"].get())
    dest=str(entries1["Destination"].get())
    dt=str(entries1["Departure Time"].get())
    at=str(entries1["Arrival Time"].get())
    fare=int(entries1["Fare"].get())
    l="insert into flight values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    k=(fln,fc,cls,ts,sr,dest,dt,at,fare)
    cur=db.cursor()
    cur.execute(l,k)
    cur.execute('commit')
    messagebox.showinfo("Add","Details inserted Successfully \n       :) ")
    cur.execute('select * from flight')
    for x in cur:
        print(x)

# to update flight detail
def update1(entries1):
    fln=str(entries1["Flight name"].get())
    fc=str(entries1["Flight code"].get())
    cls=str(entries1["Class"].get())
    ts=int(entries1["Total seats"].get())
    sr=str(entries1["Source"].get())
    dest=str(entries1["Destination"].get())
    dt=str(entries1["Departure Time"].get())
    at=str(entries1["Arrival Time"].get())
    fare=int(entries1["Fare"].get())
    l="update flight set flight_name=%s,class=%s,total_seats=%s,source=%s,destination=%s,departure_time=%s,arrival_time=%s,ticket_cost=%s where flight_code=%s"
    k=(fln,cls,ts,sr,dest,dt,at,fare,fc)
    cur=db.cursor()
    cur.execute(l,k)
    cur.execute('commit')
    messagebox.showinfo("Update","Details updated/changed succesfully \n       :)")
    cur.execute('select * from flight')
    for x in cur:
        print(x)

#to delete flight details
def del1(entries1):
    fc=str(entries1["Flight code"].get())
    cnf=messagebox.askyesno('Verify', 'Sure to delete \n       :) ')
    cur=db.cursor()
    if cnf==True:
        cur.execute("delete from flight where flight_code='%s'"%fc)
        messagebox.showinfo("Delete"," Record Deleted Successfully \n         :) ")
        cur.execute('commit')
    else:
        messagebox.showinfo('Cancel', 'Deletion has been cancelled \n         :) ')
    cur.execute('select * from flight')
    for x in cur:
        print(x)
        
#clear entry of flight
def cef(entries1):
    entries1["Flight name"].delete(0,tk.END)
    entries1["Flight code"].delete(0,tk.END)
    entries1["Class"].delete(0,tk.END)
    entries1["Total seats"].delete(0,tk.END)
    entries1["Source"].delete(0,tk.END)
    entries1["Destination"].delete(0,tk.END)
    entries1["Departure Time"].delete(0,tk.END)
    entries1["Arrival Time"].delete(0,tk.END)
    entries1["Fare"].delete(0,tk.END)

#to make flight window    
def open_window2():
    global f1
    top2=Toplevel()
    top2.title("Flight details")
    top2.geometry('1350x690+0+0')
    top2.configure(background="lightpink")
    l=Label(top2,text="Flight details",bg='yellow',fg='red',font="Century 40 bold")
    l.pack( side=tk.TOP,
                     fill=tk.X,
                     padx=5, 
                     pady=5)
    l1=Label(top2,text=" => To delete any customer detail only required to type flight code and then click delete",fg='green',bg='lightyellow',font="Century 15 bold")
    l1.pack( side=tk.TOP,
                     fill=tk.X,
                     padx=5, 
                     pady=5)
    ents1 =form1(top2,f1)
    b1=Button(top2,text='ADD',bg="blue" ,fg="white",font="Century 16 bold" ,command=(lambda e=ents1: fetch1(e)))
    b1.pack( side=tk.LEFT,
                     padx=80, 
                     pady=3)
    b2=Button(top2,text='UPDATE',bg="blue" ,fg="white",font="Century 16 bold",command=(lambda e=ents1: update1(e)))
    b2.pack(side=tk.LEFT,
                     padx=80,
                     pady=3)
    b3=Button(top2,text='DELETE',bg="blue" ,fg="white",font="Century 16 bold" ,command=(lambda e=ents1: del1(e)))
    b3.pack(side=tk.LEFT, 
                     padx=80,
                     pady=5)
    b4=Button(top2, text=" CLOSE ",bg="blue",fg="white",font="Century 16 bold", command=cw)
    b4.pack(side=tk.LEFT, 
                   padx=80, 
                   pady=5)
    b5=Button(top2,text=" CLEAR ", bg="blue", fg="white", font="Century 16 bold", command=(lambda e=ents1: cef(e)))
    b5.pack(side=tk.LEFT, 
                  padx=80, 
                  pady=5)
    top2.mainloop()

#form of tickets booking  
def form2(t2,f3):
    entries2 = {}
    for i in f3:
        row = tk.Frame(t2)
        lab = tk.Label(row, width=22, text=i+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=35, 
                 pady=7)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, 
                 expand=tk.NO, 
                 fill=tk.X)
        entries2[i] = ent
    return entries2

#search details
def search(entries2):
    entries2["Flight name"].delete(0,tk.END)
    entries2["Class"].delete(0,tk.END)
    entries2["Source"].delete(0,tk.END)
    entries2["Destination"].delete(0,tk.END)
    entries2["Departure Time"].delete(0,tk.END)
    entries2["Arrival Time"].delete(0,tk.END)
    entries2["Fare"].delete(0,tk.END)
    fc=entries2["Flight code"].get()
    cur=db.cursor()
    cur.execute("select * from flight where flight_code='%s'"%(fc))
    r=cur.fetchone()
    print(r)
    if r==None:
        messagebox.showinfo("Search","Record not found \n        :) ")
    else:
        fln=r[0]
        fc=r[1]
        cls=r[2]
        sr=r[4]
        dest=r[5]
        dt=r[6]
        at=r[7]
        fare=r[8]
        entries2["Flight code"].delete(0, tk.END)
        entries2["Flight name"].insert(0, fln)
        entries2["Flight code"].insert(0, fc)
        entries2["Class"].insert(0, cls)
        entries2["Source"].insert(0, sr)
        entries2["Destination"].insert(0, dest)
        entries2["Departure Time"].insert(0, dt)
        entries2["Arrival Time"].insert(0, at)
        entries2["Fare"].insert(0, fare)

#to fetch/add details of ticket
def fetch2(entries2):
    pn=str(entries2["Passport number"].get())
    fc=str(entries2["Flight code"].get())
    fln=str(entries2["Flight name"].get())
    cls=str(entries2["Class"].get())
    sr=str(entries2["Source"].get())
    dest=str(entries2["Destination"].get())
    at=str(entries2["Arrival Time"].get())
    dt=str(entries2["Departure Time"].get())
    cdate=str(entries2["Current Date(YYYY/MM/DD)"].get())
    name=str(entries2["Name"].get())
    age=str(entries2["Age"].get())
    gen=str(entries2["Gender"].get())
    sno=str(entries2["Seat no"].get())
    fare=int(entries2["Fare"].get())
    l="insert into ticket values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    k=(pn,fc,fln,cls,sr,dest,at,dt,cdate,name,age,gen,sno,fare)
    cur=db.cursor()
    cur.execute(l,k)
    cur.execute('commit')
    messagebox.showinfo("Book","Ticket booked Successfully \n       :) ")
    cur.execute('select * from ticket')
    for x in cur:
        print(x)

#to delete ticket details
def del2(entries2):
    pn=str(entries2["Passport number"].get())
    fc=str(entries2["Flight code"].get())
    cnf=messagebox.askyesno('Verify', 'Sure to delete \n       :) ')
    cur=db.cursor()
    if cnf==True:
        cur.execute("delete from ticket where Passport_no='%s' And Flight_code='%s'"%(pn,fc))
        messagebox.showinfo("Cancel"," Record Cancelled Successfully \n         :) ")
        cur.execute('commit')
    else:
        messagebox.showinfo('Cancel', 'Cancel of ticket has been cancelled \n         :) ')
    cur.execute('select * from ticket')
    for x in cur:
        print(x)

#clear entry of ticket
def cet(entries2):
    entries2["Passport number"].delete(0,tk.END)
    entries2["Flight code"].delete(0,tk.END)
    entries2["Flight name"].delete(0,tk.END)
    entries2["Class"].delete(0,tk.END)
    entries2["Source"].delete(0,tk.END)
    entries2["Destination"].delete(0,tk.END)
    entries2["Arrival Time"].delete(0,tk.END)
    entries2["Departure Time"].delete(0,tk.END)
    entries2["Current Date(YYYY/MM/DD)"].delete(0,tk.END)
    entries2["Name"].delete(0,tk.END)
    entries2["Age"].delete(0,tk.END)
    entries2["Gender"].delete(0,tk.END)
    entries2["Seat no"].delete(0,tk.END)
    entries2["Fare"].delete(0,tk.END)

# Generate seat Number:
def gensno(entries2):
    s="select max(Seat_no) from ticket"
    cur=db.cursor()
    cur.execute(s)
    ms=cur.fetchone()
    sno=int(ms[0])+1
    entries2["Seat no"].delete(0,tk.END)
    entries2["Seat no"].insert(0, sno)
    
#ticket reservation
def open_window3():
    global f3
    top3=Toplevel()
    top3.title("ticket reservation")
    top3.geometry('1350x690+0+0')
    top3.configure(background="lightpink")
    l1=tk.Label(top3,text="TICKET RESERVATION",bg='yellow',fg='red',font="Century 30 bold")
    l1.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=3)
    l2=tk.Label(top3,text="Enter flight code and then click on search to get flight details\nEnter passport number and flight code and then click on cancel to cancel the reservation\nclick on generate seat number to get seat no",bg='lightyellow',fg='green',font="Century 13")
    l2.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=3)
    ents2 =form2(top3,f3)
    b1=Button(top3,text='SEARCH',bg="blue" ,fg="white",font="Century 16 bold",command= (lambda e=ents2: search(e)))
    b1.pack( side=tk.LEFT,
                     padx=60, 
                     pady=3)
    b2=Button(top3,text='GENERATE\nSEAT NUMBER',bg="blue" ,fg="white",font="Century 8 bold",command= (lambda e=ents2: gensno(e)))
    b2.pack( side=tk.LEFT,
                     padx=60, 
                     pady=3)
    b3=Button(top3,text='ADD',bg="blue" ,fg="white",font="Century 14 bold",command= (lambda e=ents2: fetch2(e)))
    b3.pack(side=tk.LEFT,
                     padx=60,
                     pady=3)
    b4=Button(top3,text='CANCEL',bg="blue" ,fg="white",font="Century 14 bold",command= (lambda e=ents2: del2(e)))
    b4.pack(side=tk.LEFT, 
                     padx=60,
                     pady=3)
    b5=Button(top3, text=" CLEAR ",bg="blue",fg="white",font="Century 14 bold",command= (lambda e=ents2: cet(e)))
    b5.pack(side=tk.LEFT, 
                   padx=60, 
                   pady=3)
    b6=Button(top3,text=" CLOSE ", bg="blue", fg="white", font="Century 14 bold", command=cw)
    b6.pack(side=tk.LEFT, 
                  padx=60, 
                  pady=3)
    top3.mainloop()
    
db=ms.connect(host='localhost',user='root',passwd='root',database='airline_management_system')
root = Tk()
root.geometry('1350x690+0+0')
root.configure(background="blue")

#to create label
l=Label(root,text="Welcome to Airline Management System",bg='red',fg='yellow',font="Century 40 bold")
l.pack( side=tk.TOP,
                 fill=tk.X,
                 padx=5, 
                 pady=10)

#to link window with button
b1=Button(root,text='Customer details',bg="white" ,fg="black",font="Papyrus 18 bold" ,command=open_window1)
b1.pack( side=tk.TOP,
                 padx=5, 
                 pady=10)
b2=Button(root,text='Flight details',bg="white" ,fg="black",font="Papyrus 18 bold" ,command=open_window2)
b2.pack(side=tk.TOP,
                 padx=5,
                 pady=10)
b3=Button(root,text='Ticket reservation',bg="white" ,fg="black",font="Papyrus 18 bold" ,command=open_window3)
b3.pack(side=tk.TOP, 
                 padx=5, 
                 pady=10)
b4=Button(root, text="Exit",bg="white",fg="black",font="Papyrus 18 bold", command=cw)
b4.pack(side=tk.TOP, 
                 padx=5, 
                 pady=10)

root.mainloop()


