from algorithms import *
from algorithms import AStarAlgorithm

if __name__ == "__main__":
    # backtrack = BacktrackAlgorithm(5, 3, branch_bound=False)
    # backtrack.solve()
    # print backtrack.steps()

    # hillClimber = HillClimbingAlgorithm(4, 3)
    # hillClimber.solve()
    # print hillClimber.steps()

    astar = AStarAlgorithm.AStarAlgorithm(4,3)
    astar.solve()
    print astar.steps()

    # print "Random optimized:" + str(benchmark.avg_steps("random optimized", 4, 3, 30))
    # print "Random:" + str(benchmark.avg_steps("random", 4, 3, 30))
    # print "Backtracking:" + str(benchmark.avg_steps("backtracking", 4, 3, 30))
    # print "Hill climbing:" + str(benchmark.avg_steps("hill climbing", 4, 3, 30))
