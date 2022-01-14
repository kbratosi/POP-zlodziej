from Individual import Individual
class Population():
    
    def __init__(self, population_size = 0, genome_size = 0):
        self.individuals = []
        
        for i in range (population_size):
            self.individuals.append(Individual(genome_size))
    
    def fitness_calculation(self, max_weight, weight_params, cost_params):        
        for obj in self.individuals:
            weight_of_obj = 0
            for i in range(len(weight_params)):
                weight_of_obj += obj.genes[i] * float(weight_params[i])
            
            if weight_of_obj > max_weight:
                obj.fitness = 0
            else:
                fitness_value = 0
                for i in range(len(weight_params)):
                    fitness_value += obj.genes[i] * float(cost_params[i])
                obj.fitness = fitness_value
            # print("Print V: " + str(obj.fitness) + " AND W: " + str(weight_of_obj))
            
    def get_the_best(self):
        elite = self.individuals[0]
        for obj in self.individuals:
            if obj.fitness >= elite.fitness:
                elite = obj
        return elite
    
    def get_at_idx(self, index):
        return self.individuals[index]
    
        