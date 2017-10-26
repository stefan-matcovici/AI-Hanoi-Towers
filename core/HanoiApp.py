from Benchmark import Benchmark


class HanoiApp:
    def __init__(self):
        self.no_discs = 0
        self.no_rods = 0
        self.initial = []
        self.final = []

    def read(self):
        self.no_discs = int(raw_input("Number of discs: "))
        self.no_rods = int(raw_input("Number of rods: "))

        s = raw_input("Initial state: ")
        self.initial = list(map(int, s.split()))

        s = raw_input("Final state: ")
        self.final = list(map(int, s.split()))

    def check_inputs(self):
        if self.no_rods < 3:
            print "Number of rods can't be lower than 3"
            exit()

        if self.no_discs <= 0:
            print "Number of rods can't be non-positive"
            exit()

        if len(self.initial) > self.no_discs:
            print "Number of discs in initial state exceeds maximum number of discs"
            exit()

        if len(self.final) > self.no_discs:
            print "Number of discs in final state exceeds maximum number of discs"
            exit()

        for x in self.initial:
            if x > self.no_rods or x < 0:
                print "One disc in your initial state is on an invalid rod (negative or exceeds no of rods)"
                exit()

        for x in self.final:
            if x > self.no_rods or x < 0:
                print "One disc in your final state is on an invalid rod (negative or exceeds no of rods)"
                exit()

    def run(self):
        self.read()
        self.check_inputs()

        benchmark = Benchmark(self.no_discs, self.no_rods, self.initial, self.final)
        benchmark.start()