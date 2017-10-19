from core.Benchmark import Benchmark
from algorithms import *
if __name__ == "__main__":
    # no_discs = raw_input("Number of discs: ")
    # no_rods = raw_input("Number of rods: ")
    #
    # benchmark = Benchmark(int(no_discs), int(no_rods))
    # benchmark.test()
    randomoptim = RandomAlgorithm(4,3)
    randomoptim.solve()
    print randomoptim.steps()
    print randomoptim.states
    print len(randomoptim.visited_states)
