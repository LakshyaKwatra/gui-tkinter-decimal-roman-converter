
import tkinter as tk
import math

def romanToInt(rom): 
    value = {
        'H': 10000,
        'G': 5000,
        'M': 1000, 
        'D': 500, 
        'C': 100, 
        'L': 50, 
        'X': 10, 
        'V': 5, 
        'I': 1
    }  
    p = 0
    ans = 0 
    n = len(rom)  
    for i in range(n-1,-1,-1):
        romi = rom[i].upper()
        if romi not in value:
            return "Not a proper roman numeral!"
        if value[romi] >= p: 
            ans += value[romi]    
        else: 
            ans -= value[romi]  
        p = value[romi] 
  
    return ans 

  
def intToRoman(A): 
    romansDict = { 
            1: "I", 
            5: "V", 
            10: "X", 
            50: "L", 
            100: "C", 
            500: "D", 
            1000: "M", 
            5000: "G", 
            10000: "H"
        } 
  
    div = 1
    while A >= div: 
        div *= 10
  
    div /= 10
  
    res = "" 
  
    while A: 
        lastNum = int(A / div) 
  
        if lastNum <= 3: 
            res += (romansDict[div] * lastNum) 
        elif lastNum == 4: 
            res += (romansDict[div] + 
                          romansDict[div * 5]) 
        elif 5 <= lastNum <= 8: 
            res += (romansDict[div * 5] + 
            (romansDict[div] * (lastNum - 5))) 
        elif lastNum == 9: 
            res += (romansDict[div] +
                         romansDict[div * 10]) 
  
        A = math.floor(A % div) 
        div /= 10
          
    return res
    
fields = ('Roman Numeral', 'Integer')

import tkinter as tk
from functools import partial

# global variable
tempVal = "Celsius"


# getting drop down value
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp


# the main conversion
def call_convert(rlabel1, inputn):
    tem = inputn.get()
    if tempVal == 'Integer To Roman':
        if(not tem.isnumeric()):
            rlabel1.config(text= "Not a proper decimal!")
            return
        if(float(tem) == 0):
            rlabel1.config(text= "-")
            return
        if(float(tem) > 10000):
            rlabel1.config(text= "Number should be <= 10000")
            return
        f = intToRoman(float(tem))
        rlabel1.config(text= f)
    if tempVal == 'Roman To Integer':
        if(tem.isnumeric()):
            rlabel1.config(text= "Not a proper Roman numeral!")
            return
        c = romanToInt(tem)
        rlabel1.config(text=str(c))
    return


# app window configuration and UI
root = tk.Tk()
root.geometry('450x150+100+200')
root.title('Roman/Integer Converter')
root.configure(background='#3D576E')
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=10)
root.grid_rowconfigure(1, weight=10)

numberInput = tk.StringVar()
var = tk.StringVar()

# label and entry field
input_label = tk.Label(root, text="Enter Integer/Roman Number:", background='#3D576E', foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1)
input_entry.grid(row=1,column = 1)

# result label's for showing the other two temperatures
result_label1 = tk.Label(root, background='#3D576E', foreground="#FFFFFF")
result_label1.grid(row=4, columnspan=4, padx = 40,pady = 4)

# drop down initalization and setup
dropDownList = ["Integer To Roman", "Roman To Integer"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set('Select Operation')
dropdown.grid(row=1, column=3)
dropdown.config(background='#09A3BA', foreground="#FFFFFF")
dropdown["menu"].config(background='#000000', foreground="#FFFFFF")

# button click
call_convert = partial(call_convert, result_label1, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
result_button.grid(row=2, columnspan=4)

root.mainloop()
