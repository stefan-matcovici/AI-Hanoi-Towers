import random

from core import *


class HillClimbingAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, heuristic=2, restarts=100):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods)

        self.database = []
        self.moves = {}
        self.heuristic = None

        self.dead_ends = []
        self.restarts = restarts

        exec ("self.heuristic = self.heuristic" + str(heuristic))

        self.init_moves(no_discs, no_rods)

    def init_moves(self, no_discs, no_rods):
        """ Assign a number to every possible move """
        k = 0
        for i in xrange(no_discs):
            for j in xrange(no_rods):
                self.moves[k] = (i, j)
                k = k + 1

    def solve(self):
        self.current_state = self.initial_state

        while self.current_state != self.final_state:
            self.database.append(self.current_state)
            self.visit(self.current_state)

            # print [(x,self.heuristic(x)) for x in self.database]
            best_moves = []  # the moves that produce the best score
            best_score = float('+inf')  # the best score so far

            for move in self.moves.values():  # search all the possible moves
                current_score = self.anticipate_score(move)
                if current_score < best_score:  # if the anticipated score is the best so far, store it
                    best_score = current_score
                    best_moves = [move]
                elif current_score == best_score:
                    best_moves += [move]

            if best_score == float("+inf"):  # we reached a dead end
                if self.restarts == 0:  # out of restarts, we end
                    self.database = []
                    break
                self.dead_ends.append(self.current_state)  # mark it so the path doesn't go one more time
                self.database.pop()  # remove it from current path
                self.current_state = self.database.pop()  # restart path from previous state
                self.restarts -= 1
                continue

            random_move = random.choice(best_moves)  # choose randomly between moves with best scores
            self.current_state = self.current_state.move(random_move[0], random_move[1])  # choose the best score move

        if self.current_state == self.final_state:
            self.states = self.database + [self.current_state]

    def anticipate_score(self, move):
        """ Calculates the score for a move """
        if self.current_state.can_move(move[0], move[1]):  # if the move is valid
            temp_state = self.current_state.move(move[0], move[1])

            if temp_state in self.database or temp_state in self.dead_ends:  # check for cycles and dead ends
                return float('+inf')

            return self.heuristic(temp_state)
        else:  # invalid move
            return float('+inf')  # return the highest possible score
