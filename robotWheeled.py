import constants as c
import random
class ROBOTWHEELED:
    def __init__(self,sim,wts, env):
        xc = 0
        yc = 0
        if(env.ID == 0):
            xc = c.L*2
            yc = 0
        self.send_objects(sim, xc, yc)
        self.send_joints(sim, xc, yc)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)

    def send_objects(self, sim, xc, yc):
#        self.whiteObject = sim.send_cylinder( x=0 ,y=0 , z=0.6 , length=1.0 , radius=0.1)
#        self.redObject = sim.send_cylinder( x=0 , y=0.5 , z=1.1, r=1, g=0, b=0, r1=0, r2=1, r3=0 )

        self.wheels = [0]*4
        self.wheels2 = [0]*4
        count = 0
        count2 = 0
        
        self.O0 = sim.send_box(x=0 + xc, y=0 + yc, z=c.L/2, length=1.75*c.L, width=c.L, height=2*c.R, r=0.5, g=0.5, b=0.5)
        
        for x_pos in [-c.L/2, c.L/2]:
            for y_pos in [-c.L/2, c.L/2]:
                self.wheels[count] = sim.send_cylinder(x=x_pos + xc, y=y_pos + yc, z=c.R, length = 0, radius=c.R, r=1, g=0, b=0)
                count += 1
    
        for x_pos in [-c.L/2, c.L/2]:
            for y_pos in [-c.L/2, c.L/2]:
                self.wheels2[count2] = sim.send_cylinder(x=x_pos + xc, y=y_pos + yc, z=c.R, length = 0, radius=c.R/2, r=1, g=0, b=0)
                count2 += 1
        
        
        
        self.O = {}
        self.O[0] = self.O0
        self.O[1] = self.wheels[0]
        self.O[2] = self.wheels[1]
        self.O[3] = self.wheels[2]
        self.O[4] = self.wheels[3]
        self.O[5] = self.wheels2[0]
        self.O[6] = self.wheels2[1]
        self.O[7] = self.wheels2[2]
        self.O[8] = self.wheels2[3]

    def send_joints(self, sim, xc, yc):
        self.axles = [0]*4
        self.axles2 = [0]*4
        count = 0
        count2 = 0

        for x_pos in [-c.L/2, c.L/2]:
            for y_pos in [-c.L/2, c.L/2]:
                # position_control = False -> continuous range of motion
                self.axles[count] = sim.send_hinge_joint(first_body_id= self.wheels[count], second_body_id=self.O[0], x=x_pos + xc,
                y=y_pos + yc, z=c.R,
                n1=1, n2=0, n3=0,
                position_control=False,
                speed=c.Speed)
                count += 1
    
        for x_pos in [-c.L/2, c.L/2]:
            for y_pos in [-c.L/2, c.L/2]:
                # position_control = False -> continuous range of motion
                self.axles2[count2] = sim.send_hinge_joint(first_body_id= self.wheels2[count2], second_body_id=self.wheels[count2], x=x_pos + xc,
                y=y_pos + yc, z=c.R,
                n1=0, n2=1, n3=0,
                position_control=False,
                speed=c.Speed)
                count2 += 1


        self.J = {}
        self.J[0] = self.axles[0]
        self.J[1] = self.axles[1]
        self.J[2] = self.axles[2]
        self.J[3] = self.axles[3]
        self.J[4] = self.axles2[0]
        self.J[5] = self.axles2[1]
        self.J[6] = self.axles2[2]
        self.J[7] = self.axles2[3]


    def send_sensors(self, sim):
#        self.T0 = sim.send_light_sensor( body_id = self.O[1] )
#        self.T1 = sim.send_light_sensor( body_id = self.O[2] )
#        self.T2 = sim.send_light_sensor( body_id = self.O[3] )
#        self.T3 = sim.send_light_sensor( body_id = self.O[4] )
        self.L4 = sim.send_light_sensor( body_id = self.O0 )

        self.S = {}
#        self.S[0] = self.T0
#        self.S[1] = self.T1
#        self.S[2] = self.T2
#        self.S[3] = self.T3
        self.S[0] = self.L4
#        self.P2 = sim.send_proprioceptive_sensor( joint_id = self.joint )
#        self.R3 = sim.send_ray_sensor( body_id = self.redObject , x = 0 , y = 1.1 , z = 1.1 , r1 = 0 , r2 = 1, r3 = 0)
        #R3 = sim.send_ray_sensor( body_id = redObject , x = 0 , y = 0.5 , z = 1.0 , r1 = 0, r2 = 0, r3 = -1)
    def send_neurons(self, sim):
        self.SN = {}
        self.MN = {}
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])

        for j in self.J:
            self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j])
        
#        self.SN0 = sim.send_sensor_neuron( sensor_id = self.T0 )
#        self.SN1 = sim.send_sensor_neuron( sensor_id = self.T1 )
#        self.SN2 = sim.send_sensor_neuron( sensor_id = self.P2 )
#        self.SN3 = sim.send_sensor_neuron( sensor_id = self.R3 )
#
#        self.sensorNeurons = {}
#        self.sensorNeurons[0] = self.SN0
#        self.sensorNeurons[1] = self.SN1
#        self.sensorNeurons[2] = self.SN2
#        self.sensorNeurons[3] = self.SN3
#
#        self.MN2 = sim.send_motor_neuron( joint_id = self.joint )
#        self.motorNeurons = {}
#        self.motorNeurons[0] = self.MN2
    def send_synapses(self, sim, wts):

#        for sn in self.SN:
#            firstMN = min(self.MN, key=self.MN.get)
#            sim.send_synapse(source_neuron_id = self.SN[sn] , target_neuron_id = self.MN[firstMN] , weight = random.random()*2 - 1 )
#        for s in self.sensorNeurons:
#            for m in self.motorNeurons:
#                sim.send_synapse( source_neuron_id = self.sensorNeurons[s] , target_neuron_id = self.motorNeurons[m] , weight = wts[s] )
        for j in self.SN:
            for i in self.MN:
#                if (i > 3):
#                    sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id = self.MN[i], weight = wts2[i])
#                else:
#                    sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id = self.MN[i], weight = wts)
                sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id = self.MN[i], weight = wts[j][i])

#sim.send_synapse( source_neuron_id = SN0 , target_neuron_id = MN2 , weight = -1.0 )



