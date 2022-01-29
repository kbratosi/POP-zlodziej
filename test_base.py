from backpack.backpack_algorithm import backpack_algorithm
from genetic.genetic_algorithm import genetic_algorithm

import argparse, json, time, csv
import random

parser = argparse.ArgumentParser(description="SK.POP.2 Złodziej test suite")
parser.add_argument(
    "-i",
    "--input",
    help="Path to input .csv",
    type=str,
    required=False,
    default=None
)
parser.add_argument(
    "-o",
    "--output",
    help="Path to output .csv",
    type=str,
    required=False,
    default="./output.csv"
)
parser.add_argument(
    "-p",
    "--parameters",
    help="Path to .json parameters file",
    type=str,
    required=True,
)
parser.add_argument(
    "-n",
    "--num_tests",
    help="Number of test iterations",
    type=int,
    required=False,
    default=1
)
parser.add_argument(
    "-r",
    "--randomize",
    help="Generate random A, V arrays of specified length and random X value",
    metavar="SIZE",
    type=int,
    required=False,
    default=0
)

if __name__ == "__main__":
    args = parser.parse_args()

    json_file = open(args.parameters)
    json_data = json.load(json_file)
    
    results_file = open("default_name.csv", "a")
    write_to_file = csv.writer(results_file)

    for _ in range(args.num_tests):
        if (args.randomize > 0):
            A = [random.randint(1, 40) for _ in range(args.randomize)]
            V = [random.randint(1, 120) for _ in range(args.randomize)]
            X = int(sum(A) * random.uniform(0.4, 0.6))
        else:
            csv_file = open(args.output)
            csvreader = csv.reader(csv_file)

            csv_rows = [row for row in csvreader]
            A = csv_rows[0]
            V = csv_rows[1]
            X = csv_rows[2]
            
            csv_file.close()
        
        print("A: {}\nV: {}\nW: {}".format(A, V, X))
        
        start_time_backpack = time.time()
        b_answer, b_score, b_final_weight = backpack_algorithm(A, V, X)
        elapsed_time_backpack = time.time() - start_time_backpack

        print("Backpack:\nAnswer: {}\nFinal weight: {}\nScore: {}\nTime: {}".format(b_answer, b_final_weight, b_score, elapsed_time_backpack))

        start_time_genetic = time.time()
        e_answer, e_score, e_final_weight = genetic_algorithm(A, V, X, json_data)
        elapsed_time_genetic = time.time() - start_time_genetic

        print("Genetic algorithm:\nAnswer: {}\nFinal weight: {}\nScore: {}\nTime: {}".format(e_answer, e_final_weight, e_score, elapsed_time_genetic))
        print()
        
        row_to_save = [X, len(A), json_data["populations"], json_data["generations"],
                       json_data["crossover_probability"], json_data["mutation_probability"], 
                       b_score, e_score, b_score == e_score, 
                       elapsed_time_backpack, elapsed_time_genetic]        
        
        write_to_file.writerow(row_to_save)
        
    results_file.close()
