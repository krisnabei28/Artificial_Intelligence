import tkinter
import pygame
from tkinter import *
from pygame import *
import tkinter.messagebox as msg
import random

rootGame = Tk()
mixer.init()

def __play_comp__():
    gameComputer = Toplevel(rootGame)
    gameComputer.focus_force()
    width, height = 900, 700
    compWidth = ((gameComputer.winfo_screenwidth()//2) - (width //2))
    compHeight = ((gameComputer.winfo_screenheight()//2) - (height//2))
    gameComputer.geometry(f"{width}x{height}+{compWidth}+{compHeight}")
    gameComputer.resizable(0,0)
    gameComputer.title("Play With Computer")
    gameComputer.iconbitmap("files/ico.ico")
    gameComputer.configure(bg="#EEEEEE")
    
    # ================================ CANVAS GAME CREATION LAYOUT ==================================== #
    canvas = Canvas(gameComputer, height=510, width=660, bg="#EEEEEE", bd=0)
    
    # # ===================== FUNCTIONS(PLAYER VS COMPUTER) ====================== #
    def reset():
        for i in chances:
            i['text'] = ""

    def winner():
        PLAYER = 0
        AI = 1

        for i in range(0, 9, 3):
            first_cell = chances[i]['text']
            idx = i
            count_1 = 0

            current_side = -1

            if first_cell == "":
                continue
            elif first_cell == "X":
                current_side = PLAYER
            elif first_cell == "O":
                current_side = AI

            for j in range(2):
                idx += 1
                if chances[idx]['text'] == first_cell:
                    count_1 += 1

            if count_1 == 2:
                if current_side == PLAYER:
                    msg.showinfo("Well Done!", f"{player1.get()} won this game by defeating Random Bot", parent=gameComputer)
                    reset()
                    return
                elif current_side == AI:
                    msg.showinfo("Try Again!", f"Random Bot won this game by defeating {player1.get()}", parent=gameComputer)
                    reset()
                    return

        for i in range(3):
            first_cell = chances[i]['text']
            idx = i
            count_2 = 0
            
            if first_cell == "":
                continue
            elif first_cell == "X":
                current_side = PLAYER
            elif first_cell == "O":
                current_side = AI

            for j in range(2):
                idx += 3
                if chances[idx]['text'] == first_cell:
                    count_2 += 1

            if count_2 == 2:
                if current_side == PLAYER:
                    msg.showinfo("Well Done!", f"{player1.get()} won this game by defeating Random Bot", parent=gameComputer)
                    reset()
                    return

                elif current_side == AI:
                    msg.showinfo("Try Again!", f"Random Bot won this game by defeating {player1.get()}", parent=gameComputer)
                    reset()
                    return

        cell0 = chances[0]['text']
        if cell0 != "" and cell0 == chances[4]['text'] and cell0 == chances[8]['text']:
            if cell0 == "X":
                msg.showinfo("Well Done!", f"{player1.get()} won this game by defeating Random Bot", parent=gameComputer)
                reset()
                return

            elif cell0 == "O":
                msg.showinfo("Try Again!", f"Random Bot won this game by defeating {player1.get()}", parent=gameComputer)
                reset()
                return
        
        cell0 = chances[2]['text']
        if cell0 != "" and cell0 == chances[4]['text'] and cell0 == chances[6]['text']:
            if cell0 == "X":
                msg.showinfo("Well Done!", f"{player1.get()} won this game by defeating Random Bot", parent=gameComputer)
                reset()
                return

            elif cell0 == "O":
                msg.showinfo("Try Again!", f"Random Bot won this game by defeating {player1.get()}", parent=gameComputer)
                reset()
                return

        for i in chances:
            if i['text'] == "":
                return
        
        msg.showinfo("Better Luck Next Time!", f"It is a tie between {player1.get()} and Random Bot", parent=gameComputer)
        reset()

    def bot_move():
        chance = random.choice(chances)  # CHOICE IS USED TO PICK ONE ItEM FROM A LIST
        if chance.cget('text') == "":
            chance.config(text="O")
            ___playSound___()
        else:
            for x in range(len(chances)):
                if chances[x].cget('text') == "":
                    bot_move()
                    break
        p_name.config(fg="red")
        c_name.config(fg="black")
        winner()
    
    def whose_move(event):
        p_name.config(fg="black")
        c_name.config(fg="red")
        event.widget.config(text="X")
        ___playSound___()
        winner()
        gameComputer.after(400, bot_move)

    def check_space(event):
        if event.widget.cget('text') == "":
            whose_move(event)

    INIT_XY = 6
    initial = [6, 6]
    incr = [200, 170]
    chances = []

    for i in range(3):
        for j in range(3):
            sq = Frame(canvas, width=190, height=160, bg="#0a0a0a")
            l1 = Label(sq, text="", font="Corbel 93 bold", bg="#EEEEEE")  # 7 EMPTY SPACES
            l1.pack(padx=1, pady=1.5, fill="both", side="top")
            sq.pack_propagate(False) 
            sq.place(x=initial[0], y=initial[1])

            initial[0] += incr[0]
            chances.append(l1)
        
        initial[0] = INIT_XY
        initial[1] += incr[1]

    for x in chances:
        x.bind('<Button>', check_space)

    canvas.place(x=(width / 2) - (660 / 2), y=(height / 2) - (660 / 2))

    # ========================== PLAYER NAME =========================== #
    p_name = Label(gameComputer, text=player1.get(), font="Corbel 20 bold", bg="#EEEEEE", anchor=W, fg="red")
    p_name.pack(side=LEFT, anchor=NW, padx=5)

    c_name = Label(gameComputer, text="Random Bot", font="Corbel 20 bold", bg="#EEEEEE", anchor=W)
    c_name.pack(side=RIGHT, anchor=NE, padx=5)

    ___playSound___()

def __computer__():

    # ================== FUNCTIONS DI COMPUTER================= #
    def __comp_condition__():
        computer.destroy()
        if player1.get() == "":
            msg.showerror("Error", "Please check that you have entered the name of player.")
            __computer__()
        else:
            __play_comp__()
            player1.set("")

    def _comp_quit_():
        player1.set("")
        player2.set("")
        computer.destroy()

    computer = Toplevel(rootGame)
    computer.focus_force()
    w, h = 850, 500
    computer.geometry(f"{w}x{h}+{350}+{150}")
    computer.title("Player")
    computer.iconbitmap("files/ico.ico")
    computer.resizable(0, 0)
    computer.e1 = PhotoImage(file="files/BgNick.png")
    computer.submit = PhotoImage(file="files/submit.png")
    computer.configure(bg="#FFFFFF")

    # ============================ LAYOUT ========================== #

    heading = Label(computer, text="Enter The Name Of Player", font="Courier 33 bold", pady=5)
    heading.pack(fill=X)

    frame1 = Frame(computer, bg="#FFFFFF")
    p_1 = Label(frame1, text="Player's Name:", font="Courier 20 bold", pady=25, bg="#FFFFFF", padx=40)
    p_1.pack(side=LEFT, anchor=W)

    l1 = Label(frame1, image=computer.e1, bg="#FFFFFF")
    l1.pack(side=RIGHT, anchor=E, padx=40)

    global e1
    player1.set("")

    e1 = Entry(frame1, textvariable=player1, bg="#FFFFFF", font="Courier 25 bold", width=12, relief=FLAT)
    e1.place(x=460, y=20)
    frame1.pack(fill=X, pady=10)

    frame2 = Frame(computer, bg="#FFFFFF")
    p_2 = Label(frame2, text="Computer Name:", font="Courier 20 bold", pady=25, bg="#FFFFFF", padx=40)
    p_2.pack(side=LEFT, anchor=W)

    l2 = Label(frame2, image=computer.e1, bg="#FFFFFF")
    l2.pack(side=RIGHT, anchor=E, padx=40)

    global e2
    player1.set("")

    e2 = Label(frame2, text="Random Bot", bg="#FFFFFF", font="Courier 25 bold", width=12, relief=FLAT, anchor=W)
    e2.place(x=460, y=20)
    frame2.pack(fill=X, pady=10)

    btn_submit = Button(computer, image=computer.submit, bg="#FFFFFF", bd=0, command=__comp_condition__)
    btn_submit.pack(side=RIGHT, anchor=SE, padx=10, pady=10)

    btn_quit = Button(computer, image=rootGame.exitGame, bd=0, bg="#FFFFFF", command=_comp_quit_)
    btn_quit.pack(side=LEFT, anchor=SW, padx=10, pady=10)
    ___playSound___()

#======== FUNCTIONS ========

def ____sound___():
    if popGame.get() == 1:
        soundGame.config(image=rootGame.soundOff)
        popGame.set(0)
    elif popGame.get() == 0:
        soundGame.config(image=rootGame.soundOn)
        popGame.set(1)
        ___playSound___()
        
def ___playSound___():
    if popGame.get() == 1:
        pop_Sound = mixer.Sound("files/pop.wav")
        pop_Sound.play()
        
def ___music___():
    if music_temp.get() == 0:
        musicGame.config(image=rootGame.musicOn)
        music_temp.set(1)
        __playMusic__()
    elif music_temp.get() == 1:
        musicGame.config(image=rootGame.musicOff)
        music_temp.set(0)
        __stopMusic__()

def __playMusic__():
    mixer.music.load("files/music.mp3")
    mixer.music.play(-1)

def __stopMusic__():
    mixer.music.pause()

def ___exit___():
    rootGame.destroy()

width , height = 850, 500
rootGame.geometry(f'{width}x{height}+{350}+{150}')
rootGame.title("TIC TAC TOE")
rootGame.iconbitmap("files/ico.ico")
rootGame.heading = PhotoImage(file="files/background.png")
rootGame.buttonGame = PhotoImage(file="files/play.png")
rootGame.soundOn = PhotoImage(file="files/s_on.png")
rootGame.soundOff = PhotoImage(file="files/s_off.png")
rootGame.musicOn = PhotoImage(file="files/music_on.png")
rootGame.musicOff = PhotoImage(file="files/music_off.png")
rootGame.exitGame = PhotoImage(file="files/exit.png")
rootGame.resizable(0,0)

music_temp = IntVar(rootGame, 1)
popGame = IntVar(rootGame, 1)
move = IntVar(rootGame, 1)
player1 = StringVar()
player2 = StringVar()

#============= LAYOUT ===========
lblBg = Label(rootGame, image=rootGame.heading)
lblBg.pack(pady=25)

playButton = Button(rootGame, image=rootGame.buttonGame, bd=0, relief=FLAT, command=__computer__)
playButton.pack(pady=15)

soundGame = Button(rootGame, image=rootGame.soundOn, bd=0, relief=FLAT, command=____sound___)
soundGame.pack(anchor=S, side=LEFT, padx=10, pady=5)

musicGame = Button(rootGame, image=rootGame.musicOn, bd=0, relief=FLAT, command=___music___)
musicGame.pack(anchor=S, side=LEFT, padx=10, pady=5)

exitedGame = Button(rootGame, image=rootGame.exitGame, bd=0, relief=FLAT, command=___exit___)
exitedGame.pack(anchor=S, side=RIGHT, padx=10, pady=5)

__playMusic__()

rootGame.mainloop()

