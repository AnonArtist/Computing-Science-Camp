import pygame
import random
import time

def collision_with_boundaries(snake_head):

    if snake_head[0]>=display_width or snake_head[0]<0 or snake_head[1]>=display_height or snake_head[1]<0:
        return 1
    else:
        return 0

def generate_snake(snake_head, snake_position, button_direction):

    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10
        
    snake_position.insert(0,list(snake_head))
    snake_position.pop()
    return snake_position

def display_snake(snake_position):

    for position in snake_position:
        pygame.draw.rect(display,player_color,pygame.Rect(position[0],position[1],10,10))

def play_game(snake_head, snake_position, button_direction):
    crashed = False
    while crashed is not True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button_direction = 0
                elif event.key == pygame.K_RIGHT:
                    button_direction = 1
                elif event.key == pygame.K_UP:
                    button_direction = 3
                elif event.key == pygame.K_DOWN:
                    button_direction = 2

        snake_position = generate_snake(snake_head, snake_position, button_direction)
        
        display.fill(window_color)
        display_snake(snake_position)
        pygame.display.update()

        if collision_with_boundaries(snake_head) == 1:
            crashed = True

        clock.tick(20)

if __name__ == "__main__":

    display_width = 500
    display_height = 500
    player_color = (115,194,251)
    window_color = (0,0,0)
    clock=pygame.time.Clock()

    snake_head = [250,250]
    snake_position = [[250,250],[240,250],[230,250]]
   
    pygame.init()

    display = pygame.display.set_mode((display_width,display_height))
    display.fill(window_color)
    pygame.display.set_caption("Snake Game")
    pygame.display.update()

    play_game(snake_head, snake_position, 1)
    pygame.quit()