import copy

from core import *


class RecursiveBacktrackAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, branch_bound=False):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods)

        self.database = []
        self.moves = {}

        self.limit = None
        self.branch_bound = branch_bound

        self.init_moves(no_discs, no_rods)

    def init_moves(self, no_discs, no_rods):
        """ Assign a number to every possible move """
        k = 0
        for i in xrange(no_discs):
            for j in xrange(no_rods):
                self.moves[k] = (i, j)
                k = k + 1

    def search(self, state):
        self.database.append(state)

        if state == self.final_state:  # we reached a solution
            # print self.database
            if self.branch_bound:
                if not self.limit:
                    self.limit = len(self.database)
                elif len(self.database) < self.limit:
                    self.states = copy.deepcopy(self.database)
                    self.limit = len(self.database)
            else:
                self.states = copy.deepcopy(self.database)
            self.database.pop()
            return None

        for i in xrange(0, len(self.moves)):  # as long as there are possible moves
            if state.can_move(self.moves[i][0], self.moves[i][1]):  # the current move is valid
                next_state = state.move(self.moves[i][0], self.moves[i][1])
                if next_state not in self.database:  # check for cycles
                    result = self.search(next_state)
                    if result:  # try the move
                        print result,
                        self.database.pop()
                        return state
        self.database.pop()
        return None

    def solve(self):
        self.search(self.initial_state)
