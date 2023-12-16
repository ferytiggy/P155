from tkinter import*
import random

root = Tk()
root.geometry("600x400")
root.title("diccionario")

dictionary={"color":["green", "blue", "red", "yellow", "orange"]}

def background_change ():
    aleatorio = random.randint(0,4)
    root.configure(background=dictionary["color"][aleatorio])
    
color = Button(root, text="colores en ing", command=background_change)
color.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()


