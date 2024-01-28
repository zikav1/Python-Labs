import numpy as np
import random

class MemoryCard:
    def __init__(self, front_filename, back_filename):
        self._front_filename = front_filename
        self._back_filename = back_filename
        self._front_up = False

    def current_side_up(self):
        if self._front_up:
            return self._front_filename
        else:
            return self._back_filename

    def is_front_up(self):
        return self._front_up

    def has_same_front(self, other_card):
        return self._front_filename == other_card._front_filename

    def flip(self):
        self._front_up = not(self._front_up)

    def __str__(self):
        return f'Card(is_front_up={self._front_up}, front={self._front_filename}, back={self._back_filename})'

    def __repr__(self):
        return str(self)
