import pygame
from player import Player
from constants import *

def main():
    print("Starting Asteroids!")

    pygame_module_init_pass, pygame_module_init_fail = pygame.init()
    print("Pygame Initialization")
    print(f"Modules Passed: {pygame_module_init_pass}, Modules Failed: {pygame_module_init_fail}")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    main_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:         #GAME LOOP
        #print("Entering Game Loop")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        main_player.update(dt)

        screen.fill(color="black")
        main_player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
