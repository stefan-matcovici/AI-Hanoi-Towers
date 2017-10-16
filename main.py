from algorithms import *

if __name__ == "__main__":
    # backtrack = BacktrackAlgorithm(5, 3, branch_bound=True)
    # backtrack.solve()
    # print backtrack.steps()

    hillClimber = HillClimbingAlgorithm(5, 3)
    hillClimber.solve()
    print hillClimber.steps()
