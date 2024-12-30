from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x233")
root.title("slider")

def getbuck():
    print(f"we have {myslider2.get()}credited bucks")
    a = tmsg.showinfo("Paytm karo",f"gotcha {myslider2.get()}")
    a = tmsg.showinfo(f"gotcha {myslider2.get()}","fbi is on the way")
# myslider = Scale(root,from_=0 , to=100)
# myslider.pack()

Label(root,text="how many bucks u want mf?").pack()

myslider2 = Scale(root, from_=0, to = 100, orient=HORIZONTAL,tickinterval=50)
# myslider2.set(34)
myslider2.pack()

Button(root, text="get bucks",  command=getbuck).pack()

root.mainloop()