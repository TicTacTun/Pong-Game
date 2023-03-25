import pygame, sys, random

def ball_animation():
  global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
  ball.x += ball_speed_x
  ball.y += ball_speed_y
    
  if ball.top <= 0 or ball.bottom >= height:
    ball_speed_y *= -1 # Reverse the ball speed when collide with the border
  
  if ball.left <= 0: 
    player_score += 1
    score_time = pygame.time.get_ticks()
  
  if ball.right >= width:
    opponent_score += 1
    score_time = pygame.time.get_ticks()
  
  if ball.colliderect(player) and ball_speed_x > 0:
    if abs(ball.right - player.left) < 10: # Make sure the ball hits the left side of the stick
      ball_speed_x *= -1 # Reverse the ball speed when collide with the sticks
    elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0: # Make sure ball hits the top
      ball_speed_y *= -1
    elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0: # Make sure ball hits the bottom
      ball_speed_y *= -1


  if ball.colliderect(opponent) and ball_speed_x < 0:
    if abs(ball.left - opponent.right) < 10:
      ball_speed_x *= -1
    elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
      ball_speed_y *= -1
    elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
      ball_speed_y *= -1

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
  global ball_speed_x, ball_speed_y, current_time, score_time

  current_time = pygame.time.get_ticks()
  ball.center = (width/2, height/2)

  if current_time - score_time < 700:
    countdown_three = game_font.render("Ready", False, light_grey)
    screen.blit(countdown_three, (width/2 - 30, height/2 + 20))
  if 700 < current_time - score_time < 1400:
    countdown_two = game_font.render(" Set", False, light_grey)
    screen.blit(countdown_two, (width/2 - 30, height/2 + 20))
  if 1400 < current_time - score_time < 2100:
    countdown_one = game_font.render("  Go", False, light_grey)
    screen.blit(countdown_one, (width/2 - 30, height/2 + 20))

  if current_time - score_time < 2100:
    ball_speed_x = 0 
    ball_speed_y = 0
  else:
    ball_speed_y = 7 * random.choice((1,-1)) 
    ball_speed_x = 7 * random.choice((1,-1)) # After restart, ball starts with random pos
    score_time = None
    
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
game_font = pygame.font.Font("E:\Python\pygame\Pong-Game\Koulen-Regular.ttf", 32) # (font name, size)

# Timer
score_time = True

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

    if score_time:
      ball_restart()

    player_text = game_font.render(f"{player_score}", False, light_grey) # (argument, True/False, color)
    screen.blit(player_text,(670,460))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey) # (argument, True/False, color)
    screen.blit(opponent_text,(590,460))

    # Updating the window
    pygame.display.flip()
    clock.tick(60) # 60 frames per second (mention how fast the loop works)
