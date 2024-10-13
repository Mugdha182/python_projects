import json
import requests
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.ttk import OptionMenu
import tkinter as tk


def populate_currency_options():
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    data = response.json()
    currency_codes = list(data['rates'].keys())
    return currency_codes

def curr_converter():
    amount=amount_inp.get()
    try:
        amount=float(amount)
    except ValueError:
        messagebox.showerror("Error","Enter valid amount!")
        amount_inp.delete(0, tk.END)
        return
        
    from_curr=from_curr_var.get()
    to_curr=to_curr_var.get()

    url=f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
    data=requests.get(url)
    plain_text=data.text
    res=json.loads(plain_text)

    exchange_rate=res['rates'][to_curr]
    converted_curr=amount*exchange_rate

    final_result.config(text=f"{amount} {from_curr} = {converted_curr} {to_curr}")
    messagebox.showinfo("Success", "AMOUNT converted successfully!")
    amount_inp.delete(0, tk.END)
    
t=Tk()
t.title("Currency Converter")
t.geometry('300x300')
t.configure(bg='turquoise')

lbl1=Label(text="Amount",font=('Arial',13))
lbl1.grid(row=0,column=0,padx=10,pady=5)

amount_inp=Entry()
amount_inp.grid(row=0,column=1,padx=10,pady=5)

currency_options=populate_currency_options()

lbl2=Label(text="From Currency",font=('Arial',13))
lbl2.grid(row=1,column=0,padx=10,pady=5)

from_curr_var=tk.StringVar(t)
from_curr_var.set('INR')
from_curr_dropdown=tk.OptionMenu(t,from_curr_var, *currency_options)
from_curr_dropdown.grid(row=1,column=1,padx=10,pady=5)

lbl3=Label(text="To Currency",font=('Arial',13))
lbl3.grid(row=2,column=0,padx=10,pady=5)
to_curr_var=tk.StringVar(t)
to_curr_var.set('USD')
to_curr_dropdown=tk.OptionMenu(t,to_curr_var, *currency_options)
to_curr_dropdown.grid(row=2,column=1,padx=10,pady=5)

convert_button=Button(text='Convert',command=curr_converter,font=('Arial',13))
convert_button.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

final_result=Label(text="",width=20)
final_result.grid(row=4,column=0,columnspan=2,padx=10,pady=5)

t.mainloop()
