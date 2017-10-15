from algorithms import *

if __name__ == "__main__":
    backtrack = BacktrackAlgorithm(3, 3, branch_bound=True)
    backtrack.solve()
    print backtrack.steps()
