
from tkinter import *


def calculate_bmi():
    try:
        name = entry_name.get()
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        label_result['text'] = f'Hi {name}, your BMI is: {bmi}'
        label_category['text'] = f'Category: you are {category}'
        
    except ValueError:
        "Invalid input"

window = Tk()
window.title('BMI Calculator')
window.iconbitmap('C:/Users/ELCOT/Desktop/Tkinter/icon.ico')


label_name = Label(window, text="Enter your name:",font='arail')
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_weight = Label(window, text="Enter your weight :",font='arail')
label_weight.grid(row=1, column=0, padx=10, pady=10)

entry_weight = Entry(window)
entry_weight.grid(row=1, column=1, padx=10, pady=10)

label_height = Label(window, text="Enter your height :",font='arail')
label_height.grid(row=2, column=0, padx=10, pady=10)

entry_height = Entry(window)
entry_height.grid(row=2, column=1, padx=10, pady=10)

button_calculate = Button(window, text="Calculate BMI",font='arail', command=calculate_bmi,bg='gray')
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = Label(window, text="Your BMI: ",font='arail')
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

label_category = Label(window, text="Category: ",font='arail')
label_category.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()