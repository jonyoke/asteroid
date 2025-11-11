import pygame
from player import Player
from logger import log_state
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame_module_init_pass, pygame_module_init_fail = pygame.init()
    print("Pygame Initialization")
    print(f"Modules Passed: {pygame_module_init_pass}, Modules Failed: {pygame_module_init_fail}")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    

    main_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:         #GAME LOOP
        log_state()

        #print("Entering Game Loop")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updatable.update(dt)
        #main_player.update(dt)

        screen.fill(color="black")
        for drawble in drawable:
            drawble.draw(screen)
        #main_player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
