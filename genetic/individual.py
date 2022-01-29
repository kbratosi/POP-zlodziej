from random import randint


class Individual():    
    def __init__(self, genome_size = 0):
        self.genes = [randint(0,1) for _ in range(genome_size)]
        self.fitness = 0
            
    def get_gene_at_idx(self, index):
        return self.genes[index]
    
    def set_gene_at_idx(self, index, value):
        self.genes[index] = value
        
    def change_gene_at_idx(self, index):
        if self.genes[index]:
            self.genes[index] = 0
        else:
            self.genes[index] = 1