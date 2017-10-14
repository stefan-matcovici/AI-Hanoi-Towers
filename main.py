from algorithms import *
from core import *

if __name__ == "__main__":
    algorithm = Algorithm(3, 5)

    for i in range(10):
        algorithm.move_to_next_random_state()

    print algorithm.steps()

    random = RandomAlgorithm(3, 5)

    print random.current_state
