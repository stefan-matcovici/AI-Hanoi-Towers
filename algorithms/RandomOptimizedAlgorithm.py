import random

from core import *


class RandomOptimizedAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, restarts=10000, initial=[], final=[]):
        Algorithm.__init__(self, no_discs, no_rods, initial, final)
        self.dead_ends = []
        self.restarts = restarts
        self.restarts_so_far = 0

        self.intermediate_states = [self.current_state]

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
                    self.go_back2()
                else:
                    self.states = []
                    break
            else:
                self.visit(neighbours[random.randint(0, len(neighbours) - 1)])
                self.check_intermediate(self.current_state)
                self.states.append(self.current_state)

    def go_back2(self):
        if not self.intermediate_states or len(self.intermediate_states) <= 1:
            return

        rand_state = random.choice(self.intermediate_states[1:])

        while self.current_state != rand_state and self.states:
            self.current_state = self.states.pop()
            if self.current_state in self.intermediate_states:
                self.intermediate_states.remove(self.current_state)

        self.states.append(self.current_state)

    def go_back1(self):
        if not self.states:
            return

        go_back = random.randint(0, len(self.states) - 1)
        while go_back:
            self.states.pop()
            go_back -= 1
        self.visit(self.states[-1])
        self.states.pop()

    def check_intermediate(self, state):
        if self.compute_intermediate_score(state) > 0:
            self.intermediate_states.append(state)

    def compute_intermediate_score(self, state):
        score = 0
        i = self.no_discs - 1
        while state.positions[i] == self.no_rods - 1 and i >= 0:
            i = i - 1
            score = score + 1

        return score
