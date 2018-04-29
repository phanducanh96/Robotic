
from individual import INDIVIDUAL
import pickle
import constants as c
from environments import ENVIRONMENTS
from individual3 import INDIVIDUAL3
envs = ENVIRONMENTS()

#f = open ( 'robot2.p' , 'r' )
#best = pickle.load(f)
#f.close()

#best.p[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)
#best.p2[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)

f = open ( 'wheggedGenome1.p', 'r')
gn1 = pickle.load(f)
f.close()

f2 = open ( 'wheggedGenome2.p', 'r')
gn2 = pickle.load(f2)
f2.close()

f3 = open( 'wheeledGenome.p', 'r')
gn3 = pickle.load(f3)
f3.close()

best = INDIVIDUAL3(0, gn1, gn2, gn3)
best.Start_Evaluation(envs.envs[0], True, False, c.evalTime)





