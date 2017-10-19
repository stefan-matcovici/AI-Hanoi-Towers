from datetime import datetime
from datetime import timedelta

from algorithms import *


class Benchmark:
    def __init__(self, no_rods, no_discs, no_iter=10):
        """ Constructor """

        self.no_rods = no_rods
        self.no_discs = no_discs
        self.no_iter = no_iter

        self.algorithms = ["A star", "Backtrack", "Hill climbing", "Random", "Random optimized", "Recursive backtrack"]

    def test(self):
        # self.test_astar()
        self.test_backtracking()
        self.test_backtracking_recursive()
        self.test_hillclimbing()
        self.test_random()
        self.test_random_optimized()

    def test_astar(self):
        print "***Benchmarking A Star algorithm***"
        algorithm = AStarAlgorithm(self.no_discs, self.no_rods)
        self.print_result(algorithm)

    def test_backtracking(self):
        print "***Benchmarking Backtracking algorithm***"
        algorithm = BacktrackAlgorithm(self.no_discs, self.no_rods)
        self.print_result(algorithm)

    def test_backtracking_recursive(self):
        print "***Benchmarking Recursive Backtracking algorithm***"
        algorithm = RecursiveBacktrackAlgorithm(self.no_discs, self.no_rods)
        self.print_result(algorithm)

    def test_hillclimbing(self):
        print "***Benchmarking Hill Climbing algorithm***"
        algorithm = HillClimbingAlgorithm(self.no_discs, self.no_rods)
        self.print_iterated_result(algorithm)

    def test_random(self):
        print "***Benchmarking Random algorithm***"
        algorithm = RandomAlgorithm(self.no_discs, self.no_rods)
        self.print_iterated_result(algorithm)

    def test_random_optimized(self):
        print "***Benchmarking Random Optimized algorithm***"
        algorithm = RandomOptimizedAlgorithm(self.no_discs, self.no_rods)
        self.print_iterated_result(algorithm)

    def get_execution_time(self, algorithm):
        start_time = datetime.now()
        algorithm.solve()
        end_time = datetime.now()
        return end_time - start_time

    def get_solution_length(self, algorithm):
        return algorithm.steps(), len(algorithm.visited_states)

    def print_iterated_result(self, algorithm):
        total_time = timedelta()
        visited_states = 0
        result = 0
        for i in xrange(self.no_iter):
            total_time += self.get_execution_time(algorithm)
            solution_steps, solution_visited = self.get_solution_length(algorithm)
            result += solution_steps
            visited_states += solution_visited

        print "Duration: {}".format(total_time)
        print "Result: {}".format(result)
        print "Visited states: {}".format(visited_states)

    def print_result(self, algorithm):
        algorithm_time = self.get_execution_time(algorithm)
        solution_steps, solution_visited = self.get_solution_length(algorithm)

        print "Duration: {}".format(algorithm_time)
        print "Result: {}".format(solution_steps)
        print "Visited states: {}".format(solution_visited)
