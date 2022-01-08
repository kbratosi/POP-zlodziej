import sys, csv, getopt, json

from Population import Population

def main(argv):
    characteristic_file = ''
    parameters_file = ''
    
    try:
      opts, args = getopt.getopt(argv,"hc:p:",["characteristic=","parameters="])
    except getopt.GetoptError:
      print("geneticAlgorithm.py -g <characteristic.csv> -p <parameters.json>")
      sys.exit(2)
      
    for opt, arg in opts:
      if opt == '-h':
         print("geneticAlgorithm.py -g <characteristic.csv> -p <parameters.json>")
         sys.exit()
      elif opt in ("-c", "--characteristic"):
         characteristic_file = arg
      elif opt in ("-p", "--parameters"):
         parameters_file = arg
    
    if not (characteristic_file and parameters_file):
        print("Both files are required")
        sys.exit()
        
    return characteristic_file, parameters_file

def tournament_selection(population):
    _

if __name__ == "__main__":
    csv_file_name, json_file_name = main(sys.argv[1:])
        
    csv_file = open(csv_file_name)
    csvreader = csv.reader(csv_file)
    
    csv_rows = [row for row in csvreader]    
    
    json_file = open(json_file_name)
    json_data = json.load(json_file)
    
    # - Generowanie losowe populacji startowej
    population = Population(json_data['populations'], len(csv_rows[0]))
    
# Działanie w pętli
# - implementacja funkcji oceny przystosowania
    population.fitness_calculation(json_data['max_weight'], 
                                   csv_rows[0], csv_rows[1])
    # the_best = population.get_the_best()
    
    # for i in range(len(the_best.genes)):
    #     print(the_best.get_gene_at_idx(i))
    
# - Implementacja selekcji turniejowej

# - Implementacja krzyżowania w zależności od parametru k i prawdopodobieństwa Pk

# - Implementacja mutacji z prawdopodobieństwem Pm

# - Implementacja odrzucenia najgorszych osobników zastępując je potomstwem