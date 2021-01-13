from time import strftime

from GUI import lbl

def time(): 
    """Display of the current time"""
    string = strftime('%H:%M:%S %p \n %d.%m.%Y')
    lbl.config(text = string) 
    lbl.after(1000, time)