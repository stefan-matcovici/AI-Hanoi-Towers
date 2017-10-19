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


    def solve(self):
        found = False
        self.priorityQueue.put(self.initial_state,0)
        while not found and self.priorityQueue.qsize():
            closestChild = self.priorityQueue.get() # child with minimum h cost
            self.set_current_state(closestChild)
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