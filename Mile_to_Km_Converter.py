from tkinter import *

def mile_to_Km():
    input = float(mile_entry.get())
    ouput = input*1.609
    op_text.config(text = ouput)

window = Tk()
window.title("Mile to Km Converter")
window.config(padx = 20, pady = 20)

mile_entry = Entry(width=10)
mile_entry.grid(column=4, row = 0)


miles_label = Label(text = "Miles")
miles_label.grid(column = 5, row =0)

text = Label(text = "is equal to ")
text.grid(column = 3, row =1)

op_text = Label(text = " 0 ")
op_text.grid(column = 4, row = 1)

km_label = Label(text = "Km")
km_label.grid(column= 5, row= 1)


calculate_button = Button(text = "Calculate", command= mile_to_Km)
calculate_button.grid(column =4, row =2 )


window.mainloop()