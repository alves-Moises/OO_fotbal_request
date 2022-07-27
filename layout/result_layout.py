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

def season_result(data):

    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    season_list = Listbox(root, yscrollcommand=scrollbar.set)
    

    for season in data:

        season_list.insert(END, str(f'Id: {season.get_id()}'))
        season_list.insert(END, str(f'Id da tempoorada: {season.get_league_id()}'))
        season_list.insert(END, str(f'Nome: {season.get_name()}'))
        season_list.insert(END, str(f'Id da oartuda atual atual: {season.get_current_round_id()}'))
        season_list.insert(END, str(f'Estágio atual: {season.get_current_stage()}'))
        season_list.insert(END, str(''))


    season_list.pack(side=LEFT, fill=BOTH)

    height = 60 if len(data) > 10 else (len(data) * 7)
    season_list.config(width=100, height=height)
    scrollbar.config(command=season_list.yview)

    mainloop()

def league_result(data):

    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(root, yscrollcommand=scrollbar.set)

    for league in data:

        mylist.insert(END, str(f'Id: {league.get_id()}'))
        mylist.insert(END, str(f'Nome: {league.get_name()}'))
        mylist.insert(END, str(f'Está ativo? {league.is_active()}'))
        mylist.insert(END, str(f'Tipo de liga: {league.get_type()}'))
        # mylist.insert(END, str(f'Id do país: {league.country_id()}'))
        mylist.insert(END, str(f''))



    mylist.pack(side=LEFT, fill=BOTH)
    height= 60 if (len(data) > 12) else (len(data) * 6)
    mylist.config(width=80, height= height)
    scrollbar.config(command=mylist.yview)

    mainloop()