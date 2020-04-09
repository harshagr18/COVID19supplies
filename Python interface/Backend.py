from tkinter import *
import tkinter as tk 
from tkinter import filedialog
from PIL import Image,ImageTk
import pandas as pd
import numpy as np
import sqlite3
from collections import OrderedDict
import time


master = Tk() 
master.geometry("550x680")
master.title("Coverpage")
master.iconbitmap("C:/Users/Administrator/Desktop/Eyantra COVID 19 Challenge/images/iconn2.ico")

def read_excel(df):
    Items_list = list(df["NAME"])
    Quantity_list = list(df["PASSWORD"])
    dictionary = {Items_list[i]:Quantity_list[i] for i in range(len(Quantity_list))}
    return Items_list,Quantity_list,dictionary
    
def read_sql(data):
    con = sqlite3.connect(data)
    df = pd.read_sql_query("SELECT * FROM mytable",con)
    return df

def make_changes(data,dictionary,ID):
    connect = sqlite3.connect(data)
    curser = connect.cursor()
    if 'OXYGENERATOR'in dictionary.keys():
        var = dictionary.get('OXYGENERATOR')
        curser.execute('''Update mytable set OXYGENERATOR = (?) where NAME = (?)''',(var,ID))
        
    if 'SANITISER'in dictionary.keys():
        var = dictionary.get('SANITISER')
        curser.execute('''Update mytable set SANITISER = (?) where NAME = (?)''',(var,ID))

    if 'MASKS' in dictionary.keys():
        var = dictionary.get('MASKS')
        curser.execute('''Update mytable set MASKS = (?) where NAME = (?)''',(var,ID))

    if 'VENTILATOR' in dictionary.keys():
        var = dictionary.get('VENTILATOR')
        curser.execute('''Update mytable set VENTILATOR = (?) where NAME = (?)''',(var,ID))

    if 'PPE' in dictionary.keys():
        var = dictionary.get('PPE')
        curser.execute('''Update mytable set PPE = (?) where NAME = (?)''',(var,ID))

    if 'VITAMINB12' in dictionary.keys():
        var = dictionary.get('VITAMINB12')
        curser.execute('''Update mytable set VITAMINB12 = (?) where NAME = (?)''',(var,ID))

    if 'VITAMINC' in dictionary.keys():
        var = dictionary.get('VITAMINC')
        curser.execute('''Update mytable set VITAMINC = (?) where NAME = (?)''',(var,ID))

    if 'SURGICALS' in dictionary.keys():
        var = dictionary.get('SURGICALS')
        curser.execute('''Update mytable set SURGICALS = (?) where NAME = (?)''',(var,ID))

    if 'BEDS' in dictionary.keys():
        var = dictionary.get('BEDS')
        curser.execute('''Update mytable set BEDS = (?) where NAME = (?)''',(var,ID))
        
    connect.commit()

def make_dictionary(data,key,value):
    items = list(data[key])
    items = [x.upper() for x in items] 
    quantity =list(data[value])
    dictionary = { items[i]:quantity[i] for i in range(len(quantity))}
    return dictionary

def RBGAImage(path):
    return Image.open(path).convert("RGBA")

def popupunsuccess(msg):
    pop = Toplevel(master) 
    pop.geometry("%dx%d+%d+%d" % (200,100,400,400))
    pop.title("oops")
    pop.iconbitmap("C:/Users/Administrator/Desktop/Eyantra COVID 19 Challenge/images/iconn2.ico")
    label = Label(pop, text=msg, font=("FELIX TITLING",10,"bold"),fg="red")
    label.place(x=15, y=35)
    But = tk.Button(pop, text="Okay", command = pop.destroy)
    But.place(x=75, y=60)
    
    

bkg = RBGAImage("C:/Users/Administrator/Desktop/Eyantra COVID 19 Challenge/images/background.jpg")
bkg=bkg.resize((550,680), Image.ANTIALIAS)
logo = RBGAImage("C:/Users/Administrator/Desktop/Eyantra COVID 19 Challenge/images/coviod2.png")
logo=logo.resize((500,250), Image.ANTIALIAS)
bkg.paste(logo, (0, 0), logo)
bkgpic = ImageTk.PhotoImage(bkg)
label1 = Label(image=bkgpic)
label1.place(x=0, y=0)


un=StringVar()
pwd=StringVar()


    
def login_win():
    uname=un.get()
    pswd=pwd.get()
    print(f"Username : {uname}")
    print(f"Password : {pswd}")

    database = "C:/Users/Administrator/AppData/Local/Programs/Python/Python37/page/combined.db"  #Put the name of your database here
    dataframe = read_sql(database)
    username_list, password_list,Auth = read_excel(dataframe)
    
    #login = input("enter your login id:  ")
    for i in Auth:
      if uname in Auth:
        print("username found")
        label_2_12=Label(master, text="User Found", font=("FELIX TITLING",10,"bold"), fg="Green")
        label_2_12.place(x=280,y=280)
        flag = 1
        break
      else:
        flag = 0  
        
    if flag == 0:
        print("username not found")
        popupunsuccess("username not found")
        
    
    while(flag==1):
       x = Auth.get(uname)
       if(pswd == x):
            print("Password Confirmed")
            window2 = Toplevel(master) 
            window2.geometry("600x350")
            window2.title("Upload Page")
            window2.iconbitmap("C:/Users/Administrator/Desktop/Eyantra COVID 19 Challenge/images/iconn2.ico")
            def upload():
                file_path = filedialog.askopenfilename(initialdir="D:", title="Select a file", filetypes=(("Exel","*.xlsx"),("all files","*.*")))
                label_2_1=Label(window2, text=file_path, width=40).place(x=200, y=190)
                window2.destroy()
                while True:
                     global df
                     df = pd.read_excel(file_path)
                     keys = "Item"
                     values = "Quantity"
                     Items_Matcher = make_dictionary(df,keys,values)
                     main_database_collumns = list(dataframe.columns)
                     matching_items = set(main_database_collumns)&set(Items_Matcher.keys())
                     matching_items = list(matching_items)
                     matched_values = []
                     for i in matching_items:
                         X= Items_Matcher.get(i)
                         matched_values.append(X)
                     matched_dictionary = {matching_items[i]:matched_values[i] for i in range(len(matched_values))}
                     print(matched_dictionary)
                     make_changes(database,matched_dictionary,uname)
                     time.sleep(10)
                
    
            
            label_2_1=Label(window2, text=" UPLOAD PAGE ", font=("FELIX TITLING",40,"bold"))
            label_2_1.place(x=100,y=20)
    
            label_2_1=Label(window2, text=" Login Successful! ", font=("FELIX TITLING",10,"bold"))
            label_2_1.place(x=75,y=110)
    
            label_2_1=Label(window2, text=" Upload the excel file of your inventory ", font=("FELIX TITLING",10))
            label_2_1.place(x=75,y=150)
    
            button_2_1 = tk.Button(window2, text='Browse', width=10, bg='light grey', font=("FELIX TITLING",10), command=upload)
            button_2_1.place(x=75, y=190)
    
            button_2_2 = tk.Button(window2, text='Back', width=10, bg='light grey', font=("FELIX TITLING",10), command=window2.destroy)
            button_2_2.place(x=75, y=230)
            break
       else:
         print("Wrong Password")
         break


def signup_win():
    window1 = Toplevel(master) 
    window1.geometry("650x650")
    window1.title("Sign Up Page")
    window1.iconbitmap("C:/Users/Administrator/Desktop/Eyantra COVID 19 Challenge/images/iconn2.ico")
    un1=StringVar()
    pw=StringVar()
    fn=StringVar()
    sn=StringVar()
    sa=StringVar()
    c=StringVar()
    s=StringVar()
    pn=StringVar()
    ea=StringVar()
    
    def printt():
        label1=Label(window1, text=" SIGN UP SUCCESSFULL. Now you can go back", font=("FELIX TITLING",10,"bold"))
        label1.place(x=75,y=555)
        uname=un1.get()
        pas=pw.get()
        fname=fn.get()
        sname=sn.get()
        sadd=sa.get()
        city=c.get()
        state=s.get()
        pnumber=pn.get()
        eadd=ea.get()

        print(f"Username : {uname}")
        print(f"password: {pas}")
        print(f"Owner's name : {fname}")
        print(f"Shop name : {sname}")
        print(f"Shop address : {sadd}")
        print(f"City : {city}")
        print(f"State : {state}")
        print(f"Phone number :  {pnumber}")
        print(f"Email address : {eadd}")
        
    label_1_1=Label(window1, text=" SIGN UP PAGE", font=("FELIX TITLING",30,"bold"))
    label_1_1.place(x=150,y=75)
    
    label_1_2=Label(window1, text="Please fill in the details accurately", font=("Agency FB",15))
    label_1_2.place(x=50,y=145)
    
    label_1_2=Label(window1, text="Username ", font=("Agency FB",15))
    label_1_2.place(x=50,y=185)
    e1 = Entry(window1, width=75, textvar=un1)
    e1.place(x=175,y=195)
    
    label_1_3=Label(window1, text="Password", font=("Agency FB",15))
    label_1_3.place(x=50,y=225)
    e2 = Entry(window1, width=75, textvar=pw)
    e2.place(x=175,y=235)
    
    label_1_4=Label(window1, text="Owner's full name", font=("Agency FB",15))
    label_1_4.place(x=50,y=265)
    e3 = Entry(window1, width=75, textvar=fn)
    e3.place(x=175,y=275) 
    
    label_1_5=Label(window1, text='Shop Name', font=("Agency FB",15))
    label_1_5.place(x=50,y=305)
    e4 = Entry(window1, width=75, textvar=sn)
    e4.place(x=175,y=315)
    
    label_1_6=Label(window1, text='Shop Address', font=("Agency FB",15))
    label_1_6.place(x=50,y=345)
    e5 = Entry(window1, width=75, textvar=sa)
    e5.place(x=175,y=355)
    
    label_1_7=Label(window1, text='City', font=("Agency FB",15))
    label_1_7.place(x=50,y=385)  
    e6 = Entry(window1, width=75, textvar=c)
    e6.place(x=175,y=395)
    
    label_1_8=Label(window1, text='State', font=("Agency FB",15))
    label_1_8.place(x=50,y=425)  
    e7 = Entry(window1, width=75, textvar=s)
    e7.place(x=175,y=435)
    
    label_1_9=Label(window1, text='Phone number', font=("Agency FB",15))
    label_1_9.place(x=50,y=465)
    e8 = Entry(window1, width=75, textvar=pn)
    e8.place(x=175,y=475)
    
    label_1_10=Label(window1, text='Email address', font=("Agency FB",15))
    label_1_10.place(x=50,y=505)
    e9 = Entry(window1, width=75, textvar=ea)
    e9.place(x=175,y=515)
    
    button_1_1 = tk.Button(window1, text='Sign Up', width=15, bg='light grey', font=("FELIX TITLING",15), command=printt)
    button_1_2 = tk.Button(window1, text='Back', width=15, command=window1.destroy, bg='light grey', font=("FELIX TITLING",15))
    button_1_1.place(x=75,y=595)
    button_1_2.place(x=275,y=595)

def helpp():
    window3 = Toplevel(master) 
    window3.geometry("600x350")
    window3.title("Help Page")
    window3.iconbitmap("C:/Users/Administrator/Desktop/Eyantra COVID 19 Challenge/images/iconn2.ico")
    
    label_1_8=Label(window3, text='Coming soon .....', font=("Agency FB",15,"bold"))
    label_1_8.place(x=100,y=100)
    
imge2=Image.open("C:/Users/Administrator/Desktop/Eyantra COVID 19 Challenge/images/member.png")
imge2=imge2.resize((70,70), Image.ANTIALIAS)
photo2=ImageTk.PhotoImage(imge2)
lab2=Label(image=photo2)
lab2.place(x=75,y=200)
    
label_0_1=Label(master, text='MEMBER LOGIN ', font=("FELIX TITLING",20,"bold"))
label_0_1.place(x=150,y=215)

label_0_2=Label(master, text='USERNAME', font=("FELIX TITLING",15,"bold"))
label_0_2.place(x=80,y=300)
e1 = Entry(master, width=25, textvar=un)
e1.place(x=280,y=305)

label_0_3=Label(master, text='PASSWORD', font=("FELIX TITLING",15,"bold"))
label_0_3.place(x=80,y=350)
e2 = Entry(master, width=25, textvar=pwd)
e2.place(x=280,y=355)

button_0_1= tk.Button(master, text='Login', width=10, command=login_win, bg='pink', font=("FELIX TITLING",15))
button_0_2 = tk.Button(master, text='Exit', width=10, command=master.destroy, bg='light grey', font=("FELIX TITLING",15))
button_0_1.place(x=100,y=450)
button_0_2.place(x=300,y=450)

button_0_3 = tk.Button(master, text='Sign up now if you are a new user', command=signup_win, width=30, bg='pink', font=("FELIX TITLING",15))
button_0_3.place(x=50,y=530)

button_0_4 = tk.Button(master, text='Help?', width=10, command=helpp, bg='light grey', font=("FELIX TITLING",15))
button_0_4.place(x=200,y=580)

 



