from tkinter import *

import controllers.player_controller
import layout.result_layout

#importaçoes de dados da API



# funçoes de interface



def request_season():
    season = controllers.season_controller.search_season()
   
    layout.result_layout.season_result(season)

def request_player_by_name():
    player_name = input_field.get()

    #getting data players
    data_players = controllers.player_controller.search_player_by_name(player_name)
    
    if not data_players: 
        print("Jogador não encontrado")

        return
    layout.result_layout.player_result(data_players)

def request_player_by_id():
    player_name = input_field.get()

    data_player = controllers.player_controller.search_player_by_id(player_name)
    if not data_player:
        print("Jogador não encontrado") 
        
        return

    layout.result_layout.player_result_id(data_player)



   



# montando a janela
window = Tk()
window.title("Super Star Futebol - by Rondinelly Martins")

BACKGROUND_COLOR = "#B1DDC6"
window.config(pady=10,padx=10, bg=BACKGROUND_COLOR)


# imagens de fundo

# my_image = "assets/fundo_game.png"

# imagem do topo
canvas = Canvas(height=720, width=580)
card_front_image = PhotoImage(file="assets/fundoa1.png")
canvas.create_image(290, 130, image=card_front_image)

# imagem do rodapé
card_front_image2 = PhotoImage(file="assets/fundoc1.png")
canvas.create_image(290, 520, image=card_front_image2)

# cor de fundo
BACKGROUND_COLOR = "#270c39"
window.config( bg=BACKGROUND_COLOR)



# entradas de dados #
input_field = Entry(width=30)
input_field.grid(row=8,column=1, columnspan=2)
input_field.config(bg="#FFFFFF", fg="#000000",highlightthickness=0, font=("Arial", 15, "bold"))
input_field.insert(0,"")


#botoes



button_player = Button(text="Jogador", width=10, command=request_player_by_name)
button_player.grid(row=10,column=1)

button_player2 = Button(text="jogador ID", width=10, command=request_player_by_id)
button_player2.grid(row=10,column=2)

button_player3 = Button(text="temporada", width=10, command=request_season)
button_player3.grid(row=10,column=3)

button_player4 = Button(text="time por País", width=10, command='')
button_player4.grid(row=11,column=1)



#####


button_player5 = Button(text="aaaaaaaa", width=10, command=request_season)
button_player5.grid(row=11,column=2)

button_player6 = Button(text="Liga", width=10, command=request_league)
button_player6.grid(row=11,column=3)

# montando a janela
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=16, rowspan=30)


window.mainloop()