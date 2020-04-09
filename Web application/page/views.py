from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import numpy
import numpy as np
import sqlite3
import pandas as pd
from collections import OrderedDict 



def home(request): # function for home.html page of website
    
    loc = request.POST.get('Loc') #get  location data from webpage
    data = request.POST.get('Requirements') # get requirement data from webpage

    datau= str(data.upper()) 

    database = "C:/Users/Admin/Desktop/django_project/page/combined.db" # path of databse 
    con = sqlite3.connect(database) #connecting to database
    df = pd.read_sql_query("SELECT * FROM mytable",con)
    lenc = len(df.columns)
    address=list(df["ADDRESS2"])
    full = list(df['ADDRESS1'])
    username=list(df["NAME"])
    medname=list(df["MEDICAL"])
    phno = list(df["PHONE"])

    components={'Medical' : 0,
                'Count' : 0,
                'Address' : 0,
                'Phone' : 0}

    for i in range(lenc):
        
        if (df.columns[i]) == datau:
            usr= list(df[df.columns[i]])
            print (usr[i])
            flag=1
            break
        else:
            flag=0
    cell =[]
    if flag==1:
        for i in range(len(address)):
            add=address[i]
            if add == loc :
                print("location founf")
                if usr[i] > 0:
                    components={ 
                    'Medical' : medname[i],
                    'Count' : usr[i],
                    'Address' : full[i],
                    'Phone' : phno[i]}
                    
                    cell.append(components)
            else:
                print("not found")       

    print(cell)
    
    context=[
    	{
        'posts': cell
    	},
    	{ "d1" : loc , "d2" : data}
    ]
    return render(request, 'blog/home.html', context[0]) 

    

def about(request): #function for about.html

    database = "C:/Users/Admin/Desktop/django_project/page/combined.db"  
    con = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * FROM mytable",con)
   
    address=list(df["ADDRESS1"])
    
    lenc = len(address)

       
    user =[]

    for i in range(0,lenc):
        date = {}
        user.append(date)   
        for j in range(0,len(df.columns)):
            if j != 1:
                usr=(list(df[df.columns[j]]))
                
                date.update({df.columns[j]:usr[i]})
       
    print(user) 

    databasedis = {'posts':user}           
    return render(request, 'blog/about.html', databasedis)

