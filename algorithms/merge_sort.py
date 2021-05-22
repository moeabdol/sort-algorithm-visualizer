from display import draw_algorithm_step


def merge_sort(numbers, *args):
    left = args[0]
    right = args[1]

    if left < right:
        mid = int((left + right) / 2)
        merge_sort(numbers, left, mid)
        merge_sort(numbers, mid + 1, right)
        merge(numbers, left, mid, right)


def merge(numbers, left, mid, right):
    L = numbers[left:mid + 1]
    R = numbers[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        draw_algorithm_step(numbers, left + i, mid + j, left, right)

        if L[i] < R[j]:
            numbers[k] = L[i]
            i += 1
        else:
            numbers[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        numbers[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        numbers[k] = R[j]
        j += 1
        k += 1
