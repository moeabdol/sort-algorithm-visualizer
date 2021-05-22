from display import draw_algorithm_step
from random import randint


def partition(array, start, end, pi):
    array[start], array[pi] = array[pi], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        draw_algorithm_step(array, j, end, i, -1)
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def quick_sort(array, start, end):
    if end - start < 1:
        return

    pi = randint(start, end)
    pi = partition(array, start, end, pi)
    quick_sort(array, start, pi - 1)
    quick_sort(array, pi + 1, end)
