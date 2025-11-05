import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    pygame_module_init_pass, pygame_module_init_fail = pygame.init()
    print("Pygame Initialization")
    print(f"Modules Passed: {pygame_module_init_pass}, Modules Failed: {pygame_module_init_fail}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:         #GAME LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0,0,0))


        pygame.display.flip()

if __name__ == "__main__":
    main()
