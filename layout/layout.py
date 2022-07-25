from tkinter import *

import controllers.player_controller
import requests

#importaçoes de dados da API



# funçoes de interface





def placar_visual_jogador(dados):
    placar = canvas.create_text(100, 370, 
                                text='aaasdasd\nasdasd\nasdasd\n' * 40,
                                font=("Arial", 15, "bold"), fill="#9191FF", anchor=W)

def request_player():
    player_name = input_field.get()

    data_players = controllers.player_controller.search_player(player_name)
    # print(data_players)
    
    #tratamento final
    # temp_list = list()

    
    # for data in data_players:
    #     temp_list.append(data.name)
    #     temp_list.append('\n')

    # print(temp_list)
    # placar_visual_jogador(temp_list)



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
input_field = Entry(width=35)
input_field.grid(row=7,column=1,columnspan=2, rowspan=2)
input_field.config(bg="#FFFFFF", fg="#000000",highlightthickness=0, font=("Arial", 15, "bold"))
input_field.insert(0,"")


#botoes


button_player = Button(text="Jogador", width=10, command=request_player)
button_player.grid(row=11,column=0)

button_player2 = Button(text="jogador ID", width=10, command=request_player)
button_player2.grid(row=11,column=1)

button_player3 = Button(text="league", width=10, command=request_player)
button_player3.grid(row=11,column=2)

button_player4 = Button(text="time por País", width=10, command=request_player)
button_player4.grid(row=11,column=3)

# montando a janela
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=16, rowspan=30)


window.mainloop()