# import necessary modules and libraries

import ttkbootstrap as tb
import math
from ttkbootstrap.constants import *
from button_class import Button
from tkinter import messagebox

root = tb.Window(themename='cyborg')
root.title('Calculator')
root.geometry('625x500')


# Create click function
def on_click(text):
    if text == '=':
        try:
            result = eval(field.get())
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Expression: ' + str(e))
    elif text == 'Clear':
        field.delete(0, tb.END)
    elif text == 'Delete':
        field.delete(len(field.get())-1)
    elif text == 'sqrt':
        try:
            result = math.sqrt(float(field.get()))
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for sqrt: ' + str(e))
    elif text == 'square':
        try:
            result = float(field.get()) ** 2
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for square: ' + str(e))
    elif text == 'cube':
        try:
            result = float(field.get()) ** 3
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for cube: ' + str(e))
    elif text == 'log':
        try:
            result = math.log(float(field.get()))
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for log: ' + str(e))
    elif text == 'sin':
        try:
            result = math.sin(math.radians(float(field.get())))
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for sin: ' + str(e))
    elif text == 'cos':
        try:
            result = math.cos(math.radians(float(field.get())))
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for cos: ' + str(e))
    elif text == 'asin':
        try:
            result = math.degrees(math.asin(float(field.get())))
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for asin: ' + str(e))
    elif text == 'acos':
        try:
            result = math.degrees(math.acos(float(field.get())))
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for acos: ' + str(e))
    elif text == 'exp':
        try:
            result = math.exp(float(field.get()))
            field.delete(0, tb.END)
            field.insert(0, str(result))
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Input for exp: ' + str(e))
    else:
        current_input = field.get()
        field.delete(0, tb.END)
        field.insert(0, current_input + text)


# Create input field
field = tb.Entry(root, width=50, bootstyle=PRIMARY, font=('Times New Roman', 18))
field.grid(columnspan=4, padx=10, pady=10, sticky='nsew')

# Buttons for numbers
button9 = Button(root, '9', 1, 0, 20, 10, 10, on_click)
button8 = Button(root, '8', 1, 1, 20, 10, 10, on_click)
button7 = Button(root, '7', 1, 2, 20, 10, 10, on_click)
button6 = Button(root, '6', 2, 0, 20, 10, 10, on_click)
button5 = Button(root, '5', 2, 1, 20, 10, 10, on_click)
button4 = Button(root, '4', 2, 2, 20, 10, 10, on_click)
button3 = Button(root, '3', 3, 0, 20, 10, 10, on_click)
button2 = Button(root, '2', 3, 1, 20, 10, 10, on_click)
button1 = Button(root, '1', 3, 2, 20, 10, 10, on_click)
button0 = Button(root, '0', 4, 0, 20, 10, 10, on_click)

# Operator symbols
add = Button(root, '+', 1, 3, 20, 10, 10, on_click)
subtract = Button(root, '-', 2, 3, 20, 10, 10, on_click)
multiply = Button(root, 'X', 3, 3, 20, 10, 10, on_click)
divide = Button(root, '/', 4, 3, 20, 10, 10, on_click)
square_root = Button(root, 'sqrt', 6, 0, 20, 10, 10, on_click)
square = Button(root, 'square', 6, 1, 20, 10, 10, on_click)
cube = Button(root, 'cube', 6, 2, 20, 10, 10, on_click)
log = Button(root, 'log', 6, 3, 20, 10, 10, on_click)
sin = Button(root, 'sin', 7, 0, 20, 10, 10, on_click)
cos = Button(root, 'cos', 7, 1, 20, 10, 10, on_click)
asin = Button(root, 'asin', 7, 2, 20, 10, 10, on_click)
acos = Button(root, 'acos', 7, 3, 20, 10, 10, on_click)
exp = Button(root, 'exp', 8, 0, 20, 10, 10, on_click)

# Equal
equal = Button(root, '=', 4, 2, 20, 10, 10, on_click)

# Decimal
dot_decimal = Button(root, '.', 4, 1, 20, 10, 10, on_click)

# Bracket
front_bracket = Button(root, '(', 5, 0, 20, 10, 10, on_click)
back_bracket = Button(root, ')', 5, 1, 20, 10, 10, on_click)

# Clear
clear = Button(root, 'Clear', 5, 2, 20, 10, 10, on_click)

# Delete
delete = Button(root, 'Delete', 5, 3, 20, 10, 10, on_click)

root.mainloop()
