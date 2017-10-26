import random

from core import *


class RandomAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, initial=[], final=[]):
        Algorithm.__init__(self, no_discs, no_rods, initial, final)

    def solve(self):

        while self.current_state != self.final_state:
            neighbours = self.valid_neighbours()
            self.visit(neighbours[random.randint(0, len(neighbours) - 1)])
            self.states.append(self.current_state)
