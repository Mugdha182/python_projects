import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

def generate_pwd():
    pwd_len=inp1.get()
    if not pwd_len:
        messagebox.showerror("Error", "Please enter a password length.")
        clear_msg()
        return
        
    try:
        pwd_len = int(pwd_len)
    except ValueError:
        messagebox.showerror("Error", "Password length must be a valid integer.")
        clear_msg()
        return

    if pwd_len<=0:
        messagebox.showerror('Error','Invalid length!')
        clear_msg()
        return

    pwd=''
    if capital.get():
        pwd += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if special.get():
        pwd += '!@#$^&'
    if numbers.get():
        pwd += '0123456789'
    if small.get():
        pwd += 'abcdefghijklmnopqrstuvwxyz'
    if not pwd:
        messagebox.showerror('Error','Select atleast one option')
        return

    password=''.join(random.choices(pwd,k=pwd_len))
    password_input.delete(0,tk.END)
    password_input.insert(tk.END,password)
    show_msg()


def show_msg():
    messagebox.showinfo("Success", "Password generated successfully!")
    inp1.delete(0, tk.END)
    capital.set(0)
    numbers.set(0)
    special.set(0)
    small.set(0)

def clear_msg():
    inp1.delete(0, tk.END)
    capital.set(0)
    numbers.set(0)
    special.set(0)
    small.set(0)
    
t=Tk()
t.title("Password Generator")
t.geometry('400x400')
t.configure(bg='lightgreen')

lbl1=Label(text='Password length',font=('Arial',13))
lbl1.grid(row=0, column=0, padx=10, pady=5)
inp1=Entry(font=('Arial',13))
inp1.grid(row=0, column=1, padx=10, pady=5)        

lbl2=Label(text='Select Options',font=('Arial',13))
lbl2.grid(row=1, column=0, padx=10, pady=5)

capital=IntVar()
capital_checkbox=Checkbutton(text='Capital Letters',variable=capital,font=('',11))
capital_checkbox.grid(row=1,column=1,padx=10,pady=5,sticky=tk.W)

special=IntVar()
special_checkbox=Checkbutton(text='Special Characters',variable=special,font=('',11))
special_checkbox.grid(row=2,column=1,padx=10,pady=5,sticky=tk.W)

numbers=IntVar()
numbers_checkbox=Checkbutton(text='Numbers',variable=numbers,font=('',11))
numbers_checkbox.grid(row=3,column=1,padx=10,pady=5,sticky=tk.W)

small=IntVar()
small_checkbox=Checkbutton(text='Small Letters',variable=small,font=('',11))
small_checkbox.grid(row=4,column=1,padx=10,pady=5,sticky=tk.W)


gen_button=Button(text='Create Password',command=generate_pwd,font=('Arial',15))
gen_button.grid(row=5,column=0,padx=15,pady=15,columnspan=2)

password_label=Label(text='Generated password',font=('Arial',13))
password_label.grid(row=6,column=0,padx=10,pady=5)
password_input=Entry(font=('Arial',13))
password_input.grid(row=6,column=1,padx=10,pady=5)


t.mainloop()
