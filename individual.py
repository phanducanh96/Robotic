import numpy
import math
import random
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../../..')
import pyrosim
from robotWhegged import ROBOTWHEGGED

class INDIVIDUAL:
    def __init__(self, i):
        self.genome = numpy.random.random_sample((5, 8)) * 2 - 1
        self.genomeTest = numpy.random.random_sample(8) * 2 - 1
        self.fitness = 0
        self.ID = i
    
    def Mutate(self):
        geneToMutate = random.randint(0,4)
        geneToMutate2 = random.randint(0,7)
        geneToMutate3 = random.randint(0,7)
        
        temp = random.gauss( self.genome[geneToMutate][geneToMutate2], math.fabs(self.genome[geneToMutate][geneToMutate2]))
        
        temp2 = random.gauss( self.genomeTest[geneToMutate3], math.fabs(self.genomeTest[geneToMutate3]))
        
        if temp > 1:
            temp = 1
        if temp < -1:
            temp = -1
        
        if temp2 > 1:
            temp2 = 1
        if temp2 < -1:
            temp2 = -1
        
        self.genome[geneToMutate][geneToMutate2] = temp

        self.genomeTest[geneToMutate3] = temp2

    def Print(self):
        print(self.ID),
        print(self.fitness),
        print('] '),
    
    def Start_Evaluation(self, env, pp, pb,evalTime):
        self.sim = pyrosim.Simulator( play_paused=pp , eval_time=evalTime, play_blind = pb)
        self.robotWhegged = ROBOTWHEGGED( self.sim , self.genome, self.genomeTest, env )
        env.Send_To( self.sim )
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        sensorData = self.sim.get_sensor_data( sensor_id = self.robotWhegged.L4)
        self.fitness = self.fitness + sensorData[-1]
        del self.sim



