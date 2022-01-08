# - Generowanie losowe populacji startowej
# - implementacja funkcji oceny przystosowania
# - Implementacja selekcji turniejowej
# - Implementacja krzyżowania w zależności od parametru k i prawdopodobieństwa Pk
# - Implementacja mutacji z prawdopodobieństwem Pm
import sys, csv, getopt, json

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

if __name__ == "__main__":
    csv_file_name, json_file_name = main(sys.argv[1:])
        
    csv_file = open(csv_file_name)
    csvreader = csv.reader(csv_file)
    
    csv_rows = [row for row in csvreader]    
    
    json_file = open(json_file_name)
    json_data = json.load(json_file)

    print(csv_rows)