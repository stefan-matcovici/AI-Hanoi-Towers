from core import *


class RandomAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods):
        Algorithm.__init__(self, no_discs, no_rods)

    def solve(self):

        while not self.current_state.__eq__(self.final_state):
            self.move_to_next_random_state()
