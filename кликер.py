from tkinter import *
import random
import tkinter as tk

HP = 25
P = 100
LVL = 1
MonsterLVL= 50
Money = 100

def gear_clicked():
    gear = Tk()
    gear.title("Экипировка")

def exit_clicked():
    window.destroy()

def PlayerHP():
    global P
    P = P - 1
    labelP ["text"]=P
    root.after(1000, P)
 
def click_button():
    global HP
    global LVL
    global P
    global MonsterLVL
    Dmg = random.randint (1,LVL)
    HP -= Dmg
    if HP <= 1:
        HP = MonsterLVL
        MonsterLVL +=10
        LVL +=1
    else:
        HP += 0
    labelHP ["text"]=HP
    labelP ["text"]=P
    labelLVL ["text"]=LVL
        
window = Tk()
window.title("Кликер")
window.geometry("400x250")
 
btn = Button(text="Kill",command=click_button,)
btn.pack()
labelHP = Label(window,text=HP)
labelHP.pack()
labelP = Label(window,text=P)
labelP.pack()
labelLVL = Label(window,text=LVL)
labelLVL.pack()

window.option_add("*tearOff", FALSE)

main_menu = Menu()
player_menu = Menu()

player_menu.add_command(label="Навыки")
player_menu.add_command(label="Экипировка", command=gear_clicked)
setings_menu = Menu()
setings_menu.add_command(label="Новая игра")
setings_menu.add_command(label="Сохранить")
setings_menu.add_command(label="Загрузить")
setings_menu.add_separator()
setings_menu.add_command(label="Выйти", command=exit_clicked)

main_menu.add_cascade(label="Игра",menu=setings_menu)
main_menu.add_cascade(label="Игрок",menu=player_menu)
main_menu.add_cascade(label="Магазин")

window.config(menu=main_menu)

window.mainloop()
PlayerHP()
