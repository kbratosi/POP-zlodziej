from Individual import Individual
class Population():
    
    def __init__(self, population_size, genome_size):
        self.individuals = []
        
        for i in range (population_size):
            self.individuals.append(Individual(genome_size))
    
    def fitness_calculation(self, max_weight, weight_params, cost_params):        
        for obj in self.individuals:
            fitness_value = 0
            weight_of_obj = 0
            for i in range(len(weight_params)):
                fitness_value += obj.genes[i] * float(cost_params[i])
                weight_of_obj += obj.genes[i] * float(weight_params[i])
            
            if weight_of_obj > max_weight:
                obj.fitness = 0
            else:
                obj.fitness = fitness_value
            
    def get_the_best(self):
        elite = self.individuals[0]
        for obj in self.individuals:
            if obj.fitness >= elite.fitness:
                elite = obj
        return elite
        