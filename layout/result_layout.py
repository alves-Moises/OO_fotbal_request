from tkinter import *

def new_window(algo):
    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    azul = (["banana","yolando","acelga","romulo"],["banana","yolando","acelga","romulo"],["banana","yolando","acelga","romulo"])
    mylist = Listbox(root, yscrollcommand=scrollbar.set)
    for line in azul:
        print(line)
        mylist.insert(END, line)

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)

    mainloop()


    print("seila")
