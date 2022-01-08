from random import randint
class Individual():
    
    def __init__(self, genome_size):
        self.genes = [None] * genome_size
        self.fitness = 0
        
        for i in range(genome_size):
            self.genes[i] = randint(0,1)
            
    def get_gene_at_idx(self, index):
        return self.genes[index]
    
    def set_gene_at_idx(self, index, value):
        self.genes[index] = value
        
    def change_gene_at_idx(self, index):
        if self.genes[index]:
            self.genes[index] = 0
        else:
            self.genes[index] = 1