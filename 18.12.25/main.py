from tkinter import *

window = Tk() # Create window
window.title("Example title") # Add title
window.geometry('400x250')

lbl = Label(window, text='Hi') # Create text
lbl.grid(column=0, row=0) # Connect/Render to window

window.mainloop() # Start window
