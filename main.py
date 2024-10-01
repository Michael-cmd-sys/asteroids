import pygame 
from constants import *

def main():
   print("Starting asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   is_running = True
   while is_running:
       screen.fill((0, 0, 0))
       display.flip()

if __name__ == "__main__":
    main()
