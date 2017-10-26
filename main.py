from algorithms import *
if __name__ == "__main__":
    """TODO: implement custom initial state and final state
             implement random optimized with custom backsteps (intermediate steps)
             hillclimbing: euristica
             astar: from final state to initial state
    """

    # hanoi.HanoiApp().run()
    astar = RandomOptimizedAlgorithm(3, 3)
    astar.solve()
    print astar.steps()
    print astar.states
