import random
import pygame
import tkinter as tk
from tkinter import messagebox
pygame.init()
clock=pygame.time.Clock()
FPS=40

name=input('Naam batao boss? ')

white=(255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
height,width=480,480
win=pygame.display.set_mode((width,height))
caption=pygame.display.set_caption("Tic Tac Toe")

def draw_line(x,y):
    line=pygame.draw.line(win ,white ,x,y)

#Grid Designing
l1=draw_line((180,80),(180,400))
l2=draw_line((290,80),(290,400))
l3=draw_line((80,180),(400,180))
l4=draw_line((80,290),(400,290))

#Importing letters
o_image=pygame.image.load('letters/o.png')
x_image=pygame.image.load('letters/x.png')
o=pygame.transform.scale(o_image, (100,100))
x=pygame.transform.scale(x_image, (100,100))
w=pygame.image.load('letters/w1.png')
l=pygame.image.load('letters/n1.png')
t=pygame.image.load('letters/t1.png')

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove(move):
    run = True
    while run:
        move = int(move)
        if move > 0 and move < 10:
            if spaceIsFree(move):
                run = False
                insertLetter('X', move)

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def playerMove(move):
    run = True
    while run:
        move = int(move)
        if move > 0 and move < 10:
            if spaceIsFree(move):
                run = False
                insertLetter('X', move)

def message_box(subject,content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject,content)
    try:
        root.destroy()
    except:
        pass

# Making boxes
click1=0
click2=0
click3=0
click4=0
click5=0
click6=0
click7=0
click8=0
click9=0
end=0

def insert_o(move):
    if move==1:
        global click1
        click1+=1
        win.blit(o,(80,80))
        pygame.display.update()
    if move==2:
        global click2
        click2+=1
        win.blit(o,(190,80))
        pygame.display.update()
    if move==3:
        global click3
        click3+=1
        win.blit(o,(300,80))
        pygame.display.update()
    if move==4:
        global click4
        click4+=1
        win.blit(o,(80,190))
        pygame.display.update()
    if move==5:
        global click5
        click5+=1
        win.blit(o,(190,190))
        pygame.display.update()
    if move==6:
        global click6
        click6+=1
        win.blit(o,(300,190))
        pygame.display.update()
    if move==7:
        global click7
        click7+=1
        win.blit(o,(80,300))
        pygame.display.update()
    if move==8:
        global click8
        click8+=1
        win.blit(o,(190,300))
        pygame.display.update()
    if move==9:
        global click9
        click9+=1
        win.blit(o,(300,300))
        pygame.display.update()

def game(move):
    global end
    global name
    if not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove(move)
        else:
            end=1
            win.blit(l,(80,80))
            message_box('O win\'s',f'Learn to play {name} first you noob!')
            print('Sorry, O\'s won this time!')

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                end=2
                win.blit(t,(80,80))
                message_box('Tie game',f'Aese hi thori {name} jani')
            else:
                insert_o(move)
                insertLetter('O', move)
        else:
            end=3
            message_box('X won',f'Beta {name} agle match mein bata ta hun!')
            win.blit(w,(80,80))

while True:
    mouse = pygame.mouse.get_pos()
    if click1==0:
        if 80 <= mouse[0] <= 170 and 80 <= mouse[1] <= 170:
            x1=pygame.draw.rect(win,color_dark,[80,80,90,90])
        else:
            y1=pygame.draw.rect(win,color_light,[80,80,90,90])

    if click2==0:
        if 190 <= mouse[0] <= 280 and 80 <= mouse[1] <= 170:
            x2=pygame.draw.rect(win,color_dark,[190,80,90,90])
        else:
            y2=pygame.draw.rect(win,color_light,[190,80,90,90])

    if click3==0:
        if 300 <= mouse[0] <= 390 and 80 <= mouse[1] <= 170:
            x3=pygame.draw.rect(win,color_dark,[300,80,90,90])
        else:
            y3=pygame.draw.rect(win,color_light,[300,80,90,90])

    if click4==0:
        if 80 <= mouse[0] <= 170 and 190 <= mouse[1] <= 280:
            x4=pygame.draw.rect(win,color_dark,[80,190,90,90])
        else:
            y4=pygame.draw.rect(win,color_light,[80,190,90,90])

    if click5==0:
        if 190 <= mouse[0] <= 280 and 190 <= mouse[1] <= 280:
            x5=pygame.draw.rect(win,color_dark,[190,190,90,90])
        else:
            y5=pygame.draw.rect(win,color_light,[190,190,90,90])

    if click6==0:
        if 300 <= mouse[0] <= 390 and 190 <= mouse[1] <= 280:
            x6=pygame.draw.rect(win,color_dark,[300,190,90,90])
        else:
            y6=pygame.draw.rect(win,color_light,[300,190,90,90])

    if click7==0:
        if 80 <= mouse[0] <= 170 and 300 <= mouse[1] <= 390:
            x7=pygame.draw.rect(win,color_dark,[80,300,90,90])
        else:
            y7=pygame.draw.rect(win,color_light,[80,300,90,90])

    if click8==0:
        if 190 <= mouse[0] <= 280 and 300 <= mouse[1] <= 390:
            x8=pygame.draw.rect(win,color_dark,[190,300,90,90])
        else:
            y8=pygame.draw.rect(win,color_light,[190,300,90,90])

    if click9==0:
        if 300 <= mouse[0] <= 390 and 300 <= mouse[1] <= 390:
            x9=pygame.draw.rect(win,color_dark,[300,300,90,90])
        else:
            y9=pygame.draw.rect(win,color_light,[300,300,90,90])

    for event in pygame.event.get():

        click=pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and end==0:

            if 80 <= mouse[0] <= 170 and 80 <= mouse[1] <= 170:
                click1+=1
                win.blit(x,(80,80))                
                game(1)           
                pygame.display.update()
                
            if  190 <= mouse[0] <= 280 and 80 <= mouse[1] <= 170:
                click2+=1
                win.blit(x,(190,80))
                game(2)
                pygame.display.update()

            if  300 <= mouse[0] <= 390 and 80 <= mouse[1] <= 170:
                click3+=1
                win.blit(x,(300,80))
                game(3)
                pygame.display.update()

            if  80 <= mouse[0] <= 170 and 190 <= mouse[1] <= 280:
                click4+=1
                win.blit(x,(80,190))
                game(4)
                pygame.display.update()

            if  190 <= mouse[0] <= 280 and 190 <= mouse[1] <= 280:
                click5+=1
                win.blit(x,(190,190))
                game(5)
                pygame.display.update()

            if  300 <= mouse[0] <= 390 and 190 <= mouse[1] <= 280:
                click6+=1
                win.blit(x,(300,190))
                game(6)
                pygame.display.update()

            if  80 <= mouse[0] <= 170 and 300 <= mouse[1] <= 390:
                click7+=1
                win.blit(x,(80,300))
                game(7)
                pygame.display.update()

            if  190 <= mouse[0] <= 280 and 300 <= mouse[1] <= 390:
                click8+=1
                win.blit(x,(190,300))
                game(8)
                pygame.display.update()

            if  300 <= mouse[0] <= 390 and 300 <= mouse[1] <= 390:
                click9+=1
                win.blit(x,(300,300))
                game(9)
                pygame.display.update()

    if end==1:win.blit(l,(80,80))
    if end==2:win.blit(t,(80,80))
    if end==3:win.blit(w,(80,80))
    clock.tick(FPS)
    pygame.display.update()

