# All the libraries # 
from cgitb import text
from contextlib import redirect_stdout
from email.mime import image
from logging import root
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import Style
import webbrowser

# Definitions #
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files","*.txt"),("All File", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Writer by Hetp - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes = [("Text files", "*.txt"),("All Files", "*.*")],
    )

    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Writer by Hetp - {filepath}")

new = 1
url = "https://github.com/Hetp05/Word-Writer/blob/main/README.md"

def openweb():
    webbrowser.open(url,new=new)

# Windows Setings #
window = tk.Tk()
window.title("Word Writer 1.5 by Hetp")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window, font=("Menlo"))


# Buttons & Laylot #
txt_edit.grid(row=0, column=1, sticky="nsew")

# Test #
menubar = tk.Menu(window, foreground='black', activebackground='white', activeforeground='black')  
file = tk.Menu(menubar, tearoff=0, foreground='black')
file.add_command(label="Open", command=open_file)  
file.add_command(label="Save", command=save_file)  
file.add_command(label="Save as", command=save_file)  
file.add_separator()  
file.add_command(label="Exit", command=window.quit)  
menubar.add_cascade(label="File", menu=file)   

help = tk.Menu(menubar, tearoff=0)  
help.add_command(label="About", command=openweb)  
menubar.add_cascade(label="Help", menu=help)

# Etc/ Other #
window.config(menu=menubar)
window.iconbitmap(r'icon-1.ico') 
window.mainloop()