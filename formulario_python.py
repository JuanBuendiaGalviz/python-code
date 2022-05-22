from tkinter import Tk, Label, Button, Entry, END 


formulario = Tk()

formulario.config(bg="Black")
formulario.geometry('560x388')
formulario.resizable(0,0)
formulario.title("Formulario Python")


frame1  = Frame(formulario), bg="olvie"
frame1.grid(column=0, row=0, sticky="nsew")
frame2 = Frame(formulario, bg="olvive")
frame2.grid(column=1, row=0, sticky="nsew")


nombre = Label(frame1, text="Nombre" width="10px".grid(column=0, row=0)


formulario.mainloop()
