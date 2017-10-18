import random
from Queue import PriorityQueue
from copy import deepcopy
from core import *


class AStarAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, heuristic=3, restarts=10):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods)

        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.parentDict = {}
        self.heuristic = None

        exec ("self.heuristic = self.heuristic" + str(heuristic))


    def heuristic1(self, state):
        """ Add to the score the difference between final rod and current rod """
        score = 0
        for disc in state.positions:
            score = score + self.no_rods - 1 - disc

        return score

    def heuristic2(self, state):
        """ Add one to the score for every disc that is not on the final rod"""
        score = 0
        for disc in state.positions:
            score = score + (1 if disc != self.no_rods - 1 else 0)

        return score

    def heuristic3(self, state):
        """ Add one to the score for every disc that is not on top of the right disc or rod in case of the first disc"""
        score = 0
        for i in range(self.no_discs):
            if i == 0 and self.current_state.positions[i] != (self.no_rods - 1):
                score = score + 1
            elif self.current_state.positions[i] != self.current_state.positions[i - 1]:
                score = score + 1

        return score

    def solve(self):
        found = False
        self.priorityQueue.put(self.initial_state,0)
        while not found and self.priorityQueue.qsize():
            closestChild = self.priorityQueue.get() # child with minimum h cost
            self.current_state = closestChild
            children = self.list_all_possibilities() # all neighbours
            self.visitedQueue.append(closestChild)
            for child in children:
                if child not in self.visitedQueue:
                    self.parentDict[child] = self.current_state #mark the states route
                    if child.__eq__(self.final_state):
                        found = True
                        break
                    priority = self.heuristic(child)
                    self.priorityQueue.put(child,priority)
        #build the states from the parentdictionary
        state = self.final_state
        self.states = list()
        while state!= self.initial_state:
            self.states.append(state)
            state = self.parentDict[state]
        self.states.append(self.initial_state)
        self.states.reverse()