import pygame 
from pygame import QUIT
pygame.font.init()  
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
LIME = (0, 128, 0)
screen = pygame.display.set_mode((500, 600)) 
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")   
x,y,val=0,0,0
req = 500 / 9
import random

board1= [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board2= [
    [3,0,6,5,0,8,4,0,0],
    [5,2,0,0,0,0,0,0,0],
    [0,8,7,0,0,0,0,3,1],
    [0,0,3,0,1,0,0,8,0],
    [9,0,0,8,6,3,0,0,5],
    [0,5,0,0,9,0,6,0,0],
    [1,3,0,0,0,0,2,5,0],
    [0,0,0,0,0,0,0,7,4],
    [0,0,5,2,0,6,3,0,0]
]

database=[board1, board2]
board=random.choice(database)
fo = pygame.font.SysFont("comicsans", 40) 
fo2 = pygame.font.SysFont("comicsans", 20) 
def get_cord(pos): 
    global x 
    x = pos[0]//req 
    global y 
    y = pos[1]//req 
    
def draw_box(): 
    for i in range(2): 
        pygame.draw.line(screen, (255, 0, 0), (x * req-3, (y + i)*req), (x * req + req + 3, (y + i)*req), 7) 
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* req, y * req ), ((x + i) * req, y * req + req), 7)    
  
def draw(): 
    for i in range (9): 
        for j in range (9): 
            if board[i][j]!= 0: 
                text = fo.render(str(board[i][j]), 1, (RED)) 
                screen.blit(text, (i * req + 15, j * req + 15))       
    for i in range(10): 
        if i % 3 == 0 : 
            thick = 7
        else: 
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * req), (500, i * req), thick) 
        pygame.draw.line(screen, (0, 0, 0), (i * req, 0), (i * req, 500), thick)        
def draw_value(val): 
    text = fo.render(str(val), 1, (GREEN)) 
    screen.blit(text, (x * req + 15, y * req + 15))     
def error1(): 
    text = fo.render("WRONG !!!", 1, (0, 0, 0)) 
    screen.blit(text, (20, 570))   
def error2(): 
    text = fo.render("Wrong !!! Not a valid Key", 1, (0, 0, 0)) 
    screen.blit(text, (20, 570))   
 
def valid(m, i, j, val): 
    for it in range(9): 
        if m[i][it]== val: 
            return False
        if m[it][j]== val: 
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3): 
        for j in range (jt * 3, jt * 3 + 3): 
            if m[i][j]== val: 
                return False
    return True
  
def solve(board, i, j): 
      
    while board[i][j]!= 0: 
        if i<8: 
            i+= 1
        elif i == 8 and j<8: 
            i = 0
            j+= 1
        elif i == 8 and j == 8: 
            return True
    pygame.event.pump()     
    for it in range(1, 10): 
        if valid(board, i, j, it)== True: 
            board[i][j]= it 
            global x, y 
            x = i 
            y = j  
            screen.fill((WHITE)) 
            draw() 
            draw_box() 
            pygame.display.update() 
            pygame.time.delay(10) 
            if solve(board, i, j)== 1: 
                return True
            else: 
                board[i][j]= 0
            screen.fill((WHITE)) 
          
            draw() 
            draw_box() 
            pygame.display.update() 
            pygame.time.delay(10)     
    return False  
  
def instruction(): 
    text = fo2.render("PRESS C TO CLEAR FOR OWN PUZZLE ENTRY", 1, (LIME)) 
    text2 = fo2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (LIME)) 
    screen.blit(text, (20, 520))         
    screen.blit(text2, (20, 540)) 
  
def result(): 
    text = fo.render("FINISHED ", 1, (GREEN)) 
    screen.blit(text, (20, 570))     
run = True
flag1 = 0
flag2 = 0
r = 0
error = 0

while run: 
    screen.fill((WHITE))  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False       
        if event.type == pygame.MOUSEBUTTONDOWN: 
            flag1 = 1
            pos = pygame.mouse.get_pos() 
            get_cord(pos)     
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT: 
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP: 
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN: 
                y+= 1
                flag1 = 1    
            if event.key == pygame.K_1: 
                val = 1
            if event.key == pygame.K_2: 
                val = 2    
            if event.key == pygame.K_3: 
                val = 3
            if event.key == pygame.K_4: 
                val = 4
            if event.key == pygame.K_5: 
                val = 5
            if event.key == pygame.K_6: 
                val = 6 
            if event.key == pygame.K_7: 
                val = 7
            if event.key == pygame.K_8: 
                val = 8
            if event.key == pygame.K_9: 
                val = 9  
            if event.key == pygame.K_RETURN: 
                flag2 = 1    
            if event.key == pygame.K_c: 
                r = 0
                error = 0
                flag2 = 0
                board =[ 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0] 
                ]   
           
    if flag2 == 1: 
        if solve(board, 0, 0)== False: 
            error = 1
        else: 
            r = 1
        flag2 = 0    
    if val != 0:             
        draw_value(val)  
        if valid(board, int(x), int(y), val)== True: 
            board[int(x)][int(y)]= val 
            flag1 = 0
        else: 
            board[int(x)][int(y)]= 0
            error2()    
        val = 0    
        
    if error == 1: 
        error1()   
    if r == 1: 
        result()         
    draw()   
    if flag1 == 1: 
        draw_box()        
    instruction()     
    
    pygame.display.update()   
     
pygame.quit() 