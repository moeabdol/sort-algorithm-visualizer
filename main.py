import pygame
import display
from algs import algorithm_dict, run_algorithm 
from random import randint


def main():
    numbers = []
    running = True
    display.algorithm_box.add_options(list(algorithm_dict.keys()))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            display.update_ui(event)
            a_set = set(range(display.num_bars))

            if display.start_button.active:
                display.num_bars = int(display.size_box.text)
                display.delay = display.delay_box.value - display.delay_box.rect.x - 6
                algorithm = display.algorithm_box.get_active_option()

                # Generate random list of numbers
                numbers = [randint(10, 400) for i in range(display.num_bars)]
                run_algorithm(algorithm.lower(), numbers)
                display.to_draw = True

        display.draw_ui(numbers, -1, -1, -1, -1, green_rows=a_set)


if __name__ == "__main__":
    main()
