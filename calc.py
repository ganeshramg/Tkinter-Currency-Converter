# Package import
from tkinter import *
import requests

# API call using requests to get live data with base currency USD
# Sign Up in any open source api provider website and paste your API-ID in the myId variable below
myId = '' #API ID
url = 'https://openexchangerates.org/api/latest.json?app_id=' + myId #Appending API ID
response = requests.get(url).json()
conversion_value = response['rates']['INR'] #JSON Object - Python Dictionary

# Root Widget
root = Tk()
root.title('USD to INR Live Converter')
root.minsize(500,200)

# To calculate conversion
def calculate(event):
    enteredValue = e1.get()
    if enteredValue == None:
        e2.config(text='0.0')
    else:
        try:
            new_value = str(round((float(enteredValue) * conversion_value),2))
            e2.config(text=str(new_value))

        except ValueError:
            e2.config(text='0.0')

# Label and Entry Widgets
head_line_1 = Label(root,font = 'calibri 15', text = '1 United States Dollar equals', justify='left')
head_line_1.grid(column = 0,row=0)

head_line_2 = Label(root,font = 'calibri 20 bold', text = str(round(conversion_value,2)) + ' Indian Rupee',justify='left')
head_line_2.grid(column = 0,row=1)

e1 = Entry(root,justify = 'right',width = 10,borderwidth = 5, font = 'calibri 20')
e1.grid(column = 0,row=2)
e1.bind('<Return>',calculate) #Whenever 'Enter' button is pressed, label is modified

e2 = Label(root,justify = 'left',width = 10,borderwidth = 5, font = 'calibri 20', text ='0.0')
e2.grid(column = 0,row=3)

l1 = Label(root,text='United States Dollar',font = 'calibri 20')
l1.grid(column = 1,row=2,sticky='w')

l2 = Label(root,text='Indian Rupee',font = 'calibri 20')
l2.grid(column = 1,row=3,sticky='w')

l3 = Label(root,text='Press Enter to convert',font = 'calibri 15')
l3.grid(column = 0, row = 4)



root.mainloop()
