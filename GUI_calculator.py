from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title("Calculator")
GUI.geometry("500x500")

L = Label(GUI, text="calculator", font=("Ansana New", 40, "bold"))
L.pack(pady=5)

E1 = Entry(GUI, font=("Angsana New", 20))
E1.pack(pady=5)

B1 = Button(GUI, text="Calculator")
B1.pack(pady=10)


GUI.mainloop()
