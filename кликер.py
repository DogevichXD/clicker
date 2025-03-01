from tkinter import *
import random
import tkinter as tk

HP = 25
P = 100
LVL = 1
MonsterLVL= 50
Money = 100
STR = 0
DECS = 0 
INT = 0 

def clear_window():
    for widget in window.winfo_children():
        if not isinstance(widget, tk.Menu):
            widget.destroy()

def gear_clicked():
    clear_window()

def ability_clicked():
    global STR
    global DECS
    global INT
    clear_window()
    labelSTR = Label(window,text="СИЛА")
    labelSTR.grid(column=0,row=0)
    labelDECS = Label(window,text="ЛОВКОСТЬ")
    labelDECS.grid(column=0,row=1)
    labelINT = Label(window,text="ИНТЕЛЕКТ")
    labelINT.grid(column=0,row=2)
    STR = Button(text="+",command=STR_btn)
    STR.grid(column=1,row=0)
    DECS = Button(text="+",command=DECS_btn)
    DECS.grid(column=1,row=1)
    INT = Button(text="+",command=INT_btn)
    INT.grid(column=1,row=2)
    
def STR_btn():
    LVL-=1
    STR+=1
    labelSTR ["text"]=f"{STR}"

def DECS_btn():
    LVL-=1
    DECS+=1
    labelDECS ["text"]=f"{DECS}"

def INT_btn():
    LVL-=1
    INT+=1
    labelINT ["text"]=f"{INT}"

def exit_clicked():
    window.destroy()

def PlayerHP():
    global P
    P = P - 1
    labelP ["text"]=P
    window.after(1000, P)
 
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

player_menu.add_command(label="Навыки", command=ability_clicked)
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
