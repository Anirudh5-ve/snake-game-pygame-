import pygame
from pygame.locals import *
import random

pygame.init()    # initialize pygame

# screen
screen_height = 500
screen_width = 500

screen = pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption('Snake game ani')
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None , 30)

# colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)


def text_screen(text):
    screen_text = font.render(text,True, black)
    screen.blit(screen_text,[10,10])

def plot_snake(screen,color,snake_lst,size):
    for x,y in snake_lst:
        pygame.draw.rect(screen,color,[x,y,size,size])

#exit_game = False

# ------------- GAME LOOP ----------------

def gameloop():
    exit_game = False
    game_over = False

    with open("highscore.txt","r") as f:
        highscore = f.read()
    
    # VARIABLES
    move_x = 10             # velocity
    move_y = 0              # velocity
    score = 0
    
    # SNAKE
    snake_x = screen_height/2
    snake_y = screen_width/2
    snake_size = 15

    # FOOD
    food_x = random.randint(0,screen_width)
    food_y = random.randint(0,screen_height)

    snake_len = 1
    snake_lst = []

    #exit_game = False   # run = True
    while  exit_game == False:
        screen.fill((0,200,100))
        
        if game_over :
            with open("highscore.txt","w") as f:
                f.write(highscore)

            screen.fill(white)
            text_screen('GAME OVER !! PRESS ENTER TO PLAY AGAIN !!')
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
            
                if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        move_x = 0
                        move_y = -10
                    elif event.key == K_DOWN:
                        move_x = 0
                        move_y = 10
                    elif event.key == K_RIGHT:
                        move_x = 10 
                        move_y = 0
                    elif event.key == K_LEFT:
                        move_x = -10
                        move_y = 0
                    

            snake_x += move_x
            snake_y += move_y
            
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                food_x = random.randint(0,screen_width)
                food_y = random.randint(0,screen_height)
                score += 10
                snake_len += 5
                #print('HIGHSCORE : ',highscore)
            
            if score > int(highscore):
                highscore = str(score)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)

            if len(snake_lst) > snake_len:
                del snake_lst[0]

            if head in snake_lst[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            text_screen('SCORE : ' + str(score) + '         HIGH SCORE : ' + highscore)
            #screen.fill((0,200,100))
            pygame.draw.rect(screen,red,[food_x,food_y,10,10])
            
            # pygame.draw.rect(screen,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(screen,black,snake_lst,snake_size)
        
        pygame.display.update()
        clock.tick(15)



    pygame.quit()   # end pygame

gameloop()