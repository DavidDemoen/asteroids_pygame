import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

VERSION = pygame.version.ver

def main():
    print(f"Starting Asteroids! with pygame version: {VERSION}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0   

    while(True):
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        time_in_ms = clock.tick(60)
        dt = time_in_ms / 1000.0

if __name__ == "__main__":
    main()
