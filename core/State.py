import copy


class State:
    def __init__(self, positions=None, state=None):
        """ Constructor """

        if state is not None:  # copy constructor
            self.positions = copy.deepcopy(state.positions)
        else:  # initialisation constructor
            self.positions = copy.deepcopy(positions)

    def move(self, disc, rod):
        """ Moves the disc to the rod and returns a newly created state """

        result = State(state=self)
        result.positions[disc] = rod

        return result

    def can_move(self, which, where):
        """ Checks if from the current state a transition of the disc 'which' is possible to the rod 'where' """

        if self.positions[which] == where:  # transition to the same rod
            return False

        for i in range(which):
            if self.positions[i] == self.positions[which]:  # any smaller discs are on the same rod
                return False
            if self.positions[i] == where:  # any smaller disc is on the 'where' rod
                return False

        return True

    def __str__(self):
        """ To string """
        return str(self.positions)

    def __eq__(self, other):
        """ Equal comparator """
        return self.positions == other.positions

    def __repr__(self):
        """ Representation for printing objects in lists"""
        return str(self)
