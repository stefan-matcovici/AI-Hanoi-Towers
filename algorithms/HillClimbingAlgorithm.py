from core import *


class HillClimbingAlgorithm(Algorithm):
    def __init__(self, no_discs, no_rods, heuristic=1):
        """ Overridden constructor """
        Algorithm.__init__(self, no_discs, no_rods)

        self.database = []
        self.moves = {}
        self.heuristic = None

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

            # print [self.heuristic(x) for x in self.database]
            best_move = -1  # the move that produces the best score
            best_score = float('+inf')  # the best score so far

            for move in self.moves.values():  # search all the possible moves
                current_score = self.anticipate_score(move)
                if current_score < best_score:  # if the anticipated score is the best so far, store it
                    current_score = best_score
                    best_move = move

            self.current_state = self.current_state.move(best_move[0], best_move[1])  # choose the best score move

        if self.current_state == self.final_state:
            self.states = self.database + [self.current_state]

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

    def anticipate_score(self, move):
        """ Calculates the score for a move """
        if self.current_state.can_move(move[0], move[1]):  # if the move is valid
            temp_state = self.current_state.move(move[0], move[1])

            if temp_state in self.database:  # check for cycles
                return float('+inf')

            return self.heuristic(temp_state)
        else:  # invalid move
            return float('+inf')  # return the highest possible score
