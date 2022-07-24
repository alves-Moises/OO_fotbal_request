from tkinter import *
'''
my_image = PhotoImage(file="fundo.png")
button = Button(image=my_image, highlightthickness=0)
'''
#######################

my_image = "assets/fundo_game.png"



window = Tk()
window.title("Go Idiomas FlashCards challengermode - by Marco Aurélio Menezes")
BACKGROUND_COLOR = "#B1DDC6"
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
##########################################################
canvas = Canvas(height=580, width=720)
card_front_image = PhotoImage(file=my_image)
canvas.create_image(580, 720, image=card_front_image)

oIdioma = canvas.create_text(400, 70, text="inglês", font=("Arial", 15, "italic"), fill="#000000")
aPalavra = canvas.create_text(400, 150, text='Seja bem vindos', font=("Arial", 70, "bold"), fill="#000000")
placar = canvas.create_text(700, 80, text='pontos', font=("Arial", 15, "bold"), fill="#9191FF")


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
##########################################################
# Buttons

known2_button = Button(text= "batata",font=("Arial", 30, "italic"), width=15, height=1)#, command=pass)#Button(image= check2_image,highlightthickness=0)#,text="Unknown", width=10)#, command=unknown)
# known_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.create_text(400, 263, text="palavra", font=("Arial", 60, "italic"), fill="#000000")
known2_button.grid(row=2, column=1)

# canvas.pack()

# card_back_image = PhotoImage(file="img/card_back.png")
# window.geometry("500x500")











window.mainloop()