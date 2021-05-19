import pygame
import display

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            display.update_ui(event)
        display.draw_ui()

if __name__ == "__main__":
    main()
