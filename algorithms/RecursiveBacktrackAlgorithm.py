from core import *


class RecursiveBacktrackAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, branch_bound=False, initial=[]):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods, initial)

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

    def search(self, path):
        state = path[-1]
        self.visit(state)

        if state == self.final_state:  # we reached a solution
            self.states = path
            return True

        for move in self.moves.values():  # as long as there are possible moves
            if state.can_move(move[0], move[1]):  # the current move is valid
                next_state = state.move(move[0], move[1])
                if next_state not in path and next_state not in self.visited_states:  # check for cycles
                    path.append(next_state)
                    result = self.search(path[:])
                    if result:  # successful
                        return True
                    path.pop()

        path.pop()
        return False

    def solve(self):
        self.search([self.initial_state])
