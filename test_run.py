from backpack_algorithm import backpack_algorithm
from geneticAlgorithm import genetic_algorithm

import argparse, json, time
import random

parser = argparse.ArgumentParser(description="SK.POP.2 Złodziej test run")
parser.add_argument(
    "-p",
    "--parameters",
    help="Path to .json parameters file",
    type=str,
    required=True,
)
parser.add_argument(
    "-n",
    "--num_iterations",
    type=int,
    required=False,
    default=5
)
parser.add_argument(
    "-s",
    "--size",
    help="Problem size",
    type=int,
    required=True
)
parser.add_argument(
    "-o",
    "--output",
    help="Path to output log",
    type=str,
    required=False,
    default="./output.log"
)

if __name__ == "__main__":
    args = parser.parse_args()

    json_file = open(args.parameters)
    json_data = json.load(json_file)

    for _ in range(args.num_iterations):
        A = [random.randint(1, 40) for _ in range(args.size)]
        V = [random.randint(1, 120) for _ in range(args.size)]
        W = int(sum(A) * random.uniform(0.4, 0.6))

        print("A: {}\nV: {}\nW: {}".format(A, V, W))
        
        start_time_backpack = time.time()
        b_answer, b_score = backpack_algorithm(A, V, W)
        elapsed_time_backpack = time.time() - start_time_backpack

        print("Backpack:\nAnswer: {}\nScore: {}\nTime: {}".format(b_answer, b_score, elapsed_time_backpack))

        start_time_genetic = time.time()
        e_answer, e_score = genetic_algorithm(A, V, W, json_data)
        elapsed_time_genetic = time.time() - start_time_genetic

        print("Genetic algorithm:\nAnswer: {}\nScore: {}\nTime: {}".format(e_answer, e_score, elapsed_time_genetic))

        # b_answer == e_answer
        # b_score == e_score
        # save