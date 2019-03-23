from Tkinter import *

def screen1():
    screen1 = Tk()
    screen1.geometry("300x250")
    screen1.title("LOgin Page..")
    Label(Text = "Login Page",bg ="grey", font = ("Calibri",16)).pack()
    Label(Text = "").pack()
    Button(Text = "Login").pack()
    Label(Text = "").pack()
    Button(Text = "New User").pack()