from Benchmark import Benchmark


class HanoiApp:
    def __init__(self):
        self.no_discs = 0
        self.no_rods = 0
        self.initial = []

    def read(self):
        self.no_discs = int(raw_input("Number of discs: "))
        self.no_rods = int(raw_input("Number of rods: "))

        s = raw_input("Initial state: ")
        self.initial = list(map(int, s.split()))

    def run(self):
        self.read()

        benchmark = Benchmark(self.no_discs, self.no_rods, self.initial)
        benchmark.start()
