import random
from Queue import PriorityQueue
from copy import deepcopy
from core import *


class AStarAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, heuristic=1, restarts=10):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods)

        self.priorityQueue = PriorityQueue()
        self.parentDict = {}
        self.costDict = {}
        self.heuristic = None
        exec ("self.heuristic = self.heuristic" + str(heuristic))

    def calculate_cost(self,state):
        temp_state = deepcopy(state)
        score = 0
        while temp_state != self.initial_state:
            temp_state = self.parentDict[temp_state]
            score += 1
        return score

    def solve(self):
        found = False
        self.priorityQueue.put(self.initial_state,0)
        while not found and self.priorityQueue.qsize():
            closest_child = self.priorityQueue.get() # child with minimum h cost
            children = self.valid_neighbours() # all neighbours
            self.visit(closest_child)
            for child in children:
                if child not in self.visited_states:
                    self.parentDict[child] = self.current_state #mark the states route
                    if child == self.final_state:
                        found = True
                        break
                    heuristic = self.heuristic(child)
                    cost = self.calculate_cost(child)
                    self.priorityQueue.put(child,heuristic + cost)
        #build the states from the parentdictionary
        state = self.final_state
        self.states = list()
        while state!= self.initial_state:
            self.states.append(state)
            state = self.parentDict[state]
        self.states.append(self.initial_state)
        self.states.reverse()