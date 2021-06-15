import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from simulation.Simulation import SatelliteSim
from simulation.Reward_functions import Reward_f
from simulation.DrawSim import SatelliteView 
from stable_baselines3.common.vec_env import VecEnv
import pygame

# import the gym class and spaces
import gym
from gym import spaces

import numpy as np

class SimpleSat(gym.Env):

    def __init__(self,debug=False, 
                R_p=750, Write_ouput=False, Reward_version=2, Simulation_version=2,
                period=600):
        super(SimpleSat, self).__init__()
        """Custom Environment that follows gym interface"""
        metadata = {'render.modes': ['human']}

        # Set reward function
        self.R_p = R_p
        self.Reward = Reward_f[Reward_version-1]

        # Debuging
        self.debug = debug
        self.Write_ouput = Write_ouput

        # start render enviroment
        self.view = SatelliteView()

        # save the satelite enviroment
        self.SatSim = SatelliteSim(period,Simulation_version)
        self.t = 0
        self.dt= self.SatSim.PERIOD/SatelliteSim.CIRCUNFERENCE

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
                                        'Over Target': spaces.MultiBinary(SatelliteSim.MAX_TARGETS),
                                        'Over station': spaces.MultiBinary(SatelliteSim.MAX_STATION),
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
        if self.Write_ouput:
            if action == SatelliteSim.ACTION_TAKE_IMAGE:
                print('Take Image')
            elif action == SatelliteSim.ACTION_ANALYSE:
                print('Analyze')
            elif action == SatelliteSim.ACTION_DUMP:
                print('Dump')

        next_state, done = self.SatSim.update(action, self.dt)
        reward = self.Reward(next_state, self.state, action,R_p=self.R_p)

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