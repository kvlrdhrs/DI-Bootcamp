import random

class Gene:
    def __init__(self, value=None):
        self.value = value if value is not None else random.choice([0, 1])
        
    def mutate(self):
        self.value = 1 if self.value == 0 else 0
        
    def __str__(self):
        return str(self.value)

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]
        
    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  # 1/2 chance to flip
                gene.mutate()
                
    def __str__(self):
        return ''.join(str(gene) for gene in self.genes)

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
        
    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()
            
    def is_all_ones(self):
        return all(gene.value == 1 for chromosome in self.chromosomes for gene in chromosome.genes)
    
    def __str__(self):
        return '\n'.join(str(chromosome) for chromosome in self.chromosomes)

class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment
        
    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

# Instantiate organisms and let them mutate until one has DNA made of only 1s
generations = 0
environment_probability = 0.1  # Set an example mutation probability
organisms = [Organism(DNA(), environment_probability) for _ in range(100)]

while True:
    generations += 1
    for organism in organisms:
        organism.mutate()
        if organism.dna.is_all_ones():
            print(f"All ones DNA achieved in {generations} generations.")
            print(organism.dna)
            break
    else:
        continue
    break
