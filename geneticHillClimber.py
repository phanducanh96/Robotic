from population import POPULATION
import copy
import constants as c
from environments import ENVIRONMENTS
import pickle

envs = ENVIRONMENTS()

parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, True, True, c.evalTime)
parents.Print()

parents2 = POPULATION(c.popSize)
parents2.Initialize2()
parents2.Evaluate(envs, True, True, c.evalTime)
parents2.Print()

for g in range(1, c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
#    children.Fill_From2(parents)
    children.Evaluate(envs, False, True, c.evalTime)
    parents.ReplaceWith(children)
#    parents.ReplaceWith2(children)
    print('Whegged: '),
    print(g),
    children.Print()
    
    children2 = POPULATION(c.popSize)
    children2.Fill_From(parents2)
    children2.Evaluate(envs, False, True, c.evalTime)
    parents2.ReplaceWith(children2)

    print('Wheeled: '),
    print(g),
    children2.Print()

    if g == (c.numGens - 1):
        f = open('wheggedGenome1.p', 'wb')
        pickle.dump(parents.p[0].genome, f)
        f.close()
        f2 = open('wheggedGenome2.p', 'wb')
        pickle.dump(parents.p[0].genomeTest, f2)
        f2.close()
        f3 = open('wheeledGenome.p', 'wb')
        pickle.dump(parents2.p[0].genome2Test, f3)
        f3.close()

#for e in range(0, c.numEnvs):

#parents.p[0].Start_Evaluation(envs.envs[3], True, False, c.evalTime)
#parents.p[0].Start_Evaluation(envs.envs[2], True, False, c.evalTime)
#parents.p[0].Start_Evaluation(envs.envs[1], True, False, c.evalTime)
parents.p[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)
parents2.p[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)





#parent = INDIVIDUAL()
#parent.Evaluate(True)
#print(parent.fitness)
#
#for i in range(0,100):
#    child = copy.deepcopy( parent )
#    child.Mutate()
#    child.Evaluate(True)
#    print"[g:",  i, "]", "[pw:", parent.genome, "]", "[p:", parent.fitness , "]", "[c:", child.fitness , "]"
#    if ( child.fitness > parent.fitness ):
#        child.Evaluate(True)
#        parent = child


#        f = open('robot.p','w')
#        pickle.dump(parent , f )
#        f.close()


#sensorData = sim.get_sensor_data( sensor_id = MN2 )
#print(sensorData)
#f = plt.figure()
#panel = f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(-2, +2)
#plt.show()


