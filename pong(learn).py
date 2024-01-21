import pygame, sys, random


def ball_animation():
    global ball_speed_x
    global ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
        
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
        
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))
# this makes sure that anything you do in pygame runs
pygame.init()
clock = pygame.time.Clock()

# setting up the dimensions for the pop up window

screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
# to give the window a title 
pygame.display.set_caption("Pong")

# game rectangles
# to place the ball in the middle of the screen, divide the width and height by 2, since the screen is of centered, - that number by the half the ball in this case 15 would center it
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

bg_color = pygame.Color('grey12')
mys = (213,150, 200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7* random.choice((1,-1))
player_speed = 0
opponent_speed = 7


# loops handle movement for pygame and makes it appear that things are moving

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            
            
    ball_animation()
    player_animation()
    opponent_ai()


    pygame.display.flip()
    clock.tick(60)

    screen.fill(bg_color)
    pygame.draw.rect(screen, mys, player)
    pygame.draw.rect(screen, mys, opponent)
    pygame.draw.ellipse(screen, mys, ball)
    pygame.draw.aaline(screen, mys, (screen_width / 2, 0), (screen_width / 2, screen_height))

        # this will make sure that the window updates according to user input
        # the 60 marks how many frame the computer will display the window at, if left empty if may result in an empty screen
        #screen.fill makes sure that the background of the window is filled, without it you would not be able to see
        # The order of the code plays a part in how it is displayed, if I were to put the screen fill code after drawing the middle line, we would not see the middle line
        # the priority is top first bottom last, or fifo ????
        # visuals 

