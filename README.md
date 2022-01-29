Projekt POP
Realizacja w zespole: Bratosiewicz Konrad, Marczuk Jakub
Temat projektu: SK.POP.2 - Złodziej

Uruchomienie scenariusza testowego:
1. Dane wejściowe z pliku .csv:
```
python3 test_base.py -i <ścieżka do pliku wejściowego> 
                     -p <ścieżka do pliku z parametrami alg. ewolucyjnego> 
                    [-o <ścieżka do pliku wynikowego>]
```

2. Dane wejściowe generowane losowo:
```
python3 test_base.py -p <ścieżka do pliku z parametrami alg. ewolucyjnego> 
                     -r <rozmiar generowanego problemu> 
                    [-n <liczba testów>]
                    [-o <ścieżka do pliku wynikowego>] 
```

Format pliku wejściowego (.csv):
>1. wiersz: tablica A
>2. wiersz: tablica V
>3. wiersz: X

Przykładowy plik wejściowy: input.csv

Przykładowy zestaw parametrów: parameters.json