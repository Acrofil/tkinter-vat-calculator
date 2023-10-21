import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

def main():  
    
    sum_label = tb.Label(text="Sum", font=('Helvetica', 20), bootstyle="default")
    vat_label = tb.Label(text="VAT in %", font=("Helvetica", 20), bootstyle="default")
    
    sum_label.grid(row=3, column=0, pady=55)
    vat_label.grid(row=4, column=0, pady=0)
    
    sum_entry.grid(row=3, column=1, sticky="ew")
    vat_entry.grid(row=4, column=1, sticky="ew")
    
    top_label = tb.Label(text="Calculate VAT", font=("Helvetica", 20), bootstyle="warning")
    left_label = tb.Label(text="Inclusive/Exclusive", font=("Helvetica", 20), bootstyle="warning")
    
    top_label.grid(row=1, column=1, pady=25)
    left_label.grid(row=2, column=1)
    
    the_sum_includes = tb.Label(text="Action:", font=("Helvetica", 20), bootstyle="default")
    
    include_vat_style = tb.Style()
    include_vat_style.configure("success.TCheckbutton", font=("Helvetica", 16))
    includes_vat = tb.Checkbutton(bootstyle="success, round-toggle", 
                                text="Exclude VAT", 
                                variable=var_include_vat, 
                                onvalue=1, 
                                offvalue=0,
                                style="success.TCheckbutton")
    
    
    vat_not_included_style = tb.Style()
    vat_not_included_style.configure("success.TCheckbutton", font=("Helvetica", 16))
    vat_not_included = tb.Checkbutton(bootstyle="succes, round-toggle", 
                                        text='Add VAT',
                                        variable=var_not_include_vat,
                                        onvalue=1,
                                        offvalue=0,
                                        style="success.TCheckbutton"
                                        )
    
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

def no_str_input():
    clear_entrys()
    
    warn_input = tb.Label(text="Use only numbers!", font=("Helvetica", 18), bootstyle="danger")
    warn_input.grid(row=7, column=1, pady=50)
   
def calculate_vat_included(s_value, v_value):
    s_value = int(s_value)
    v_value = int(v_value)
    
    sum_without_vat = round((s_value / (v_value + 100) * 100), 2)
    vat = round(s_value - sum_without_vat, 2)
    
    return [sum_without_vat, vat]
  
def calculate_vat_excluded(s_value, v_value):
    s_value = int(s_value)
    v_value = int(v_value)
    
    sum_with_vat = round((s_value / 100) * (v_value + 100), 2 )
    vat = round(sum_with_vat - s_value, 2)
    
    return [sum_with_vat, vat]

def check_operation():
    
    try:
        sum_entry_value = int(sum_entry.get())
        vat_entry_value = int(vat_entry.get())
    except: 
        ValueError(no_str_input())
    
    
    if var_include_vat.get() == 1:
        exclude_vat = calculate_vat_included(sum_entry_value, vat_entry_value)
        display_result(exclude_vat, "exclude")
    elif var_not_include_vat.get() == 1:
        add_vat = calculate_vat_excluded(sum_entry_value, vat_entry_value)
        display_result(add_vat, "add")

    else:
        warn_text = tb.Label(text="Please select VAT option", bootstyle="warning", font=("Helvetica", 15))        
        warn_text.grid(row=7, column=1)

def display_result(result, action):
    
    amount = tb.Label(text="Amount", font=("Helvetica", 18), bootstyle="default")
    net_amount = tb.Label(text="Net Amount", font=("Helvetica", 18), bootstyle="default")
    gross_amount = tb.Label(text="Gross Amount", font=("Helvetica", 18), bootstyle="default")
    vat_added = tb.Label(text="VAT Added", font=("Helvetica", 18), bootstyle="default")
    vat_excluded = tb.Label(text="VAT Excluded", font=("Helvetica", 18), bootstyle="default")
    
    if action == "exclude":
        amount.grid(row=7, column=0, pady=50)
        vat_excluded.grid(row=7, column=1, pady=50)
        net_amount.grid(row=7, column=2, pady=50)
        show_result(result)        
    
    elif action == "add":
        amount.grid(row=7, column=0, pady=50)
        vat_added.grid(row=7, column=1, pady=50)
        gross_amount.grid(row=7, column=2, pady=50)
        show_result(result)

def show_result(r):
    initial_value = tb.Label(text=sum_entry.get(), font=("Helvetica", 18), bootstyle="warning")
    vat_result = tb.Label(text=str(r[1]), font=("Helvetica", 18), bootstyle="warning")
    value_result = tb.Label(text=str(r[0]), font=("Helvetica", 18), bootstyle="warning")
    
    initial_value.grid(row=8, column=0, pady=50)
    vat_result.grid(row=8, column=1, pady=50)
    value_result.grid(row=8, column=2, pady=50)
        
if __name__ == "__main__":
    
    window = tb.Window(themename="darkly")
    window.title("VAT Calculator")
    window.geometry("600x800")

    window.grid_columnconfigure((0,2), weight=1)

    # All entries
    sum_entry = tb.Entry()
    vat_entry = tb.Entry()

    #Style checkbuttons
    var_include_vat = tb.IntVar()
    var_not_include_vat = tb.IntVar()
    
    main()
    