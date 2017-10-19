from core import *
from copy import deepcopy
import random


class RandomOptimizedAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods):
        Algorithm.__init__(self, no_discs, no_rods)
        self.dead_ends = []

    def unvisited_neighbours(self):
        neighbours = self.valid_neighbours()
        result = []
        for state in neighbours:
            if state not in self.states:
                result.append(state)
        return result

    def neighbours(self):
        unvisited = self.unvisited_neighbours()
        result = []
        for state in unvisited:
            if state not in self.dead_ends:
                result.append(state)
        return result
    def solve(self):
        while self.current_state != self.final_state:
            neighbours = self.neighbours()
            if len(neighbours) == 0:
                self.dead_ends.append(self.current_state)
                self.visit(self.states[-1])
                self.states.pop()
            else:
                self.visit(neighbours[random.randint(0, len(neighbours) - 1)])
                self.states.append(self.current_state)

