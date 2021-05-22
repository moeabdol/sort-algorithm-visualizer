from algorithms.binary_insertion_sort import binary_insertion_sort
from algorithms.bitonic_sort import bitonic_sort
from algorithms.bogo_sort import bogo_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.bucket_sort import bucket_sort
from algorithms.cocktail_sort import cocktail_sort
from algorithms.comb_sort import comb_sort
from algorithms.counting_sort import counting_sort
from algorithms.cycle_sort import cycle_sort
from algorithms.gnome_sort import gnome_sort
from algorithms.heap_sort import heap_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.odd_even_sort import odd_even_sort
from algorithms.pancake_sort import pancake_sort
from algorithms.quick_sort import quick_sort
from algorithms.radix_sort import radix_sort
from algorithms.selection_sort import selection_sort
from algorithms.shell_sort import shell_sort
from algorithms.stooge_sort import stooge_sort
from algorithms.strand_sort import strand_sort
from algorithms.tim_sort import tim_sort

algorithm_dict = {
    "binary insertion": binary_insertion_sort,
    "bitonic": bitonic_sort,
    "bogo": bogo_sort,
    "bubble": bubble_sort,
    "bucket": bucket_sort,
    "cocktail": cocktail_sort,
    "comb": comb_sort,
    "counting": counting_sort,
    "cycle": cycle_sort,
    "gnome": gnome_sort,
    "heap": heap_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "odd even": odd_even_sort,
    "pancake": pancake_sort,
    "quick": quick_sort,
    "radix": radix_sort,
    "selection": selection_sort,
    "shell": shell_sort,
    "stooge": stooge_sort,
    "strand": strand_sort,
    "tim": tim_sort,
}


def run_algorithm(algorithm, numbers):
    return algorithm_dict[algorithm](numbers, 0, len(numbers) - 1)
