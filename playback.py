
from individual import INDIVIDUAL
import pickle
import constants as c
from environments import ENVIRONMENTS
envs = ENVIRONMENTS()

f = open ( 'robot2.p' , 'r' )
best = pickle.load(f)
f.close()

best.p[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)
best.p2[0].Start_Evaluation(envs.envs[0], True, False, c.evalTime)



