
from tkinter import *





window = Tk()
window.title("Go Idiomas FlashCards challengermode - by Marco Aurélio Menezes")
BACKGROUND_COLOR = "#B1DDC6"
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
##########################################################

canvas = Canvas(height=300, width=800)
card_front_image = PhotoImage(file="img/brancogrande.png")
canvas.create_image(400, 170, image=card_front_image)
'''
oIdioma = canvas.create_text(400, 70, text="inglês", font=("Arial", 15, "italic"), fill="#000000")
aPalavra = canvas.create_text(400, 150, text='Seja bem vindos', font=("Arial", 70, "bold"), fill="#000000")
placar = canvas.create_text(700, 80, text='pontos', font=("Arial", 15, "bold"), fill="#9191FF")


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
##########################################################
# Buttons
falar_button = Button(text='falar',font=("Arial", 10, "italic"), width=5, height=1, command=falar)#, command=unknown)
falar_button.grid(row=0, column=1)
# Button 1
#cross_image = PhotoImage(file="img/pequenobranco.png")
unknown_button = Button(text=item1,font=("Arial", 30, "italic"), width=15, height=1)#Button(image= cross_image,highlightthickness=0)#,text="Unknown", width=10)#, command=unknown)

# unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_button.grid(row=1, column=0)

# Button 2

check_image = PhotoImage(file="img/right.png"))#, command=unknown)
# known_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_button.grid(row=1, column=1)

# extra bootom
#botton1

unknown2_button = Button(text=item3,font=("Arial", 30, "italic"), width=15, height=1, )#,text="Unknown", width=10)#, command=unknown)
# unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown2_button.grid(row=2, column=0)

# Button 2

known2_button = Button(text= item4,font=("Arial", 30, "italic"), width=15, height=1, )#Button(image= check2_image,highlightthickness=0)#,text="Unknown", width=10)#, command=unknown)
# known_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.create_text(400, 263, text="palavra", font=("Arial", 60, "italic"), fill="#000000")
known2_button.grid(row=2, column=1)

# canvas.pack()

# card_back_image = PhotoImage(file="img/card_back.png")
# window.geometry("500x500")









'''

window.mainloop()










