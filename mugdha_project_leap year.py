from tkinter import *
from tkinter import messagebox
t = Tk()
t.geometry('400x300')
t.configure(bg='lightgreen') 
t.title("LEAP YEAR DETECTION SYSTEM")

lbl1=Label(text="Enter Year",font=('Arial', 16))
lbl1.pack(pady=(20, 5))

inp1=Entry()
inp1.pack()

def lp_year():
    try:
        year=int(inp1.get())
        if(year % 400 == 0 and year % 100 == 0):
            messagebox.showinfo("result",f"{year} is a leap year!")
        elif(year % 4 ==0 and year % 100 != 0):
            messagebox.showinfo("result",f"{year} is a leap year!")
        else:
            messagebox.showinfo("result",f"{year} is not a leap year!")
    except:
        messagebox.showerror("result","Please enter a valid year!")


btn1 = Button(text = "Check",command = lp_year,font=('Arial', 13))
btn1.pack(pady=(20, 5))

t.mainloop()

