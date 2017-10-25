from copy import deepcopy

from State import State


class Algorithm:
    def __init__(self, no_discs, no_rods, initial):
        """ Constructor """

        self.no_rods = no_rods
        self.no_discs = no_discs

        self.initial_state = self.__init_initial_state(initial)
        self.final_state = self.__init_final_state()

        self.current_state = State(state=self.initial_state)
        self.states = []
        self.states.append(self.current_state)
        self.visited_states = []
        self.visited_states.append(self.initial_state)

    def __init_initial_state(self, initial):
        """ Initialize the initial state with all the discs on the first rod """
        if len(initial) != 0:
            return State(initial)
        arr = []
        for i in range(self.no_discs):
            arr.append(0)
        return State(arr)

    def __init_final_state(self):
        """ Initialize the final state with all the discs on the last rod """
        arr = []
        for i in range(self.no_discs):
            arr.append(self.no_rods - 1)
        return State(arr)

    def valid_neighbours(self):
        """Lists all possible(valid) states from the current one"""
        possibilities = []
        for which in range(self.no_discs):
            for where in range(self.no_rods):
                if self.current_state.can_move(which,where):
                    positions = deepcopy(self.current_state.positions)
                    positions[which] = where
                    state = State(positions)
                    possibilities.append(state)
        return possibilities

    def visit(self,state):
        self.current_state = state
        self.visited_states.append(self.current_state)

    def steps(self):
        """ Returns the number of steps to reach the result """
        return len(self.states) - 1

    def get_visited_states(self):
        return self.visited_states

    def heuristic1(self, state):
        """ Add to the score the difference between final rod and current rod """
        score = 0
        for disc in state.positions:
            score = score + disc - self.no_rods - 1

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

    def heuristic4(self, state):
        """Ponderated sum"""
        score = 0
        for i in range(self.no_discs):
            score = score + state.positions[i] * (i + 1)
        return score

    def solve(self):
        """ This method must be implemented and called to solve the problem """
        raise NotImplementedError('This is the method every algorithm has to implement')
