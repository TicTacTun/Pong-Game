import pygame, sys, random

def ball_animation():
  global ball_speed_x, ball_speed_y, player_score, opponent_score
  ball.x += ball_speed_x
  ball.y += ball_speed_y
    
  if ball.top <= 0 or ball.bottom >= height:
    ball_speed_y *= -1 # Reverse the ball speed when collide with the border
  if ball.left <= 0: 
    player_score += 1
    ball_restart()
  if ball.right >= width:
    opponent_score += 1
    ball_restart() # If ball hit any left/right wall, it will reset
  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_x *= -1 # Reverse the ball speed when collide with the sticks

def player_animation():
  player.y += player_speed
  if player.top <= 0:
    player.top = 0
  if player.bottom >= height:
    player.bottom = height

def opponent_animation():
  if opponent.top < ball.y:
    opponent.top += opponent_speed
  if opponent.bottom > ball.y:
    opponent.bottom -= opponent_speed
  if opponent.top <= 0:
    opponent.top = 0
  if opponent.bottom >= height:
    opponent.bottom = height

def ball_restart():
  global ball_speed_x, ball_speed_y
  ball.center = (width/2, height/2)
  ball_speed_y *= random.choice((1,-1)) 
  ball_speed_x *= random.choice((1,-1)) # After restart, ball starts with random pos
    

# General setup
pygame.init() # initiate all the pygame module
clock =  pygame.time.Clock()

# Setting up the main window
width = 1280
height = 960
screen = pygame.display.set_mode((width, height)) # Display surface
pygame.display.set_caption('Pong Game')

# Game Rectangles
ball = pygame.Rect(width/2 - 15, height/2 - 15, 30, 30) # (x, y, width, height)
player = pygame.Rect(width - 20, height/2 - 70, 10, 140)
opponent = pygame.Rect(10, height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12') # color of the background
light_grey = (200,200,200) # (R,G,B)

ball_speed_x = 7 * random.choice((1,-1)) # Define horizontal ball speed
ball_speed_y = 7 * random.choice((1,-1)) # Define vertical ball speed
player_speed = 0
opponent_speed = 7 # Change the value to change difficulty

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("Koulen-Regular.ttf", 48) # (font name, size)

while True:
    # Handling the input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Fix the event type check
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN: 
           if event.key == pygame.K_DOWN: # Mention the down arrow
              player_speed += 7
           if event.key == pygame.K_UP: # Mention the upper arrow
              player_speed -= 7
        if event.type == pygame.KEYUP: 
           if event.key == pygame.K_DOWN: # Mention the down arrow
              player_speed -= 7
           if event.key == pygame.K_UP: # Mention the upper arrow
              player_speed += 7
   
    # Game logics
    ball_animation()
    player_animation()
    opponent_animation()
    
    # Drawing
    screen.fill(bg_color) 
    pygame.draw.rect(screen, light_grey, player) # (surface, color, rect)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (width/2, 0), (width/2, height)) # (surface, color, tuple of startpoint, tuple of endpoint)

    player_text = game_font.render(f"{player_score}", False, light_grey) # (argument, True/False, color)
    screen.blit(player_text,(670,460))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey) # (argument, True/False, color)
    screen.blit(opponent_text,(590,460))

    # Updating the window
    pygame.display.flip()
    clock.tick(60) # 60 frames per second (mention how fast the loop works)
