from tkinter import *
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier
import re

def is_valid_phone_number(phone_number):
    pattern = re.compile(r'^\+?[0-9]+$')
    return pattern.match(phone_number)

def get_phone_number_details():
    phone_number = inp1.get()
    if not is_valid_phone_number(phone_number):
        messagebox.showerror("Invalid Input", "The phone number entered is not valid. Only numbers and '+' at the beginning are allowed.")
        return
    
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country = geocoder.description_for_number(parsed_number, 'en')
        sim_card = carrier.name_for_number(parsed_number, 'en')
        result = f"Country: {country}\nSIM Card: {sim_card}"
        messagebox.showinfo("Phone Number Details", result)
    except phonenumbers.phonenumberutil.NumberParseException:
        messagebox.showerror("Invalid Number", "The phone number entered is not valid.")

t=Tk()
t.title("TRACK PHONE NUMBER")
t.geometry('500x300')
t.configure(bg='lightblue')

lbl1=Label(text="Enter Phone Number (with country code):",font=('Arial',12))
lbl1.grid(row=0, column=0, padx=10, pady=5)
inp1=Entry(font=('Arial',11))
inp1.grid(row=0, column=1, padx=10, pady=5)

track_button=Button(text='Track',command=get_phone_number_details,font=('Arial',15))
track_button.grid(row=5,column=0,padx=15,pady=15,columnspan=2)

t.mainloop()
