from core import *


class BacktrackAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, branch_bound=False, initial=[], final=[]):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods, initial, final)

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

    def backtrack(self):
        """ Backtrack step """
        self.database.pop()

    def solve(self):
        self.database.append([self.initial_state, 0])  # push the initial state

        while self.database:
            if self.limit and len(self.database) >= self.limit:
                self.backtrack()

            self.current_state, move = self.database[-1]  # get latest state pushed
            self.visit(self.current_state)

            if self.current_state == self.final_state:  # we reached a solution
                # print [x[0] for x in self.database]           # print the path
                self.states = [x[0] for x in self.database]
                break

            next_state = None
            while move < len(self.moves):  # as long as there are possible moves
                if self.current_state.can_move(self.moves[move][0], self.moves[move][1]):  # the current move is valid
                    next_state = self.current_state.move(self.moves[move][0], self.moves[move][1])  # try the move
                    if next_state not in [x[0] for x in self.database] and next_state not in self.visited_states:
                        break
                move = move + 1

            if move >= len(self.moves):  # no more possible moves
                self.backtrack()
                continue

            self.database[-1][1] = move + 1  # update last state with next move to try
            self.database.append([next_state, 0])  # push the new state with first move to try
