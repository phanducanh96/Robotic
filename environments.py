from environment import ENVIRONMENT
from robot import ROBOT
import copy
import random
import constants as c

class ENVIRONMENTS:
    def __init__(self):
        self.envs = {}
        for i in range(0, c.numEnvs):
            self.envs[i] = ENVIRONMENT(i)

