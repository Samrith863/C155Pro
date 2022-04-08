from tkinter import *
import random
root=Tk()
root.title("Random Colors Of The Root Window")
root.geometry("4004x400")
dictionary_color={'Color':['red','orange','yellow','green','cyan','purple','pink','gold']}

def changeRootWindowColor():
    random_no=random.randint(0,7)
    print(dictionary_color['Color'][random_no])
    root.configure(background=dictionary_color['Color'][random_no])



btn=Button(root,text="Change Root Window Color",bg="black",fg="white",command=changeRootWindowColor)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
