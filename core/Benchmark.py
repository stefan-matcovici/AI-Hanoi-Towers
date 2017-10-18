from algorithms import *
from datetime import datetime

class Benchmark:

    def __init__(self, no_rods, no_discs):
        """ Constructor """

        self.no_rods = no_rods
        self.no_discs = no_discs

        self.algorithms = ["A star", "Backtrack", "Hill climbing", "Random", "Random optimized", "Recursive backtrack"]

    def test(self):
        self.test_astar()
        self.test_backtracking()
        # self.test_backtracking_recursive()
        self.test_hillclimbing()
        self.test_random()
        self.test_random_optimized()

    def test_astar(self):
        print "***Benchmarking A Star algorithm***"
        algorithm = AStarAlgorithm(self.no_discs, self.no_rods)
        print self.get_execution_time(algorithm)
        self.get_solution_length(algorithm)

    def test_backtracking(self):
        print "***Benchmarking Backtracking algorithm***"
        algorithm = BacktrackAlgorithm(self.no_discs, self.no_rods)
        print self.get_execution_time(algorithm)
        self.get_solution_length(algorithm)

    def test_backtracking_recursive(self):
        print "***Benchmarking Recursive Backtracking algorithm***"
        algorithm = RecursiveBacktrackAlgorithm(self.no_discs, self.no_rods)
        print self.get_execution_time(algorithm)
        self.get_solution_length(algorithm)

    def test_hillclimbing(self):
        print "***Benchmarking Hill Climbing algorithm***"
        algorithm = HillClimbingAlgorithm(self.no_discs, self.no_rods)
        print self.get_execution_time(algorithm)
        self.get_solution_length(algorithm)

    def test_random(self):
        print "***Benchmarking Random algorithm***"
        algorithm = RandomAlgorithm(self.no_discs, self.no_rods)
        print self.get_execution_time(algorithm)
        self.get_solution_length(algorithm)

    def test_random_optimized(self):
        print "***Benchmarking Random Optimized algorithm***"
        algorithm = RandomOptimizedAlgorithm(self.no_discs, self.no_rods)
        print self.get_execution_time(algorithm)
        self.get_solution_length(algorithm)

    def get_execution_time(self, algorithm):
        start_time = datetime.now()
        algorithm.solve()
        end_time = datetime.now()
        return "Duration: {}".format(end_time - start_time)

    def get_solution_length(self, algorithm):
        print "Length of solution: " + str(algorithm.steps())
        print "Visited states: " + str(algorithm.visited_states)
