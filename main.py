from tkinter import *
import random
import tkinter.messagebox
import os

root = Tk()



class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    def init_window(self):
  
        self.master.title("Minesweeper")

        self.pack(fill=BOTH, expand=1)
        EjeX = 30

        EjeY = 30

        campo = []
        botones = ["boton_" + str(x) for x in range (EjeX * EjeY)]
        bombas = []
        posX_botones = []
        for x in range(EjeY):
            for y in range(EjeX):
                posX_botones.append(y)
        posY_botones = [x for x in range(EjeY) for a in range(EjeX)]

        for x in range(EjeX * EjeY):
            bomba = random.randrange(7)
            if bomba == 0:
                bomb = Button(text="     ", command= lambda a = posX_botones[x], b = posY_botones[x], casilla = x : click1_b(a, b, casilla))
                bomb.place(x = 25 * posX_botones[x], y = 25 * posY_botones[x])
                bomb.bind("<Button-3>", lambda a, casilla = x: click2(casilla))
                botones[x] = bomb
                bombas.append(x)
            else:
                campo.append(x)
                field = Button(text="     ", command= lambda a = posX_botones[x], b = posY_botones[x], casilla = x : click1_a(casilla, EjeX, EjeY, bombas, posX_botones, posY_botones))
                field.place(x = 25 * posX_botones[x], y = 25 * posY_botones[x])
                field.bind("<Button-3>", lambda a, casilla = x: click2(casilla))
                botones[x] = field

        #
        def buscarbomba(casilla, EjeX, EjeY, bombas, posX_botones, posY_botones):
            number = 0
            for x in bombas:
                if posX_botones[casilla] > 0 and posY_botones[casilla] > 0:
                    if x == casilla - EjeX - 1:
                        number = number + 1
                if posY_botones[casilla] > 0:
                    if x == casilla - EjeX:
                        number = number + 1
                if posX_botones[casilla] < EjeX - 1 and posY_botones[casilla] > 0:
                    if x == casilla - EjeX + 1:
                        number = number + 1   
                if posX_botones[casilla] > 0:
                    if x == casilla - 1:
                        number = number + 1
                if posX_botones[casilla] < EjeX - 1:
                    if x == casilla + 1:
                        number = number + 1  
                if posX_botones[casilla] > 0 and posY_botones[casilla] < EjeY - 1:
                    if x == casilla + EjeX - 1:
                        number = number + 1
                if posY_botones[casilla] < EjeY - 1:     
                    if x == casilla + EjeX:
                        number = number + 1
                if posX_botones[casilla] < EjeX - 1 and posY_botones[casilla] < EjeY - 1:
                    if x == casilla + EjeX + 1:
                        number = number + 1
            return number 

        # What the program does when the user left clicks a box
        def click1_a(casilla, EjeX, EjeY, bombas, posX_botones, posY_botones):
            if checkgameover() == False:
                number = buscarbomba(casilla, EjeX, EjeY, bombas, posX_botones, posY_botones)                     
                if number == 0:
                    botones[casilla]["text"] = "     "
                    botones[casilla]["state"] = DISABLED
                    botones[casilla]["relief"] = SUNKEN
                    if posX_botones[casilla] > 0 and posY_botones[casilla] > 0 and botones[casilla - EjeX - 1]["state"] == NORMAL:
                        click1_a(casilla - EjeX - 1, EjeX, EjeY, bombas, posX_botones, posY_botones)
                    if posY_botones[casilla] > 0 and botones[casilla - EjeX]["state"] == NORMAL:
                        click1_a(casilla - EjeX, EjeX, EjeY, bombas, posX_botones, posY_botones)
                    if posX_botones[casilla] < EjeX - 1 and posY_botones[casilla] > 0 and botones[casilla - EjeX + 1]["state"] == NORMAL:
                        click1_a(casilla - EjeX + 1, EjeX, EjeY, bombas, posX_botones, posY_botones)
                    if posX_botones[casilla] > 0 and botones[casilla - 1]["state"] == NORMAL:
                       click1_a(casilla - 1, EjeX, EjeY, bombas, posX_botones, posY_botones) 
                    if posX_botones[casilla] < EjeX - 1 and botones[casilla + 1]["state"] == NORMAL:
                        click1_a(casilla + 1, EjeX, EjeY, bombas, posX_botones, posY_botones) 
                    if posX_botones[casilla] > 0 and posY_botones[casilla] < EjeY - 1 and botones[casilla + EjeX - 1]["state"] == NORMAL:
                        click1_a(casilla + EjeX - 1, EjeX, EjeY, bombas, posX_botones, posY_botones)
                    if posY_botones[casilla] < EjeY - 1 and botones[casilla + EjeX]["state"] == NORMAL:
                        click1_a(casilla + EjeX, EjeX, EjeY, bombas, posX_botones, posY_botones)
                    if posX_botones[casilla] < EjeX - 1 and posY_botones[casilla] < EjeY - 1 and botones[casilla + EjeX + 1]["state"] == NORMAL:
                        click1_a(casilla + EjeX + 1, EjeX, EjeY, bombas, posX_botones, posY_botones)
                else:
                    botones[casilla]["text"] = " " + str(number) + " "
                    botones[casilla]["state"] = DISABLED
                    botones[casilla]["relief"] = SUNKEN

                checkwin(campo)
            else:
                pass
        
        # What the program does when the user left clicks a bomb
        def click1_b(a, b, casilla):
            botones[casilla]["text"] = ' x  '
            botones[casilla]["state"] = DISABLED
            tkinter.messagebox.showinfo("Game Over", "YOU LOST :(.")
            for x in bombas:
                botones[x]["text"] = ' x  '

        # What the program does when the user right clicks
        def click2(casilla):
            if botones[casilla]["text"] == "     ":
                botones[casilla]["text"] = " ?  "
            elif botones[casilla]["text"] == " ?  ":
                botones[casilla]["text"] = "     "

        def checkwin(campo):
            win = True
            for x in campo:
                if botones[x]["state"] == NORMAL:
                    win = False
            if win == True:
                tkinter.messagebox.showinfo("Game Over", "YOU WON :).")
        def checkgameover():
            gameover = False
            for x in bombas:
                if botones[x]["state"] == DISABLED:
                    gameover = True
            return gameover

root.geometry("400x400")

app = Window(root)

root.mainloop()