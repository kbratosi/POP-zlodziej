from backpack_algorithm_mod import backpack_algorithm
from geneticAlgorithm import genetic_algorithm

import argparse, json, time, csv
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
parser.add_argument(
    "-pop",
    "--populations",
    help="Number of populations",
    type=int,
    required=False,
    default=0
)
parser.add_argument(
    "-g",
    "--generations",
    help="Number of generations",
    type=int,
    required=False,
    default=0
)
parser.add_argument(
    "-w",
    "--weight",
    help="Maximum weight",
    type=int,
    required=False,
    default=0
)


if __name__ == "__main__":
    args = parser.parse_args()

    json_file = open(args.parameters)
    json_data = json.load(json_file)
    
    results_file = open("pop_test_rep_one.csv", "a")
    write_to_file = csv.writer(results_file)
    
    # W = 1006

    for _ in range(args.num_iterations):
        A = [random.randint(1, 40) for _ in range(args.size)]
        V = [random.randint(1, 120) for _ in range(args.size)]
        if (args.weight > 0):
            W = args.weight
        else:
            W = int(sum(A) * random.uniform(0.4, 0.6))
        
        if(args.populations == 0):
            populations_to_save = json_data["populations"]
        else:
            populations_to_save = args.populations
            
        if(args.generations == 0):
            generations_to_save = json_data["generations"]
        else:
            generations_to_save = args.generations
        
        print("A: {}\nV: {}\nW: {}".format(A, V, W))
        # print(W)
        
        start_time_backpack = time.time()
        b_answer, b_score, b_final_weight = backpack_algorithm(A, V, W)
        elapsed_time_backpack = time.time() - start_time_backpack

        print("Backpack:\nAnswer: {}\nFinal weight: {}\nScore: {}\nTime: {}".format(b_answer, b_final_weight, b_score, elapsed_time_backpack))

        start_time_genetic = time.time()
        e_answer, e_score, e_final_weight = genetic_algorithm(A, V, W, json_data, populations_to_save, generations_to_save)
        elapsed_time_genetic = time.time() - start_time_genetic

        print("Genetic algorithm:\nAnswer: {}\nFinal weight: {}\nScore: {}\nTime: {}".format(e_answer, e_final_weight, e_score, elapsed_time_genetic))
        print()
        
        row_to_save = [W, len(A), populations_to_save, generations_to_save,
                       json_data["crossover_probability"], json_data["mutation_probability"], 
                       b_score, e_score, b_score == e_score, 
                       elapsed_time_backpack, elapsed_time_genetic]
        
        
        write_to_file.writerow(row_to_save)
        
    results_file.close()
