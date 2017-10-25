from algorithms import *

if __name__ == "__main__":
    """TODO: implement custom initial state and final state
             implement random optimized with custom backsteps (intermediate steps)
             hillclimbing: consider current state score
                           sum, prod, ponderat
                           scadere scor doar o tranzitie
             astar: from final state to initial state
    """

    # no_discs = raw_input("Number of discs: ")
    # no_rods = raw_input("Number of rods: ")
    #
    # benchmark = Benchmark(int(no_discs), int(no_rods))
    # benchmark.test()

    hill = HillClimbingAlgorithm(5, 3)
    hill.solve()
    print hill.steps()
