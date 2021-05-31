import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from simulation.Simulation import SatelliteSim
from simulation.Reward_functions import Reward_v1 as Reward
from simulation.DrawSim import SatelliteView 
import pygame

# import the gym class and spaces
import gym
from gym import spaces

import numpy as np
class SimpleSat(gym.Env):

    def __init__(self, sim: SatelliteSim, time_step: float, degug=False, debug=False):
        super(SimpleSat, self).__init__()
        """Custom Environment that follows gym interface"""
        metadata = {'render.modes': ['human']}
        # 
        self.debug = debug
        # start render enviroment
        self.view = SatelliteView()

        # save the satelite enviroment
        self.SatSim = sim 
        self.t = 0
        self.dt= time_step

        # The actions available are:
        #  - 0: take picture
        #  - 1: analyze picture 
        #  - 2: Dump picture
        #  - 3: Do Nothing
        self.action_space = spaces.Discrete(4)

        # Observation space is composed as  a dictionary
        self.observation_space = spaces.Dict({
                                        'Time': spaces.Box(low=0, high=1e10, shape=(1,)),
                                        'Position': spaces.Box(low=0, high=400, shape=(1,)),
                                        'Busy': spaces.Discrete(2),
                                        'Memory':spaces.Discrete(SatelliteSim.MEMORY_SIZE),
                                        'Images':spaces.Box(low=-1, high=SatelliteSim.MAX_TARGETS, shape=(SatelliteSim.MEMORY_SIZE,), dtype=np.int8),
                                        'Analysis':spaces.MultiBinary(SatelliteSim.MEMORY_SIZE),
                                        'Target Location': spaces.Box(low=-1, high=360, shape=(SatelliteSim.MAX_TARGETS, 2)),
                                        'Station Location': spaces.Box(low=-1, high=360, shape=(SatelliteSim.MAX_STATION, 2))
                                            })
        self.SatSim.reset()
        self.state = self.SatSim.get_state()
        self.Total_reward = 0

    def step(self, action, dt=1):

        next_state, done = self.SatSim.update(action, self.dt)
        reward = Reward(next_state, self.state, action)

        self.state = next_state
        self.Total_reward += reward
        info = {}
        observation = self.state
        return observation, reward, done, info

    def reset(self):
        self.SatSim.reset()
        self.state = self.SatSim.get_state()
        self.Total_reward = 0
        observation = self.state
        if self.debug:
            print('Observation_space')
            for k in self.observation_space:
                print(k)
                print(self.observation_space[k].shape)
            print('\n-------\n')
            print('Observation')
            for i,k in observation.items():
                print(i)
                if i == 'Busy' or i =='Memory':
                    k =np.array(k)
                
                print(k.shape)
        return observation 

    def render(self, mode='human'):
        self.view.drawSim(self.SatSim)

    def close (self):
        pygame.quit()