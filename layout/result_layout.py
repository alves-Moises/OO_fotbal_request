from tkinter import *

def player_result(data):

    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(root, yscrollcommand=scrollbar.set)


    for player in data:

        mylist.insert(END, str(f"Id: {player.get_id()}"))
        mylist.insert(END, str(f"Nome: {player.get_name()}"))
        mylist.insert(END, str(f"Nacionalidade: {player.get_nationality()}"))
        mylist.insert(END, str(f"Nascimento: {player.get_birthdate()}"))
        mylist.insert(END, str(f'Idade: {player.get_age()}'))
        mylist.insert(END, '')


    mylist.pack(side=LEFT, fill=BOTH)
    height= 60 if (len(data) > 12) else (len(data) * 6)
    mylist.config(width=80, height= height)
    scrollbar.config(command=mylist.yview)

   
    mainloop()

def player_result_id(data):

    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    info = Listbox(root, yscrollcommand=scrollbar.set)

    info.insert(END, str(f'Id: {data.get_id()}'))
    info.insert(END, str(f'Nome: {data.get_name()}'))
    info.insert(END, str(f'Nacionalidade: {data.get_nationality()}'))
    info.insert(END, str(f'Nascimento: {data.get_birthdate()}'))
    info.insert(END, str(f'Idade: {data.get_age()}'))
    info.insert(END, str(f''))
    

    info.pack(side=LEFT, fill=BOTH)
    info.config(width=70, height= 10)
    scrollbar.config(command=info.yview)

   
    mainloop()


