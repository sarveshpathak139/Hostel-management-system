import getpass
import smtplib
import sys
import io
import os
from os import path
from email.mime.text import MIMEText

class Student(object):
    Name=None
    Permanent_Address=None
    Student_Mobile_Number=0
    Parent_Mobile_Number=0
    Date_of_Birth=0
    Class=None
    Department=None

    def __init__(self,Name,Permanent_Address,Student_Mobile_Number,Parent_Mobile_Number,Mail,Date_of_Birth,Class,Department):
        self.Name=Name
        self.Permanent_Address=Permanent_Address
        self.Student_Mobile_Number=Student_Mobile_Number
        self.Parent_Mobile_Number=Parent_Mobile_Number
        self.Date_of_Birth=Date_of_Birth
        self.Class=Class
        self.Department=Department
        self.Mail=Mail

    def addStudent(self):
        hid=open("Hostel_IDs.txt","r")
        Hostel_Id=0
        for i in hid:
            Hostel_Id=i
        Hostel_Id=int(Hostel_Id)
        Hostel_Id+=1
        f=open("Student"+str(Hostel_Id)+".txt","a")
        f.write("ID: "+str(Hostel_Id)+\
                "\nName: "+self.Name+\
                "\nAddress: "+self.Permanent_Address+\
                "\nS_phNumber: "+str(self.Student_Mobile_Number)+\
                "\nP_phNumber: "+str(self.Parent_Mobile_Number)+\
                "\nEmail Address: "+str(self.Mail)+\
                "\nBirth Date: "+str(self.Date_of_Birth)+\
                "\nClass: "+self.Class+\
                "\nDepartment: "+self.Department+"\n"

        )
        Hostel_Id=str(Hostel_Id)
        hid=open("Hostel_IDs.txt","a")
        hid.write("\n"+Hostel_Id)
        print self.Name+" Added Successfully with Hostel ID :"+Hostel_Id
        

    def removeStudent(self,hostel_id):

        try:
            if (path.exists("Student"+str(hostel_id)+".txt")):
                file1=open("Student"+str(hostel_id)+".txt","r")
                for i in file1:
                        print i
                file1.close()
                ch=raw_input("Are sure you want to Delete this student?\t Y/N\t")
                if ch=='y' or ch=='Y':
                    os.system('cls')
                    os.remove("Student"+str(hostel_id)+".txt")
                    print "Student with Hostel ID: "+str(hostel_id)+" is Deleted Successfully"
                else:
                    os.system('cls')
                    print "Not Deleted"
            else:
                print "Not Found"

        except:
            print "No Student Found"

class Room(Student):
    

    def __init__(self,Room_Id,Room_Capacity,Price):
        self.Room_Capacity=Room_Capacity
        self.Room_Id=Room_Id
        self.Price=Price

    def addRoom(self,roomcapacity,price):
        rid=open("Room_Id.txt","r")
        Room_Id=0
        for i in rid:
            Room_Id=i
        Room_Id=int(Room_Id)

        Room_Id+=1
        f=open("Room"+str(Room_Id)+".txt","a")
        f.write("ID: "+str(Room_Id)+\
                "\nCapacity: "+str(roomcapacity)+\
				"\nPrice: "+str(price)+"\n"
                

        )


        Room_Id=str(Room_Id)
        rid=open("Room_Id.txt","a")
        rid.write("\n"+Room_Id)
        print "New Room with Room Number : "+str(Room_Id)+" Added Successfully"

    def removeRoom(self,Room_id):

        try:
            if (path.exists("Room"+str(Room_id)+".txt")):
                file1=open("Room"+str(Room_id)+".txt","r")
                for i in file1:
                        print i
                file1.close()
                ch=raw_input("Are sure you want to Delete this room?\t Y/N\t")
                if ch=='y' or ch=='Y':
                    os.system('cls')
                    os.remove("Room"+str(Room_id)+".txt")
                    print "Room Number : "+str(Room_id)+" Deleted Successfully"
                else:
                    os.system('cls')
                    print "Room Not Deleted"
            else:
                os.system('cls')
                print "Not Found"

        except:
            os.system('cls')
            print "No room Found"

    def updateCapacity(self):
                    rn=input("Enter Room Number to be Updated:\t")
                    if (path.exists("Room"+str(rn)+".txt")):
                        rid=open("Room"+str(rn)+".txt", 'r')
                        print "\n"
                        for i in rid:
                            print i
                        rid.close()
                        print "\n"
                        cap=input("Enter New Capacity for this Room:\t")
                        with open("Room"+str(rn)+".txt", 'r') as file:
                            data = file.readlines()
                            file.seek(2)
                        data[1] = "Capacity: "+str(cap)+"\n"
                        with open("Room"+str(rn)+".txt", 'w') as file:
                            file.writelines( data )
                        os.system('cls')
                        print "\nRoom Id: "+str(rn)+" Updated with its Cpacity: "+str(cap)
                        rid=open("Room"+str(rn)+".txt", 'r')
                        print "\n"
                        for i in rid:
                            print i
                        print "\n"
                        rid.close()
                    else:
                        print "Room Not Found"

    def assignRoom(self):
                    students={}
                    print "\nAvailable Rooms"
                    print "-"*10
                    rooms=open("Room_Id.txt","r")
                    for i in rooms:
                            print "Rooms"+str(i)
                    print "-"*10
                    rn=input("Enter Room Number to be Assigned:\t")
                    if (path.exists("Room"+str(rn)+".txt")):
                        rid=open("Room"+str(rn)+".txt", 'r')
                        '''strt=3
                        counter=2
                        x=0
                        for i in rid:
                            
                            if counter<=strt:
                                students[x]=i
                                x+=1
                            counter+=1'''
                        
                        for i in rid:
                            print i
                        rid.close()
                        print "\nAvailable Students"
                        print "-"*10
                        studs=open("Hostel_Ids.txt","r")
                        for i in studs:
                        
                            if i=='0':
                                continue
                            else:
                                print "Student"+str(i)
                        print "-"*10
                        
                        stud=input("Enter Student ID to be Assigned :\t")
                        if (path.exists("Student"+str(stud)+".txt")):
                            sid=open("Student"+str(stud)+".txt","r")
                            print "\n"
                            for i in sid:
                                print i
                            sid.close()
                            print "\n"
                            ch=raw_input("Are you sure want to assign this student to Room"+str(rn)+" ?\tY/N :\t")
                            if ch=='Y' or ch=='y':
                                rid=open("Room"+str(rn)+".txt", "a")
                                rid.write("Student Assigned :Student"+str(stud))
                                sid=open("Student"+str(stud)+".txt","a")
                                sid.write("\nRoom Assigned: Room"+str(rn))
                                
                                os.system('cls')
                            
                                print "Assignment Done Successfully"
                                sid.close()
                                rid.close()
                                                            
                            
                        else:
                            print "Student Not Found"
                    else:
                        print "Room Not Found"
    



class Admin(Room):

    def __init__(self,Username,Password):
        self.Username=Username
        self.Password=Password
	
    def Login(self):
        print "*"*10,
        print "Login Page",
        print "*"*10,
        print "\n"
        self.Username=raw_input("Enter Username: \t")
        self.Password=getpass.getpass("Enter Password: \t")

        if (self.Username=="admin" and self.Password=="admin"):
            os.system('cls')
            while True:
             
               print "-"*50
               print "Welcome to the ADMIN Page"
               print "-"*50
               print "1.Add Room\n2.Remove Room\n3.Change Room Capacity\n4.Assign Student to a Room\n5.Logout"
               r=Room(0,0,0)
               choice=input("Enter your choice:\t") #Choice provided for user to perform various operations using menu
               if choice==1:
                   self.cap=input("Enter Capacity of the Room:\t")
                   self.price=input("Enter Price of the Room:\t")
                   os.system('cls')
                   r.addRoom(self.cap,self.price)

               elif choice==2:
                       id=input("Enter Room Number to be Removed:\t")
                       r.removeRoom(id)

               elif choice==3:
                    r.updateCapacity()
               elif choice==4:
                    r.assignRoom()

                

			

               elif choice==5:
                   os.system('cls')
                   print "Admin Logged out Successfully"
                   a=Admin(self.Username,self.Password)
                   a.Login()
               else:
                   os.system('cls')
                   print "Enter Correct Choice"

        elif (self.Username=="rector" and self.Password=="rector"):


                os.system('cls')
                while True:

                   print "-"*50
                   print "Welcome to the RECTOR Page"
                   print "-"*50
                   print "1.Add Student\n2.Remove Student\n3.Logout"


                   choice=input("Enter your choice:\t") #Choice provided for user to perform various operations using menu
                   if choice==1:
                           name=raw_input('Enter Your Name:\t')
                           addr=raw_input('Enter your Permanent Address:\t')
                           contact_S=input('Enter Your Mobile Number:\t')
                           contact_P=input("Enter Your parent's Mobile Number:\t")
                           mail=raw_input('Enter Email Address:\t')
                           dob=raw_input('Enter Date of Birth:\t')
                           clss=raw_input('Enter your Class:\t') 
                           dept=raw_input('Enter your Department:\t')
                           os.system('cls')
                           s=Student(name,addr,contact_S,contact_P,mail,dob,clss,dept)
                           s.addStudent()
                           msg = MIMEText("Welcome to Hostel Databse")
                           msg['Subject'] = 'Admission'
                           msg['From'] = 'kedar@mitaoe.ac.in'
                           msg['To'] = mail
                           s = smtplib.SMTP('smtp.gmail.com', 587)
                           s.ehlo()
                           s.starttls()
                           s.login(msg['From'], 'kedar1023') 
                           try:
                               s.send_message(msg)
                           except AttributeError:
                               s.sendmail(msg['From'], [msg['To']], msg.as_string())
                           s.quit()



                   if choice==2:
                            hostel_id=input('Enter Hostel ID of the Student to be Removed:\t')


                            s=Student("","",0000000000,0000000000,0000000000,"","","")
                            s.removeStudent(hostel_id)
                   if choice==3:
                       os.system('cls')
                       print "Admin Logged out Successfully"
                       a=Admin(self.Username,self.Password)
                       a.Login()

        else:
            os.system('cls')
            print "Enter Valid Credentials"
            a=Admin(self.Username,self.Password)
            a.Login()


a=Admin("","")
a.Login()

