from core import HanoiApp as hanoi

if __name__ == "__main__":
    """TODO: implement custom initial state and final state
             implement random optimized with custom backsteps (intermediate steps)
             hillclimbing: euristica
             astar: from final state to initial state
    """

    hanoi.HanoiApp().run()
    # rand_opt = RandomOptimizedAlgorithm(6, 3)
    # rand_opt.solve()
    # print rand_opt.steps()
