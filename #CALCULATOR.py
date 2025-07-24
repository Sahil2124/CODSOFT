#Task -1  SIMPLE CALCULATOR

import tkinter as tk
window = tk.Tk()
window.title("Sahil's calcy")

def clicked():
    try:
        num1 = float(usrentry.get())
        num2 = float(passentry.get())
    except ValueError:
        result_label.config(text ="Please enter a valid number .")
        return
    operation1 = operation.get()
    if operation1 == "+":
         result = num1 + num2
    elif operation1== "*":
        result = num1*num2
    elif operation1 == "-":
        result = num1 - num2
    elif operation1 =="/":
        if num2 == 0:
            result_label.config(text ="Cannnot divided by zero.")
            return
        result = num1/num2
    else:
        result_label.config(text = " Please select an operation. ")
        return
    result_label.config(text = f"Result: {result}")

usrnm_label = tk.Label(window,text = "number 1")
usrnm_label.grid(row = 0,column = 0, padx = 10 , pady =5)

usrentry = tk.Entry(window)
usrentry.grid(row =0,column = 1,padx = 10,pady =5)

passw_label =tk.Label(window, text ="number 2")
passw_label.grid(row  =1 ,column =0,padx = 10,pady =5)

passentry=tk.Entry(window)
passentry.grid(row = 1,column = 1,padx = 10,pady= 5)

operation = tk.StringVar()
tk.Radiobutton(window,text="add" , value = "+",variable=operation).grid(row = 4,column = 0)
tk.Radiobutton(window,text="mul" , value = "*",variable=operation).grid(row = 4,column =1)
tk.Radiobutton(window,text="sub" , value = "-",variable=operation).grid(row = 4,column=2)
tk.Radiobutton(window,text="div" , value = "/",variable=operation).grid(row = 4,column=3)



button = tk.Button(window,text = "Submit", command = clicked)
button.grid(row=2,column = 1 ,padx =10,pady=5)

result_label = tk.Label(window,text = "Chose operation")
result_label.grid(row =3,column = 0 ,padx=2,pady=5)
window.mainloop()
