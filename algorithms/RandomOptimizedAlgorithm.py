from core import *
from copy import deepcopy
import random


class RandomOptimizedAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods):
        Algorithm.__init__(self, no_discs, no_rods)
        self.uniqueStates = []

    def solve(self):
        while not self.current_state.__eq__(self.final_state):
            possibilities = self.list_all_possibilities()
            is_state_visited = True
            while is_state_visited:
                is_state_visited = False
                if len(possibilities) > 0: #there are valid states that have not been visited
                    random_state = possibilities[random.randint(0, len(possibilities) - 1)]
                    for state in self.states:
                        if random_state.__eq__(state):
                            #continue the while loop till there is an unvisited valid state
                            is_state_visited = True
                            possibilities.remove(random_state)
                            break
                elif len(possibilities) == 0:#we are blocked and cannot move
                    possibilities = self.list_all_possibilities()
                    #allow revisiting a state
                    random_state = possibilities[random.randint(0, len(possibilities) - 1)]
            self.current_state = random_state
            self.states.append(self.current_state)
