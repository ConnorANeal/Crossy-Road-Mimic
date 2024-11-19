### CONNOR NEAL & CADEN HINSHAW ###

### TIME SPENT ###

# Connor: 11 hours
# Caden: 3 hours
# Total: 14 hours

### WHO DID WHAT ###

# Connor: Main Menu, Settings, The Actual Game
# Caden: The Actual Game

##### THE CODE #####
# 749 Lines

from tkinter import *
import random
import tkinter as tk

##### UPDATE SETTINGS DISPLAY #####

def update_config():
    global diffTitle
    global lvlTitle
    global ctrlTitle

    c = open("settings.txt")
    config = c.readlines()
    diff = config[0]
    lvl = config[1]
    ctrl = config[2]
    
    canvas.delete(diffTitle)
    canvas.delete(lvlTitle)
    canvas.delete(ctrlTitle)
    
    diffTitle = canvas.create_text(140, 250, text=("Difficulty: " + diff.title()), font=("Helvetica bold", 15))
    lvlTitle = canvas.create_text(140, 280, text=("Level: " + lvl.title()), font=("Helvetica bold", 15))
    ctrlTitle = canvas.create_text(140, 310, text=("Controls: " + ctrl.title()), font=("Helvetica bold", 15))

##### CLOSE SETTINGS MENU #####

def close():
    print("SETTINGS CLOSED")
    update_config()
    settings.destroy()

##### CLOSE ERROR BOX #####
    
def okay():
    error.destroy()

##### CLOSE SUCCESSFUL SAVE BOX #####

def close_success():
    success.destroy()

##### SETTINGS SAVE SUCCESSFUL #####
    
def save_successful():
    global success
    
    success = tk.Toplevel()
    success.title("SAVED!")
    
    Label(success, text="Settings saved successfully!", font=("Helvetica", 12, "bold")).grid(row=0, column=0)
    Label(success, text=" ").grid(row=1, column=0)
    successClose = Button(success, text="Okay", command=close_success)
    successClose.grid(row=2, column=0)
    Label(success, text=" ").grid(row=3, column=0)

##### SETTINGS ERROR POPUP #####

def error_popup():
    global error
    
    error = tk.Toplevel()
    error.title("ERROR!")
    
    Label(error, text="    Invalid settings were submitted.    ", font=("Helvetica", 14, "bold")).grid(row=0, column=0)
    
    if diffInput.lower() != "easy" and diffInput.lower() != "medium" and diffInput.lower() != "hard":
        Label(error, text="Invalid difficulty. The difficulty will default back to easy.").grid(row=1, column=0)
    if levelInput.lower() != "earth" and levelInput.lower() != "moon" and levelInput.lower() != "candyland":
        Label(error, text="Invalid level. The level will default back to earth.").grid(row=2, column=0)
    if ctrlInput.lower() != "wasd" and ctrlInput.lower() != "arrow keys":
        Label(error, text="Invalid controls. The controls will default back to arrow keys.").grid(row=3, column=0)
    
    Label(error, text=" ").grid(row=4, column=0)
    okayButton = Button(error, text="Okay", command=okay)
    okayButton.grid(row=5, column=0)
    Label(error, text=" ").grid(row=6, column=0)

##### SAVE SETTINGS #####

def save():
    print("Settings saved successfully!")
    
    read_settings()
    
    global diffInput
    global levelInput
    global ctrlInput
    
    diffEntry = difficultySelect.get()
    levelEntry = levelSelect.get()
    ctrlEntry = controlSelect.get()
    
    diffInput = diffEntry.strip()
    levelInput = levelEntry.strip()
    ctrlInput = ctrlEntry.strip()

    try:
        with open("settings.txt", 'w') as f:
            if diffInput.lower() == "easy":
                f.write("easy\n")
                print("Difficulty: Easy")
            elif diffInput.lower() == "medium":
                f.write("medium\n")
                print("Difficulty: Medium")
            elif diffInput.lower() == "hard":
                f.write("hard\n")
                print("Difficulty: Hard")
            else:
                error_popup()
                f.write("easy\n")
                print("Invalid difficulty selected.\n Difficulty: Easy")

            if levelInput.lower() == "earth":
                f.write("earth\n")
                print("Level: Earth")
            elif levelInput.lower() == "moon":
                f.write("moon\n")
                print("Level: Moon")
            elif levelInput.lower() == "candyland":
                f.write("candyland\n")
                print("Level: Candyland")
            else:
                if diffInput.lower() != "easy" and diffInput.lower() != "medium" and diffInput.lower() != "hard":
                    pass
                else:
                    error_popup()
                f.write("earth\n")
                print("Invalid level selected.\n Level: Earth")

            if ctrlInput.lower() == "arrow keys":
                f.write("arrow keys\n")
                print("Controls: Arrow Keys")
            elif ctrlInput.lower() == "wasd":
                f.write("wasd\n")
                print("Controls: WASD")
            else:
                if diffInput.lower() != "easy" and diffInput.lower() != "medium" and diffInput.lower() != "hard":
                    pass
                elif levelInput.lower() != "earth" and levelInput.lower() != "moon" and levelInput.lower() != "candyland":
                    pass
                else:
                    error.popup()
                f.write("arrow keys\n")
                print("Invalid controls selected.\n Controls: Arrow Keys")
            
            if diffInput.lower() != "easy" and diffInput.lower() != "medium" and diffInput.lower() != "hard":
                sad = 1
            elif levelInput.lower() != "earth" and levelInput.lower() != "moon" and levelInput.lower() != "candyland":
                sad = 1
            elif ctrlInput.lower() != "wasd" and ctrlInput.lower() != "arrow keys":
                sad = 1
            else:
                sad = 0
                save_successful()

    except Exception as err:
        print(err)
        exit()

##### OPEN SETTINGS MENU #####

def open_settings():
    global settings
    
    settings = tk.Toplevel()
    settings.title("Settings")

    global difficultySelect
    global levelSelect
    global controlSelect
    
    blankspace = "      "
    newline = "\n"
    heading = newline + blankspace + "SETTINGS" + blankspace + newline

    Label(settings, text=heading, font=("Helvetica bold", 24)).grid(row=0, column=0)

    Label(settings, text="   DIFFICULTY SELECT:   ", font=("Helvetica bold", 20)).grid(row=1, column=0)
    Label(settings, text="EASY, MEDIUM, OR HARD\n", font=("Helvetica bold", 15)).grid(row=2, column=0)

    difficultySelect = Entry(settings)
    difficultySelect.grid(row=3, column=0)

    Label(settings, text="\n    SCENE SELECTION:    ", font=("Helvetica bold", 20)).grid(row=4, column=0)
    Label(settings, text="  EARTH, MOON, OR CANDYLAND  \n", font=("Helvetica bold", 15)).grid(row=5, column=0)

    levelSelect = Entry(settings)
    levelSelect.grid(row=6, column=0)

    Label(settings, text="\n   CONTROLS:   ", font=("Helvetica bold", 20)).grid(row=7, column=0)
    Label(settings, text="   'WASD' OR 'ARROW KEYS'   \n", font=("Helvetica bold", 15)).grid(row=8, column=0)

    controlSelect = Entry(settings)
    controlSelect.grid(row=9, column=0)

    Label(settings, text=" ").grid(row=10, column=0)

    saveButton = Button(settings, text="   Save Settings   ", font=("Helvetica bold", 12), command=save)
    saveButton.grid(row=11, column=0)

    Label(settings, text=" ").grid(row=12, column=0)

    closeButton = Button(settings, text="    Back to Menu    ", font=("Helvetica bold", 12), command=close)
    closeButton.grid(row=13, column=0)

    Label(settings, text="\n").grid(row=14, column=0)

##### READ SETTINGS #####

def read_settings():
    global length
    global speed
    global lvlColor
    global up
    global down
    global left
    global right
    global moveY1
    global moveY2
    global moveY3
    global moveY4
    global moveY5
    global moveY6
    global moveY7
    global moveY8
    global moveY9
    global moveY10
    global moveY11
    
    c = open("settings.txt")
    config = c.readlines()
    diff = config[0]
    lvl = config[1]
    ctrl = config[2]

    if diff.strip() == "easy":
        speed = 3
        length = 850
    elif diff.strip() == "medium":
        speed = 5
        length = 1050
    elif diff.strip() == "hard":
        speed = 8
        length = 1250
    else:
        speed = 5
        length = 850

    if lvl.strip() == "earth":
        lvlColor = "Cyan"
    elif lvl.strip() == "moon":
        lvlColor = "Gray"
    elif lvl.strip() == "candyland":
        lvlColor = "Pink"
    else:
        lvlColor = "Cyan"

    if ctrl.strip() == "wasd":
        up = "w"
        left = "a"
        right = "d"
        down = "s"
    elif ctrl.strip() == "arrow keys":
        up = "<Up>"
        left = "<Left>"
        right = "<Right>"
        down = "<Down>"
    else:
        up = "w"
        left = "a"
        right = "d"
        down = "s"

    moveY1 = 1 * speed
    moveY2 = 1 * speed
    moveY3 = 1 * speed
    moveY4 = 1 * speed
    moveY5 = 1 * speed
    moveY6 = 1 * speed
    moveY7 = 1 * speed
    moveY8 = 1 * speed
    moveY9 = 1 * speed
    moveY10 = 1 * speed
    moveY11 = 1 * speed

##### PLAYER CONTROLS #####

def moveUp(event):
    playerX0, playerY0, playerX1, playerY1 = gameCanvas.coords(player)
    if playerY0 <= 0:
        pass
    else:
        gameCanvas.move(player, 0, -15)

def moveDown(event):
    playerX0, playerY0, playerX1, playerY1 = gameCanvas.coords(player)
    if playerY1 >= 595:
        pass
    else:
        gameCanvas.move(player, 0, 15)

def moveLeft(event):
    playerX0, playerY0, playerX1, playerY1 = gameCanvas.coords(player)
    if playerX0 <= 0:
        pass
    else:
        gameCanvas.move(player, -15, 0)
        
def moveRight(event):
    playerX0, playerY0, playerX1, playerY1 = gameCanvas.coords(player)
    if playerX1 >= 850:
        pass
    else:
        gameCanvas.move(player, 15, 0)

##### CAR MOVING FUNCTIONS #####

def car1Move():
    global moveY1
    gameCanvas.move(car1, 0, moveY1)
    car1X0, car1Y0, car1X1, car1Y1 = gameCanvas.coords(car1)
    if car1Y0 <= 0:
        moveY1 *= -1
    if car1Y1 >= 595:
        moveY1 *= -1
    game.after(15, car1Move)
    
def car2Move():
    global moveY2
    gameCanvas.move(car2, 0, moveY2)
    car2X0, car2Y0, car2X1, car2Y1 = gameCanvas.coords(car2)
    if car2Y0 <= 0:
        moveY2 *= -1
    if car2Y1 >= 595:
        moveY2 *= -1
    game.after(15, car2Move)
    
def car3Move():
    global moveY3
    gameCanvas.move(car3, 0, moveY3)
    car3X0, car3Y0, car3X1, car3Y1 = gameCanvas.coords(car3)
    if car3Y0 <= 0:
        moveY3 *= -1
    if car3Y1 >= 595:
        moveY3 *= -1
    game.after(15, car3Move)

def car4Move():
    global moveY4
    gameCanvas.move(car4, 0, moveY4)
    car4X0, car4Y0, car4X1, car4Y1 = gameCanvas.coords(car4)
    if car4Y0 <= 0:
        moveY4 *= -1
    if car4Y1 >= 595:
        moveY4 *= -1
    game.after(15, car4Move)
    
def car5Move():
    global moveY5
    gameCanvas.move(car5, 0, moveY5)
    car5X0, car5Y0, car5X1, car5Y1 = gameCanvas.coords(car5)
    if car5Y0 <= 0:
        moveY5 *= -1
    if car5Y1 >= 595:
        moveY5 *= -1
    game.after(15, car5Move)
    
def car6Move():
    global moveY6
    gameCanvas.move(car6, 0, moveY6)
    car6X0, car6Y0, car6X1, car6Y1 = gameCanvas.coords(car6)
    if car6Y0 <= 0:
        moveY6 *= -1
    if car6Y1 >= 595:
        moveY6 *= -1
    game.after(15, car6Move)
    
def car7Move():
    global moveY7
    gameCanvas.move(car7, 0, moveY7)
    car7X0, car7Y0, car7X1, car7Y1 = gameCanvas.coords(car7)
    if car7Y0 <= 0:
        moveY7 *= -1
    if car7Y1 >= 595:
        moveY7 *= -1
    game.after(15, car7Move)

def car8Move():
    global moveY8
    gameCanvas.move(car8, 0, moveY8)
    car8X0, car8Y0, car8X1, car8Y1 = gameCanvas.coords(car8)
    if car8Y0 <= 0:
        moveY8 *= -1
    if car8Y1 >= 595:
        moveY8 *= -1
    game.after(15, car8Move)
    
def car9Move():
    global moveY9
    gameCanvas.move(car9, 0, moveY9)
    car9X0, car9Y0, car9X1, car9Y1 = gameCanvas.coords(car9)
    if car9Y0 <= 0:
        moveY9 *= -1
    if car9Y1 >= 595:
        moveY9 *= -1
    game.after(15, car9Move)
    
def car10Move():
    global moveY10
    gameCanvas.move(car10, 0, moveY10)
    car10X0, car10Y0, car10X1, car10Y1 = gameCanvas.coords(car10)
    if car10Y0 <= 0:
        moveY10 *= -1
    if car10Y1 >= 595:
        moveY10 *= -1
    game.after(15, car10Move)
    
def car11Move():
    global moveY11
    gameCanvas.move(car11, 0, moveY11)
    car11X0, car11Y0, car11X1, car11Y1 = gameCanvas.coords(car11)
    if car11Y0 <= 0:
        moveY11 *= -1
    if car11Y1 >= 595:
        moveY11 *= -1
    game.after(15, car11Move)

##### CLOSE WIN SCREEN #####
    
def close_wins():
    wins.destroy()

##### WIN SCREEN #####

def winner():
    global wins
    
    s = open("score.txt")
    score = s.readlines()
    numberwins = int(score[0])
    numberwins += 1
    s.close()
    
    try:
        with open("score.txt", 'w') as t:
            t.write(str(numberwins))
    
    except Exception as err:
        print(err)
        exit()
    
    global scoreTitle

    s = open("score.txt")
    score = s.readlines()
    numberwins = score[0]
    
    canvas.delete(scoreTitle)
    
    scoreTitle = canvas.create_text(140, 130, text=("Wins: " + str(numberwins)), font=("Helvetica bold", 15))
    
    game.destroy()
    
    wins = tk.Toplevel()
    wins.title("WINNER!!!")
    wins.geometry("500x200")
    
    wins.configure(bg="Green")
    
    winmsg = Label(wins, text="YOU WIN!!!", font=("Helvetica bold", 36))
    winmsg.pack()
    
    closewinner = Button(wins, text="  Back to Menu  ", font=("Helvetica bold", 12), command=close_wins)
    closewinner.pack()
    
    wins.mainloop()

##### CLOSE LOSE SCREEN #####
    
def close_loser():
    loses.destroy()

##### LOSE SCREEN #####

def loser():
    global loses
    
    game.destroy()
    
    loses = tk.Toplevel()
    loses.title("LOSER!")
    loses.geometry("500x200")
    
    loses.configure(bg="Red")
    
    losemsg = Label(loses, text="YOU LOST!", font=("Helvetica bold", 36))
    losemsg.pack()
    
    closeloser = Button(loses, text="  Back to Menu  ", font=("Helvetica bold", 12), command=close_loser)
    closeloser.pack()
    
    loses.mainloop()

##### CHECK FOR PLAYER COLLISION #####

def checkCollide():
    pCds = gameCanvas.coords(player)
    
    collide = gameCanvas.find_overlapping(pCds[0], pCds[1], pCds[2], pCds[3])
    collide = list(collide)
    collide.remove(player)
    
    if pCds[2] < (length - 80):
        if len(collide) == 0:
            game.after(2, checkCollide)
        else:
            print("LOSE")
            loser()
    else:
        if len(collide) == 0:
            game.after(2, checkCollide)
        else:
            print("WIN")
            winner()

##### CLOSE GAME #####
            
def close_game():
    print("Game Closed")
    game.destroy()

##### OPEN GAME GUI #####

startY1 = random.randint(0, 546)
startY2 = random.randint(0, 546)
startY3 = random.randint(0, 546)
startY4 = random.randint(0, 546)
startY5 = random.randint(0, 546)
startY6 = random.randint(0, 546)
startY7 = random.randint(0, 546)
startY8 = random.randint(0, 546)
startY9 = random.randint(0, 546)
startY10 = random.randint(0, 546)
startY11 = random.randint(0, 546)

def launch():
    global game
    global gameCanvas
    global player
    global car1
    global car2
    global car3
    global car4
    global car5
    global car6
    global car7
    global car8
    global car9
    global car10
    global car11
    
    read_settings()
    
    game = tk.Toplevel()
    game.title("Traversy Path")
    
    gameCanvas = Canvas(game, width=length, height=595, bg=lvlColor)
    
    closegame_button = Button(game, text="  Back to Menu  ", font=("Helvetica bold", 12), command=close_game)
    closegame_button.pack()
    
    finishLine = gameCanvas.create_rectangle(0, -5, 5, 605, fill="White")
    gameCanvas.move(finishLine, (length - 80), 0)

##### CREATE GAME CANVAS DETAILS #####

    gameCanvas.create_text((length - 40), 280, text="FINISH", font=("Helvetica bold", 40), angle=270)

    player = gameCanvas.create_oval(0, 0, 40, 40, fill="yellow")
    gameCanvas.move(player, 15, 270)

    car1 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
    gameCanvas.move(car1, 100, startY1)

    car2 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
    gameCanvas.move(car2, 180, startY2)

    car3 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
    gameCanvas.move(car3, 260, startY3)

    car4 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
    gameCanvas.move(car4, 440, startY4)

    car5 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
    gameCanvas.move(car5, 520, startY5)

    car6 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
    gameCanvas.move(car6, 600, startY6)

    car7 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
    gameCanvas.move(car7, 680, startY7)
    
    if length == 850:
        print("Difficulty Easy Loaded")
    elif length == 1050:
        print("Difficulty Medium Loaded")
        car8 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
        gameCanvas.move(car8, 760, startY8)
        car9 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
        gameCanvas.move(car9, 840, startY9)
        game.after(15, car8Move)
        game.after(15, car9Move)
    else:
        print("Difficulty Hard Loaded")
        car8 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
        gameCanvas.move(car8, 760, startY8)
        car9 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
        gameCanvas.move(car9, 840, startY9)
        car10 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
        gameCanvas.move(car10, 920, startY10)
        car11 = gameCanvas.create_rectangle(0, 0, 50, 50, fill=random.choice(blockColors))
        gameCanvas.move(car11, 1080, startY11)
        game.after(15, car8Move)
        game.after(15, car9Move)
        game.after(15, car10Move)
        game.after(15, car11Move)
    
    gameCanvas.bind(up, moveUp)
    gameCanvas.bind(down, moveDown)
    gameCanvas.bind(left, moveLeft)
    gameCanvas.bind(right, moveRight)
    gameCanvas.pack()
    gameCanvas.focus_set()
    
    game.after(2, checkCollide)
    
    game.after(15, car1Move)
    game.after(15, car2Move)
    game.after(15, car3Move)
    game.after(15, car4Move)
    game.after(15, car5Move)
    game.after(15, car6Move)
    game.after(15, car7Move)
    
    game.mainloop()

##### MAIN MENU SCREEN #####

menu = tk.Tk()
blank = " "
menu.title(130*blank + "Traversy Path")
canvas = Canvas(menu, width=1000, height=600)

blockColors = ["red", "orange", "blue", "green", "black", "violet"]

menu_block = canvas.create_rectangle(0, 0, 75, 75, fill=random.choice(blockColors))
canvas.move(menu_block, 225, 200)

whitespaceBlock1 = canvas.create_rectangle(-2, -2, 300, 602, fill="white")
whitespaceBlock2 = canvas.create_rectangle(0, -2, 302, 602, fill="white")
canvas.move(whitespaceBlock2, 700, 0)

canvas.create_text(495, 50, text="TRAVERSY", font=("Helvetica bold", 30, "bold"))
canvas.create_text(495, 90, text="PATH", font=("Helvetica bold", 30, "bold"))

##### BUTTONS #####

playButton = canvas.create_rectangle(0, 0, 70, 40, fill="white")
canvas.move(playButton, 460, 380)
canvas.create_text(495, 400, text="PLAY")

settingsButton = canvas.create_rectangle(0, 0, 90, 40, fill="white")
canvas.move(settingsButton, 450, 440)
canvas.create_text(495, 460, text="SETTINGS")

quitButton = canvas.create_rectangle(0, 0, 70, 40, fill="white")
canvas.move(quitButton, 460, 500)
canvas.create_text(495, 520, text="QUIT")

##### DISPLAY SETTINGS AND SCORES #####

read_settings()

s = open("score.txt")
score = s.readlines()
numberwins = score[0]

c = open("settings.txt")
config = c.readlines()
diff = config[0]
lvl = config[1]
ctrl = config[2]

scoreTitle = canvas.create_text(140, 130, text=("Wins: " + str(numberwins)), font=("Helvetica bold", 15))

diffTitle = canvas.create_text(140, 250, text=("Difficulty: " + diff.title()), font=("Helvetica bold", 15))
lvlTitle = canvas.create_text(140, 280, text=("Level: " + lvl.title()), font=("Helvetica bold", 15))
ctrlTitle = canvas.create_text(140, 310, text=("Controls: " + ctrl.title()), font=("Helvetica bold", 15))

##### ANIMATE MENU SCREEN #####

def menuAnimate():
    canvas.move(menu_block, 5, 0)
    mbx0, mby0, mbx1, mby1 = canvas.coords(menu_block)
    if mbx0 > 700:
        canvas.move(menu_block, -475, 0)
    menu.after(20, menuAnimate)

##### MAIN MENU BUTTON ACTIONS #####

def buttonSelect(event):
    cursorX = event.x
    cursorY = event.y
    px0, py0, px1, py1 = canvas.coords(playButton)
    sx0, sy0, sx1, sy1 = canvas.coords(settingsButton)
    qx0, qy0, qx1, qy1 = canvas.coords(quitButton)
    if cursorX <= px1 and cursorX >= px0 and cursorY >= py0 and cursorY <= py1:
        print("PLAY")
        launch()
    if cursorX <= sx1 and cursorX >= sx0 and cursorY >= sy0 and cursorY <= sy1:
        print("SETTINGS OPENED")
        open_settings()
    if cursorX <= qx1 and cursorX >= qx0 and cursorY >= qy0 and cursorY <= qy1:
        print("GAME QUIT")
        menu.destroy()

canvas.bind("<Button-1>", buttonSelect)
canvas.pack()
canvas.focus_set()

menu.after(20, menuAnimate)
menu.mainloop()