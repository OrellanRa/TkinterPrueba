
# Let's import tkinter + messagebox
import tkinter as tk
from tkinter import messagebox
# You can also try the next sentence:
# import tkinter.messagebox

# Create instance
myWindow = tk.Tk()
myWindow.title("PPS")
myWindow.geometry("800x800")

# Create a function to manage dialog box we are going to generate
def myMessageError():
   messagebox.showinfo("Codigo incorrecto", "Codigo incorrecto, vuelva a digitar")


#def mostrar_opciones():
   
#def aperturacion():
   

# Create a button


#btn1.pack()
#btnA.place(x=75, y=50)

# Launch the application (preventing closing: mainloop method)
myWindow.mainloop()
