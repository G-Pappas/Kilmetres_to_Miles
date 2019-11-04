"""
Kilometres to Miles converter GUI, using tkinter
"""

from tkinter import *

window=Tk() #create an empy window
window.resizable(0, 0) # set the window to a constant size
window.title("Bookcase v0.8")

#Convertion Function
def km_to_miles():
    t1.delete('1.0',END)#clear text in case user did not press clear button
    try:# Check if user addet text
        float(e1_value.get())
    except ValueError:
        t1.insert(END,"Please enter a number")
    else:
        if float(e1_value.get())<0:# Check if value is greater thatn 0
            t1.insert(END,"Value must be greater than 0")
        elif float(e1_value.get()) >= 0:#make the convertion
            miles=float(e1_value.get())/1.609
            t1.insert(END,miles)


#Clear boxes function
def clear_boxes():
    t1.delete('1.0',END)
    e1.delete(0,END)

l1=Label(window, text="Please enter kilometres: ")
l1.grid(row=0,column=0)

l2=Label(window, text="Miles:")
l2.grid(row=0, column=2)

b1=Button(window, text="Convert", command=km_to_miles)
b1.grid(row=1,column=1)

b2=Button(window, text="Clear", command=clear_boxes)
b2.grid(row=2,column=1)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value, width=30)
e1.grid(row=1,column=0)

t1=Text(window, height=1,width=30)
t1.grid(row=1,column=2)



window.mainloop() #keep window open
