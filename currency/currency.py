from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msg
from forex_python.converter import CurrencyRates
import json
import requests

def currency_converter():
    def convert():
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
        currency1 = combo1.get()
        currency2 = combo2.get()
        amount = value.get()

        querystring = {"from": currency1, "to": currency2, "amount": amount}

        headers = {
            "X-RapidAPI-Key": "9ff0a6e3d5msh5c1d6279b4f50e8p14bad7jsn5c5388652aa5",
            "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        converted_amount = data["result"]["convertedAmount"]
        formatted = "{:,.4f}".format(converted_amount)
        result['text'] = formatted

        print(converted_amount, formatted)

    result = Label(root, text=" ", width=40, height=2, relief=SOLID)
    result.place(x=200, y=150)

    currency = ["CAD", "JPY","USD", "INR", "EUR", "GBP", "CNH", "CHF"]

    from_label = Label(root, text="FROM",relief=FLAT, height=1, padx=0, pady=0, font="AREAL 15 bold", anchor=NW)
    from_label.place(x=205, y=200)
    combo1 = ttk.Combobox(root, width=15, justify=CENTER)
    combo1['values'] = currency
    combo1.place(x=205, y=250)

    to_label = Label(root, text="TO",relief=FLAT,height=1, padx=0, pady=0, font="AREAL 15 bold", anchor=NW)
    to_label.place(x=370, y=200)
    combo2 = ttk.Combobox(root, width=15, justify=CENTER)
    combo2['values'] = currency
    combo2.place(x=370, y=250)

    value = Entry(root, width=20, justify=CENTER, font="IVORY 13")
    value.place(x=250, y=300)

    btn3 = Button(text="CONVERT", bg="RED", fg="BLACK", relief=RAISED, font="AREAL 15 bold", command=convert)
    btn3.place(x=300, y=350)

def register():
    m = pass_entry.get()
    if len(m) == 0:
        msg.showwarning("ERROR", "PLEASE ENTER PASSOWRD")
    elif len(m)>0 and len(m)<8:
        msg.showwarning("ERROR", "ENTER ATLEAST 8 CHARACTERS")
    else:
        label.destroy()
        label1.destroy()
        user.destroy()
        user_entry.destroy()
        password.destroy()
        pass_entry.destroy()
        btn1.destroy()

        btn2 = Button(text="CURRENCY CONVERTER", fg="CYAN", bg="BLACK", relief=RAISED, font="AREAL 15 bold", command=currency_converter)
        btn2.place(x=200, y=50)

root = Tk()
root.title("PROJECT")
root.geometry("600x600")
label = Label(root, text="WELCOME", bg="BLACK", fg="CYAN", relief=SUNKEN, font="AREAL 25 bold")
label.place(x=205, y=50)
label1 = Label(root, text="REGISTER HERE", fg="black", relief=RAISED, font="AREAL 16 bold")
label1.place(x=205, y=170)

# user name
user = Label(root, text="USERNAME", relief=RAISED, font="AREAL 11 bold")
user.place(x=200, y=250)
user_value = StringVar()
user_entry = Entry(root, textvariable=user_value, font="AREAL 12")
user_entry.place(x=300, y=250)

# password
password = Label(root, text="PASSWORD", relief=RAISED, font="AREAL 11 bold")
password.place(x=200, y=300)
pass_value = StringVar()
pass_entry = Entry(root, textvariable=pass_value, font="AREAL 12", show="*")
pass_entry.place(x=300, y=300)

btn1 = Button(text="REGISTER", fg="BLACK", relief=RAISED, font="AREAL 15 bold", command=register)
btn1.place(x=300, y=350)
root.mainloop()