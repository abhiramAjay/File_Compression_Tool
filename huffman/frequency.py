from collections import Counter
import sys
import os

def read_file_and_count_frequencies(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File '{filename}' does not exist.")

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    frequency = Counter(text)
    return frequency