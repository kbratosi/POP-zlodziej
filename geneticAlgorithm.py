import sys, csv, getopt, json, random
from random import randint
from Population import Population
from Individual import Individual


def main(argv):
    characteristic_file = ""
    parameters_file = ""

    try:
        opts, args = getopt.getopt(argv, "hc:p:", ["characteristic=", "parameters="])
    except getopt.GetoptError:
        print("geneticAlgorithm.py -c <characteristic.csv> -p <parameters.json>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("geneticAlgorithm.py -c <characteristic.csv> -p <parameters.json>")
            sys.exit()
        elif opt in ("-c", "--characteristic"):
            characteristic_file = arg
        elif opt in ("-p", "--parameters"):
            parameters_file = arg

    if not (characteristic_file and parameters_file):
        print("Both files are required")
        sys.exit()

    return characteristic_file, parameters_file


def tournament_selection(population, tournament_size=3):
    tournament = Population()

    for i in range(tournament_size):
        random_individual = randint(0, len(population.individuals)-1)
        tournament.individuals.append(population.get_at_idx(random_individual))

    return tournament.get_the_best()


def crossover(first_individual, second_individual, probability):
    new_individual = Individual()
    
    num_of_genes = randint(1, len(first_individual.genes)-2)

    if random.uniform(0.0, 1.0) > probability:
        for i in range(num_of_genes):
            new_individual.genes.append(first_individual.genes[i])
    else:
        for i in range(num_of_genes):
            new_individual.genes.append(second_individual.genes[i])

    if random.uniform(0.0, 1.0) > probability:
        for i in range(num_of_genes, len(first_individual.genes)):
            new_individual.genes.append(first_individual.genes[i])
    else:
        for i in range(num_of_genes, len(first_individual.genes)):
            new_individual.genes.append(second_individual.genes[i])

    return new_individual

def mutate(individual, probability):
    for i in range(len(individual.genes)):
        if random.uniform(0.0, 1.0) <= probability:
            individual.change_gene_at_idx(i)

def genetic_algorithm(A, V, W, json_data):
     # - Generowanie losowe populacji startowej
    population = Population(json_data["populations"], len(A))

    # - implementacja funkcji oceny przystosowania
    population.fitness_calculation(W, A, V)
    
    # Działanie w pętli
    num_of_generation = 0
    while num_of_generation < json_data["generations"]:
        
        # - Utworzenie nowej populacji 
        next_population = Population()
        
        for i in range(len(population.individuals)):

            # - Implementacja selekcji turniejowej
            first_winner = tournament_selection(population)
            second_winner = tournament_selection(population)

            # - Implementacja krzyżowania w zależności od parametru k i prawdopodobieństwa Pk
            new_individual = crossover(
                first_winner,
                second_winner,
                json_data["crossover_probability"],
            )
            
            next_population.individuals.append(new_individual)
            
        # - Implementacja mutacji z prawdopodobieństwem Pm
        for i in range(len(population.individuals)):
            mutate(next_population.individuals[i], json_data["mutation_probability"])
        
        next_population.fitness_calculation(W, A, V)

        population = next_population        
        num_of_generation += 1    
        
    the_best = population.get_the_best()
    answer = []
    for i in range(len(the_best.genes)):
        answer.append(the_best.genes[i])

    return answer, int(the_best.fitness)

if __name__ == "__main__":
    csv_file_name, json_file_name = main(sys.argv[1:])

    csv_file = open(csv_file_name)
    csvreader = csv.reader(csv_file)

    csv_rows = [row for row in csvreader]

    json_file = open(json_file_name)
    json_data = json.load(json_file)
    
    answer, fitness = genetic_algorithm(csv_rows[0], csv_rows[1], json_data)
    print("{}, fitness: {}".format(answer, fitness))
