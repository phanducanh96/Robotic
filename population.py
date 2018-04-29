from individual import INDIVIDUAL
from individual2 import INDIVIDUAL2
from robot import ROBOT
import copy
import random
import constants as c
import sys
sys.path.insert(0, '../../..')
import pyrosim

class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize

    def Initialize(self):
        for i in range(0,self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Initialize2(self):
        for i in range(0,self.popSize):
            self.p[i] = INDIVIDUAL2(i)

    def Print(self):
        for i in self.p:
            if ( i in self.p ):
                self.p[i].Print()
        print

    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

    def Copy_Best_From(self, other):
        for i in other.p:
                count = 0;
                for j in other.p:
                        temp = other.p[i].fitness
                        if(temp > other.p[j].fitness or temp == other.p[j].fitness):
                            count = count + 1
                if (count == self.popSize):
                    self.p[0] = copy.deepcopy(other.p[i])
                    break

    def Collect_Children_From(self, other):
        for i in other.p:
            if(i > 0):
                winner = self.Winner_Of_Tournament_Selection(other)
                self.p[i] = copy.deepcopy(winner)
                self.p[i].Mutate()

    def Winner_Of_Tournament_Selection(self, other):
        p1 = random.randint(0, self.popSize - 1)
        p2 = random.randint(0, self.popSize - 1)
        while p1 == p2:
            p2 = random.randint(0, self.popSize - 1)
        if(other.p[p1] > other.p[p2]):
            return other.p[p1]
        else:
            return other.p[p2]
    def Evaluate(self, envs, pp, pb, evalTime):
        for i in self.p:
            self.p[i].fitness = 0
        for e in envs.envs:
            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e], pp, pb, evalTime)
            for i in self.p:
                self.p[i].Compute_Fitness()
#                self.p[i].Print()
#                print
        for i in self.p:
                self.p[i].fitness = self.p[i].fitness / c.numEnvs

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self,other):
        for i in self.p:
#            if( self.p[i].fitness != 0 and other.p[i].fitness != 0):
                if (self.p[i].fitness < other.p[i].fitness):
                    self.p[i] = other.p[i]

    def Fill_From2(self, other):
        self.Copy_Best_From2(other)
        self.Collect_Children_From2(other)



