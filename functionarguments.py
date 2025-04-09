#1. Default Arguments
def name (fname, mname = "Harpal", lname = "Rajput"):
    print("Hello ", fname, mname, lname)
    
name("Darshan")




#2. Keyword Arguments
def key(fname, mname, lname):
    print("Hello ", fname, mname, lname)
    
key(mname = "Harpal", lname = "Rajput", fname = "Darshan")




#3. Required Arguments
def required(fname,maname, lname):
    print("Hello ", fname, maname, lname)

# required("Darshan","Harpal") #this will give error as number of parameters passed does not matches function definition

required("Darshan","Harpal","Rajput")




#4. Variable Arguments
#arbitary arguments
def arbi(*name): #stores in tuple format
    for i in name:
        print(i)
arbi("Darshan","Harpal","Om","Karan","Yash")

def arbi2(*name):
    print("Hello",name[0],name[1],name[2])
    
arbi2("Darshan", "Harpal", "Om")


#keyword arbitary arguments
def keyarbi(**name): #stores in dictionary format
    for i,j in name.items():
        print(i,j)

keyarbi(fname = "Darshan", lname = "Rajput", mname = "Harpal")

def keyarbi2(**name):
    print("Hello",name['fname'],name['lname'],name['mname'])
    
keyarbi(mname = "Harpal", fname = "Darshan", lname = "Rajput")