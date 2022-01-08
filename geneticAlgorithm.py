# - Generowanie losowe populacji startowej
# - implementacja funkcji oceny przystosowania
# - Implementacja selekcji turniejowej
# - Implementacja krzyżowania w zależności od parametru k i prawdopodobieństwa Pk
# - Implementacja mutacji z prawdopodobieństwem Pm
import sys, csv, getopt

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

if __name__ == "__main__":
    main(sys.argv[1:])
        
    csv_file = open('pokolenie.csv')
    csvreader = csv.reader(csv_file)
    
    csv_rows = []
    for row in csvreader:
        csv_rows.append(row)
    
    print(csv_rows[0][0])