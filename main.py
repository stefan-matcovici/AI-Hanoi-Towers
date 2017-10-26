from core import HanoiApp as hanoi

if __name__ == "__main__":
    """TODO: implement custom initial state and final state
             implement random optimized with custom backsteps (intermediate steps)
             hillclimbing: euristica
             astar: from final state to initial state
    """

    hanoi.HanoiApp().run()
    # astar = AStarAlgorithm(4, 4, 1)
    # astar.solve()
    # print astar.steps()
