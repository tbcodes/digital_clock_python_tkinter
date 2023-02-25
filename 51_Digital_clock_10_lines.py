import tkinter as tk
from time import strftime

my_window = tk.Tk()
my_window.title('Digital clock')
my_window.geometry('250x100')

def time_clock():
    display_time = strftime('%H:%M:%S %p')
    label.config(text = display_time)
    label.after(1000, time_clock)

label = tk.Label(my_window, font=('Arial', 24), background = 'black', foreground = 'orange')
label.pack(anchor = 'center', pady = 30)

time_clock()
my_window.mainloop()
