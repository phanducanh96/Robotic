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
parents.Print2()

for g in range(1, c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Fill_From2(parents)
    children.Evaluate(envs, False, True, c.evalTime)
    parents.ReplaceWith(children)
    parents.ReplaceWith2(children)
    print('Whegged: '),
    print(g),
    children.Print()
    print('Wheeled: '),
    print(g),
    children.Print2()
    if g == (c.numGens - 1):
        f = open('robot2.p', 'wb')
        pickle.dump(parents, f)
        f.close()

#for e in range(0, c.numEnvs):

#parents.p[0].Start_Evaluation(envs.envs[3], True, False, c.evalTime)
#parents.p[0].Start_Evaluation(envs.envs[2], True, False, c.evalTime)
#parents.p[0].Start_Evaluation(envs.envs[1], True, False, c.evalTime)
parents.p[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)
parents.p2[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)





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


