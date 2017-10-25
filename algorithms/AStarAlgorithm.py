from Queue import PriorityQueue
from copy import deepcopy

from core import *


class AStarAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, heuristic=1, restarts=10, initial=[]):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods, initial)

        self.priorityQueue = PriorityQueue()
        self.parentDict = {}
        self.costDict = {}
        self.costDict[self.initial_state] = 0
        self.heuristic = None
        exec ("self.heuristic = self.heuristic" + str(heuristic))

    def calculate_cost(self,state):
        temp_state = deepcopy(state)
        cost = 0
        while temp_state != self.initial_state:
            temp_state = self.parentDict[temp_state]
            cost += 1
        return cost

    def calculate_score(self,state):
        return self.heuristic(state)+self.calculate_cost(state)

    def solve(self):
        found = False
        count = 0
        self.priorityQueue.put((0,self.initial_state))
        while not found and self.priorityQueue.qsize():
            closest_child = self.priorityQueue.get()[1] # child with minimum h cost
            self.visit(closest_child)
            children = self.valid_neighbours() # all neighbours
            for child in children:
                if child not in self.visited_states:
                    self.parentDict[child] = self.current_state #mark the states route
                    if child == self.final_state:
                        found = True
                        break
                    score = self.calculate_score(child)
                    self.costDict[child] = score
                    self.priorityQueue.put((score,child))
                else:
                    score = self.calculate_score(child)
                    if self.costDict[child] < score:
                        count += 1
                        print len(self.visited_states)
                        self.costDict[child] = score
                        self.priorityQueue.put((score, child))

        #build the states from the parentdictionary
        state = self.final_state
        self.states = list()
        while state!= self.initial_state:
            self.states.append(state)
            state = self.parentDict[state]
        self.states.append(self.initial_state)
        self.states.reverse()
        print count