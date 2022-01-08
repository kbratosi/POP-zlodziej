# - Generowanie losowe populacji startowej
# - implementacja funkcji oceny przystosowania
# - Implementacja selekcji turniejowej
# - Implementacja krzyżowania w zależności od parametru k i prawdopodobieństwa Pk
# - Implementacja mutacji z prawdopodobieństwem Pm
import sys, csv, getopt, json

def main(argv):
    generation_file = ''
    parameters_file = ''
    
    try:
      opts, args = getopt.getopt(argv,"hg:p:",["generation=","parameters="])
    except getopt.GetoptError:
      print("geneticAlgorithm.py -g <generation.csv> -p <parameters.json>")
      sys.exit(2)
      
    for opt, arg in opts:
      if opt == '-h':
         print("geneticAlgorithm.py -g <generation.csv> -p <parameters.json>")
         sys.exit()
      elif opt in ("-g", "--generation"):
         generation_file = arg
      elif opt in ("-p", "--parameters"):
         parameters_file = arg
    
    if not (generation_file and parameters_file):
        print("Both files are required")
        sys.exit()
        
    return generation_file, parameters_file

if __name__ == "__main__":
    csv_file_name, json_file_name = main(sys.argv[1:])
        
    csv_file = open(csv_file_name)
    csvreader = csv.reader(csv_file)
    
    csv_rows = [row for row in csvreader]
    # for row in csvreader: csv_rows.append(row)
    
    print(csv_rows)
    
    json_file = open(json_file_name)
    json_data = json.load(json_file)
    
    print(json_data['populations'])
    print(json_data['mutation_probability'])