# All the libraries # 
from cgitb import text
from contextlib import redirect_stdout
from email.mime import image
from logging import root
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import Style

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

def add_image():
    global my_image
    my_image = tk.PhotoImage(file="Reference/textedit-icon.png")
    txt_edit.image_create(tk.END, image=my_image)

# Windows Setings #
window = tk.Tk()
window.title("Text Writer by Hetp ")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window, font=("Menlo"))


# Buttons & Laylot #
txt_edit.grid(row=0, column=1, sticky="nsew")

# Test #
menubar = tk.Menu(window, foreground='black', activebackground='white', activeforeground='black')  
file = tk.Menu(menubar, tearoff=0, foreground='black')  
file.add_command(label="New")  
file.add_command(label="Open", command=open_file)  
file.add_command(label="Save")  
file.add_command(label="Save as", command=save_file)
file.add_command(label="Add Image", command=add_image,)    
file.add_separator()  
file.add_command(label="Exit", command=window.quit)  
menubar.add_cascade(label="File", menu=file)  

edit = tk.Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()     
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  

help = tk.Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)

# Etc/ Other #
window.config(menu=menubar)
window.mainloop()