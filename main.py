from algorithms import *
from algorithms import RandomOptimizedAlgorithm as roptim
import benchmark
if __name__ == "__main__":
    # backtrack = BacktrackAlgorithm(5, 3, branch_bound=True)
    # backtrack.solve()
    # print backtrack.steps()

    # hillClimber = HillClimbingAlgorithm(5, 3)
    # hillClimber.solve()
    #print hillClimber.steps()

    print "Random optimized:" + str(benchmark.avg_steps("random optimized", 4, 3, 30))
    print "Random:" + str(benchmark.avg_steps("random", 4, 3, 30))
