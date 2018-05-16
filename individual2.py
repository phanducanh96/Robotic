import numpy
import math
import random
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../../..')
import pyrosim
from robotWheeled import ROBOTWHEELED

class INDIVIDUAL2:
    def __init__(self, i):
        self.genome2Test = numpy.random.random_sample(2) * 2 - 1
        self.fitness = 0
        self.ID = i
    
    def Mutate(self):
        geneToMutate5 = random.randint(0, 1)
#        geneToMutate4 = random.randint(0,7)
        temp3 = random.gauss( self.genome2Test[geneToMutate5], math.fabs(self.genome2Test[geneToMutate5]))
    
        if temp3 > 1:
            temp3 = 1
        if temp3 < -1:
            temp3 = -1
        self.genome2Test[geneToMutate5] = temp3
    
    def Print(self):
        print(self.ID),
        print(self.fitness),
        print('] '),
    
    def Start_Evaluation(self, env, pp, pb,evalTime):
        self.sim = pyrosim.Simulator( play_paused=pp , eval_time=evalTime, play_blind = pb)
        self.robotWheeled = ROBOTWHEELED( self.sim , self.genome2Test, env)
        env.Send_To( self.sim )
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        sensorData = self.sim.get_sensor_data( sensor_id = self.robotWheeled.L0 )
        self.fitness = self.fitness + sensorData[-1]
        del self.sim



