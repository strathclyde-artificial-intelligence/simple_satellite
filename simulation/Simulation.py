import math
import numpy as np
import random
from simulation.GoalReferee import GoalReferee
import IPython 

class SatelliteSim:

    MAX_ORBITS = 30

    CIRCUNFERENCE = 360
    ACTION_THRESHOLD = 6

    MAX_TARGETS = 10
    MAX_STATION = 4
    MIN_TARGETS = 2
    MIN_STATION = 1

    MEMORY_SIZE = 10

    ACTION_TAKE_IMAGE = 0
    ACTION_DUMP = 1
    ACTION_ANALYSE = 2
    ACTION_DO_NOTHING = 3

    DURATION_TAKE_IMAGE = 2
    DURATION_DUMP = 19
    DURATION_ANALYSE = 49

    def __init__(self, period, Version):
        self.version = Version
        self.sim_time = 0
        self.PERIOD = period
        self.velocity = SatelliteSim.CIRCUNFERENCE/self.PERIOD

        # satellite state
        self.pos = 0.
        self.orbit = 0
        self.last_action = None

        # planet position
        self.groundStations = []
        self.targets = []
        self.over_targets = [0] * self.MAX_TARGETS
        self.over_Station = [0] * self.MAX_STATION 

        # memory state
        self.memory_level = 0
        self.images = [-1] * self.MEMORY_SIZE
        self.analysis = [False] * self.MEMORY_SIZE
        self.satellite_busy_time = 0
        self.busy=0

        # goals
        self.goalRef = GoalReferee()

    def update(self, action, dt: float):
        done = False
        act=[action]
        if len(act)==1:
            self.apply_action(action)
        elif len(act[0])==3:
            self.apply_action(action[0], image_target=action[1], memory_slot=action[2])

        # update time variables
        self.sim_time += dt
        self.pos += self.velocity*dt

        # update orbit position
        if self.pos > SatelliteSim.CIRCUNFERENCE:
            self.pos -=  SatelliteSim.CIRCUNFERENCE
            self.orbit += 1
            if self.orbit%100 == 0:
                self.initRandomTargets(int(round(random.normalvariate(8,4))))

        self.over_targets = [int(self.targets[i][0] < self.pos < self.targets[i][1]) for i in range(SatelliteSim.MAX_TARGETS)]
        self.over_Station = [int(self.groundStations[i][0] < self.pos < self.groundStations[i][1]) for i in range(SatelliteSim.MAX_STATION)]

        if self.satellite_busy_time > 0:
            self.satellite_busy_time = self.satellite_busy_time - dt
            self.busy=1
        else: 
            self.busy = 0

        # Check if simulation ends
        if self.orbit>=SatelliteSim.MAX_ORBITS:
            print('Episode Ended number of orbits : {}'.format(self.orbit))
            done = True
        
        # update state
        if len(act)==1:
            state = self.get_state()
            return state, done
        elif len(act[0])==3:
            self.apply_action(action[0], image_target=action[1], memory_slot=action[2])
            return done
        else:
            raise SyntaxError("Action length not Valid")

    def apply_action(self, action, image_target=None, memory_slot=None):   

        # check if busy or the satellite does nothing 
        if self.busy==1 or action==3 or action==None:
            return 

        # Take picture action
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            for index in range(len(self.targets)):
                if image_target:
                    ind_mem = memory_slot
                    index = image_target
                else:
                    if self.version == 1: 
                        ind_mem = self.memory_level
                    elif self.version == 2:
                        for ind_mem in range(SatelliteSim.MEMORY_SIZE):
                            if self.images[ind_mem] == -1:
                                break
                    else:
                        raise('Not valid value of version of simulation')
                if self.targets[index][0] < self.pos < self.targets[index][1] and self.memory_level<SatelliteSim.MEMORY_SIZE-1:
                    self.satellite_busy_time = SatelliteSim.DURATION_TAKE_IMAGE
                    self.images[ind_mem] = index
                    self.memory_level += 1
                    self.last_action = [action, index, ind_mem]
                    #print('Image succesful')
                    break
                index += 1 
            return
        
        # Analyse picture
        if action == SatelliteSim.ACTION_ANALYSE:
            for index in range(len(self.analysis)):
                if memory_slot:
                    index = memory_slot 
                if not self.analysis[index] and self.images[index]>-.5:
                    self.satellite_busy_time = SatelliteSim.DURATION_ANALYSE
                    #print('Analyzed')
                    self.last_action = [action, self.images[index], index]
                    if random.random() > 0.0:
                        self.analysis[index] = True
                    else:
                        self.analysis[index] = False
                        self.images[index] = -1
                        self.memory_level -= 1
                    break
            return
        
        # Dump picture
        if action == SatelliteSim.ACTION_DUMP:
            # check if it is above the ground station and if their is any analysed image
            Dumping=False
            if any([gs[0]< self.pos < gs[1] for gs in self.groundStations]) and self.memory_level>0 :
                # Check all the images except the last one
                if self.analysis[-1]:
                    picture_to_dump = SatelliteSim.MEMORY_SIZE-1
                else:
                    for index in range(len(self.analysis)-1):
                        if not self.analysis[index+1] and self.analysis[index]:
                            picture_to_dump=index
                            Dumping=True
                            break
                # Look at the first and last picture false
                if Dumping:
                    #print('Dumped')
                    self.last_action = [action, self.images[picture_to_dump], picture_to_dump]
                    self.satellite_busy_time = SatelliteSim.DURATION_DUMP
                    self.analysis[picture_to_dump] = False
                    self.images[picture_to_dump] = -1
                    self.memory_level -= 1
                    # score the goal value
                    self.goalRef.evaluateDump(self.orbit, self.images[index])
                    return
    
    def reset(self):
        self.sim_time = 0

        # satellite state
        self.pos = 0
        self.orbit = 0
        self.last_action = None

        self.over_targets = [0] * self.MAX_TARGETS
        self.over_Station = [0] * self.MAX_STATION 

        # memory state
        self.memory_level = 0
        self.images = [-1] * self.MEMORY_SIZE
        self.analysis = [False] * self.MEMORY_SIZE
        self.satellite_busy_time = 0

        # Generate Targets
        self.initRandomTargets(int(round(random.normalvariate(8,4))))

        # Generate Ground Stations
        self.initRandomStations(int(round(random.normalvariate(2,1))))

    def initRandomStations(self, amount):
        self.groundStations = []

        if amount>self.MAX_STATION:
            amount = self.MAX_STATION
        if amount<SatelliteSim.MIN_STATION:
            amount = SatelliteSim.MIN_STATION 

        for i in range(SatelliteSim.MAX_STATION):
            if i < amount:
                s = random.random()*(SatelliteSim.CIRCUNFERENCE-15)
                self.groundStations.append((s, s+15))
            else:
                self.groundStations.append((-1, -1))

    def initRandomTargets(self, amount):
        self.targets = []

        if amount>SatelliteSim.MAX_TARGETS:
            amount = SatelliteSim.MAX_TARGETS
        if amount<SatelliteSim.MIN_TARGETS:
            amount = SatelliteSim.MIN_TARGETS 

        for i in range(SatelliteSim.MAX_TARGETS):
            if i < amount:
                s = random.random()*(SatelliteSim.CIRCUNFERENCE-5)
                self.targets.append((s, s+5))
            else:
                self.targets.append((-1, -1))

    def get_state(self):
        state = {'Analysis':np.array([int(i) for i in self.analysis]),
                'Busy': self.busy,
                'Images':np.array(self.images, dtype=np.int8),
                'Memory': self.memory_level,
                'Over Target': np.array(self.over_targets),
                'Over station': np.array(self.over_Station),
                'Position': np.array([self.pos]),
                'Station Location': np.array(self.groundStations),
                'Target Location': np.array(self.targets),
                'Time': np.array([self.sim_time])}
        return state
        
    def time2angle(self, time):
        delta_t = time - math.floor(time/self.PERIOD) * self.PERIOD
        return self.velocity*delta_t
    
    def angle2time(self, angle):
        T = self.orbit*self.PERIOD
        t = T + angle / self.velocity

