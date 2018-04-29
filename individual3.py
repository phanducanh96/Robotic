import numpy
import math
import random
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../../..')
import pyrosim
from robotWhegged import ROBOTWHEGGED
from robotWheeled import ROBOTWHEELED

class INDIVIDUAL3:
    def __init__(self, i, gn1, gn2, gn3):
        self.genome = gn1
        self.genomeTest = gn2
        
        self.genome2Test = gn3
#        self.genome3 = numpy.random.random_sample((5, 8)) * 2 - 1
#        self.genome4 = numpy.random.random_sample((5, 8)) * 2 - 1
        self.fitness = 0
        self.fitness2 = 0
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


        geneToMutate5 = random.randint(0, 0)
        geneToMutate4 = random.randint(0,7)
        temp3 = random.gauss( self.genome2Test[geneToMutate5][geneToMutate4], math.fabs(self.genome2Test[geneToMutate5][geneToMutate4]))
    
        if temp3 > 1:
            temp3 = 1
        if temp3 < -1:
            temp3 = -1
        self.genome2Test[geneToMutate5][geneToMutate4] = temp3

    def Print(self):
        print(self.ID),
        print(self.fitness),
        print('] '),
    
    def Print2(self):
        print(self.ID),
        print(self.fitness2),
        print('] '),
    
    def Start_Evaluation(self, env, pp, pb,evalTime):
        self.sim = pyrosim.Simulator( play_paused=pp , eval_time=evalTime, play_blind = pb)
        self.robotWhegged = ROBOTWHEGGED( self.sim , self.genome, self.genomeTest, env )
        self.robotWheeled = ROBOTWHEELED( self.sim , self.genome2Test, env)
        env.Send_To( self.sim )
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        sensorData = self.sim.get_sensor_data( sensor_id = self.robotWhegged.L4)
        sensorData2 = self.sim.get_sensor_data( sensor_id = self.robotWheeled.L4)
        self.fitness = self.fitness + sensorData[-1]
        self.fitness2 = self.fitness2 + sensorData2[-1]
        del self.sim



