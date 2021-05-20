import pygame
import display
from algs import algorithm_dict

def main():
    display.algorithm_box.add_options(list(algorithm_dict.keys()))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            display.update_ui(event)

        display.draw_ui()

if __name__ == "__main__":
    main()
