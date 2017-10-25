import random

from core import *


class RandomOptimizedAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, restarts=1000, initial=[]):
        Algorithm.__init__(self, no_discs, no_rods, initial)
        self.dead_ends = []
        self.restarts = restarts
        self.restarts_so_far = 0

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
                if self.restarts_so_far < self.restarts:
                    self.restarts_so_far += 1
                    self.dead_ends.append(self.current_state)
                    go_back = random.randint(0,len(self.states)-1)
                    while go_back:
                        self.states.pop()
                        go_back -=1
                    self.visit(self.states[-1])
                    self.states.pop()
                else:
                    print "Exceded number of restarts"
                    break
            else:
                self.visit(neighbours[random.randint(0, len(neighbours) - 1)])
                self.states.append(self.current_state)

