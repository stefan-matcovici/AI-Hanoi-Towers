from core.Benchmark import Benchmark

if __name__ == "__main__":
    no_discs = raw_input("Number of discs: ")
    no_rods = raw_input("Number of rods: ")

    benchmark = Benchmark(int(no_discs), int(no_rods))
    benchmark.test()
