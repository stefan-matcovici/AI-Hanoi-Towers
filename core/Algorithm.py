import random
from copy import deepcopy
from State import State


class Algorithm:
    def __init__(self, no_discs, no_rods):
        """ Constructor """

        self.no_rods = no_rods
        self.no_discs = no_discs

        self.initial_state = self.__init_initial_state()
        self.final_state = self.__init_final_state()

        self.current_state = State(state=self.initial_state)
        self.states = []
        self.states.append(self.current_state)

    def __init_initial_state(self):
        """ Initialize the initial state with all the discs on the first rod """
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

    def move_to_next_random_state(self):
        """ Generates random disc and random rod until a move can be done and makes a valid move"""
        random_disc = random.randint(0, self.no_discs - 1)
        random_rod = random.randint(0, self.no_rods - 1)

        while not self.current_state.can_move(random_disc, random_rod):  # until a valid move can be done
            random_disc = random.randint(0, self.no_discs - 1)
            random_rod = random.randint(0, self.no_rods - 1)

        self.current_state = self.current_state.move(random_disc, random_rod)  # update current_state
        self.states.append(self.current_state)


    def list_all_possibilities(self):
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

    def steps(self):
        """ Returns the number of steps to reach the result """
        return len(self.states) - 1

    def solve(self):
        """ This method must be implemented and called to solve the problem """
        raise NotImplementedError('This is the method every algorithm has to implement')
