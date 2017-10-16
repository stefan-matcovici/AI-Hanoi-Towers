from algorithms import *
from algorithms import RandomOptimizedAlgorithm as randOptim
from copy import deepcopy
def avg_steps(algorithm,no_disks,no_rods,iterations):
    if algorithm.lower() == "random":
        alg = RandomAlgorithm(no_disks,no_rods)
    elif algorithm.lower() == "random optimized":
        alg = randOptim.RandomOptimizedAlgorithm(no_disks, no_rods)
    elif algorithm.lower() == "backtracking":
        alg = BacktrackAlgorithm(no_disks, no_rods,True)
    elif algorithm.lower() == "hill climbing":
        alg = HillClimbingAlgorithm(no_disks, no_rods)
    steps = 0
    iter = iterations
    while iter:
        alg.__init__(no_disks,no_rods)
        alg.solve()
        steps += alg.steps()
        iter -= 1
    return steps/iterations
