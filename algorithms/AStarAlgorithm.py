from Queue import PriorityQueue

from core import *


class AStarAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, heuristic=1, restarts=10, initial=[], final=[]):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods, initial, final)

        self.priorityQueue = PriorityQueue()
        self.state_cost = {}
        self.state_score = {}
        self.came_from = {}
        self.heuristic = None
        exec ("self.heuristic = self.heuristic" + str(heuristic))


    def solve(self):
        found = False
        self.priorityQueue.put((0,self.initial_state))
        self.came_from[self.initial_state] = self.initial_state
        self.state_cost[self.initial_state] = 0
        while not found and self.priorityQueue.qsize():
            closest_child = self.priorityQueue.get()[1] # child with minimum h cost
            self.visit(closest_child)
            children = self.valid_neighbours() # all neighbours
            for child in children:
                self.state_cost[child] = self.state_cost[self.current_state]+1
                score = self.heuristic(child) + self.state_cost[child]
                if not self.state_score.get(child) or score < self.state_score.get(child):
                    self.state_score[child] = score
                    self.priorityQueue.put((score,child))
                    self.came_from[child] = self.current_state

        #build the states from the came_fromionary
        state = self.final_state
        self.states = list()
        while state!= self.initial_state:
            self.states.append(state)
            state = self.came_from[state]
        self.states.append(self.initial_state)
        self.states.reverse()