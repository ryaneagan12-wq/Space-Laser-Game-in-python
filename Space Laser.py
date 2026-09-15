import pygame
import random
import sys

pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1200
screen_img = pygame.image.load("space_background.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.blit(screen_img, (0, 0))
pygame.display.set_caption("Space Laser Game")
clock = pygame.time.Clock() 

player_height = 213
player_width = 322
player_x = 800
player_y = 800
player_speed = 35
space_ship_img = pygame.image.load("space_ship.png").convert_alpha()
space_ship = pygame.transform.scale(space_ship_img, (player_width, player_height))

laser_img = pygame.image.load("laser.png").convert_alpha()
laser_width = 10
laser_height = 101 
laser_speed = 20
laser = pygame.transform.scale(laser_img, (laser_width, laser_height))
laser_active = False
laser_x = player_x
laser_y = player_y


meteorite_img = pygame.image.load("meteorite.png").convert_alpha()
enemy_width = 146   
enemy_height = 144
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
enemy_y = -enemy_height
enemy_speed = 10
meteorite = pygame.transform.scale(meteorite_img, (enemy_width, enemy_height))

GREEN = (0, 255, 0)

score = 0
font = pygame.font.SysFont("Pixel", 40, bold=False)

game_over = False
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       
            running = False

    keys = pygame.key.get_pressed()
    
    if not game_over:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if player_y > 0:    
                    player_y -= player_speed           
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if player_x > 0:
                player_x -= player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if player_y < SCREEN_HEIGHT - player_height:
                player_y += player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
            if player_x < SCREEN_WIDTH - player_width:
                player_x += player_speed
        if keys[pygame.K_f]:
            if not laser_active:
                laser_x = player_x + (player_width // 2) - (laser_width // 2)   
                laser_y = player_y
                laser_active = True 
        if laser_active:
            laser_y -= laser_speed
            laser_rect = pygame.Rect(laser_x, laser_y, laser_width, laser_height)
            enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

            if laser_rect.colliderect(enemy_rect):
                score += 1 
                laser_active = False
                enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
                enemy_y = -enemy_height

            if laser_y < 0:
                laser_active = False

        enemy_y += enemy_speed
        if enemy_y > SCREEN_HEIGHT:
            enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
            enemy_y = -enemy_height

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        if player_rect.colliderect(enemy_rect):
            game_over = True

    screen.blit(screen_img, (0,0))
    screen.blit(space_ship, (player_x, player_y))
    screen.blit(meteorite, (enemy_x, enemy_y ))

    if laser_active:
        screen.blit(laser_img, (laser_x, laser_y))

    if not game_over:
        score_surf = font.render(f"Score: {score}", True, GREEN)
        message_x = 325
        message_y = 200
        screen.blit(score_surf, (message_x,message_y))
    else:
        over_surf = font.render(f"Final Score: {score}", True, GREEN)
        text_x = (SCREEN_WIDTH // 2) - (over_surf.get_width() // 2)
        text_y = (SCREEN_HEIGHT // 2) - (over_surf.get_height() // 2)
        screen.blit(over_surf, (text_x, text_y))
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
