import tkinter as tk
from tkinter import ttk

ELEMENTS = [
    ["a", "∀"],
    ["t", "∆"],
    ["f", "£"],
    ["d", "⫏"],
    ["s", "⪙"],
    ["g", "∂"],
    ["h", "⊦"],
    ["b", "₿"],
    ["m", "⁐"],
    ["n", "≌"],
    ["o", "⊚"],
    ["q", "⇴"],
    ["x", "⟚"],
    ["c", "⋲"],
    ["l", "⤡"],
    ["i", "↑"],
    ["p", "∮"],
    ["w", "ш"],
    ["u", "Ґ"],
    ["e", "ε"]
]

def find_symbol(symbol):
    for element in ELEMENTS:
        if symbol == element[0]:
            return element[1]
    return symbol

def convert_text(text):
    text = text.lower()
    new_text = str()
    for symbol in text:
        new_text += find_symbol(symbol)
    return new_text

def get_text():
    text = entry.get()
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result = convert_text(text)
    result_entry.insert(0, result)
    result_entry.config(state="readonly")

# Root Init
root = tk.Tk()
root.title("App")

# Text
entry = ttk.Entry(root, width=40)
entry.pack(pady=10)

# Button
button = ttk.Button(root, text="Convert", command=get_text)
button.pack(pady=5)

# Result window
result_entry = ttk.Entry(root, width=40)
result_entry.pack(pady=10)
result_entry.config(state="readonly")

root.mainloop()