import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

window = tb.Window(themename="darkly")
window.title("VAT Calculator")
window.geometry("600x600")

window.grid_columnconfigure((0,2), weight=1)

sum_label = tb.Label(text="Sum", font=('Helvetica', 20), bootstyle="default")
sum_entry = tb.Entry()

vat_label = tb.Label(text="VAT in %", font=("Helvetica", 20), bootstyle="default")
vat_entry = tb.Entry()

sum_label.grid(row=3, column=0, pady=55)
sum_entry.grid(row=3, column=1, sticky="ew")

vat_label.grid(row=4, column=0, pady=0)
vat_entry.grid(row=4, column=1, sticky="ew")

#Style checkbuttons
include_vat_style = tb.Style()
include_vat_style.configure("success.TCheckbutton", font=("Helvetica", 16))

var_include_vat = tb.IntVar()
includes_vat = tb.Checkbutton(bootstyle="success, round-toggle", 
                                text="VAT included", 
                                variable=var_include_vat, 
                                onvalue=1, 
                                offvalue=0,
                                style="success.TCheckbutton")

vat_not_included_style = tb.Style()
vat_not_included_style.configure("success.TCheckbutton", font=("Helvetica", 16))

var_not_include_vat = tb.IntVar()
vat_not_included = tb.Checkbutton(bootstyle="succes, round-toggle", 
                                    text='VAT not included',
                                    variable=var_not_include_vat,
                                    onvalue=1,
                                    offvalue=0,
                                    style="success.TCheckbutton"
                                    )


def main():
    
    top_label = tb.Label(text="Calculate VAT", font=("Helvetica", 20), bootstyle="warning")
    left_label = tb.Label(text="Inclusive/Exclusive", font=("Helvetica", 20), bootstyle="warning")
    
    top_label.grid(row=1, column=1, pady=25)
    left_label.grid(row=2, column=1)
    
    the_sum_includes = tb.Label(text="The sum has", font=("Helvetica", 20), bootstyle="default")
    
    #Position on the work screen
    the_sum_includes.grid(row=5, column=0, pady=50)
    includes_vat.grid(row=5, column=1)
    vat_not_included.grid(row=5, column=2)
    
        
    #Style buttons
    calculate_style = tb.Style()
    calculate_style.configure('info.TButton', font=('Helvetica', 18))
    
    clear_style = tb.Style()
    clear_style.configure("danger.TButton", font=("Helvetica", 18))
    
    
    calculate_button = tb.Button(text="Calculate", bootstyle="info", style="info.TButton", command=check_operation)
    other_action = tb.Label(text="OR", font=("Helvetica", 20), bootstyle="default")
    clear_button = tb.Button(text="Clear", bootstyle="danger", style="danger.TButton", command=clear_entrys)
    
    calculate_button.grid(row=6, column=0)
    other_action.grid(row=6, column=1)
    clear_button.grid(row=6, column=2)
    
    window.mainloop()

def clear_entrys():
    sum_entry.delete(0, 'end')
    vat_entry.delete(0, 'end')
   


def calculate_vat_included(s_value, v_value):
    print(s_value)
    print(v_value)


def calculate_vat_excluded():
    ...

def check_operation():
    sum_entry_value = sum_entry.get()
    vat_entry_value = vat_entry.get()
    
    if var_include_vat.get() == 1:
        calculate_vat_included(sum_entry_value, vat_entry_value)
    elif var_not_include_vat.get() == 1:
        calculate_vat_excluded(sum_entry_value, vat_entry_value)
    
    else:
        warn_text = tb.Label(text="Please select VAT option", bootstyle="warning", font=("Helvetica", 15))
        
        warn_text.grid(row=7, column=1)

if __name__ == "__main__":
    
    main()
    