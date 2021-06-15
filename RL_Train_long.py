import os
import numpy as np
from stable_baselines3.common.env_checker import check_env
from simulation.RL_env import SimpleSat
from simulation.Simulation import SatelliteSim
from stable_baselines3 import PPO as agent
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import VecEnv
from stable_baselines3.common.callbacks import CheckpointCallback, CallbackList, EvalCallback 
import IPython

R_p = int(input('Reward per succesful action: '))
Simulation_version = int(input('Simulation Version: '))
Reward_version = int(input('Reward Version: '))
number_of_episodes = int(input("How many episodes to train? "))
filename = "Full_Simulation_V{}_Reward_V{}_{}_Ep_{}".format(Simulation_version, Reward_version,R_p,number_of_episodes)

# It will check your custom environment and output additional warnings if needed
env = SimpleSat(debug=False, R_p=R_p, Reward_version=Reward_version, Simulation_version=Simulation_version)
episode_length = SatelliteSim.MAX_ORBITS*env.SatSim.PERIOD
#VecEnv(4, env.observation_space, env.action_space)
check_env(env)
env.close()
eval_env = SimpleSat( R_p=R_p, Reward_version=Reward_version, Simulation_version=Simulation_version)
# Call backs
n_episode_save = 100
checkpoint_callbac = CheckpointCallback(save_freq=episode_length*n_episode_save, save_path="RL/Agent/"+filename)
eval_callback = EvalCallback(eval_env, best_model_save_path='./RL/Agent/logs/best_model',
                             log_path='./RL/Agent/logs/results', eval_freq=episode_length*n_episode_save)
callback_list = CallbackList([checkpoint_callbac, eval_callback])

# Set agent and Wrappers
env.debug = False
model = agent("MultiInputPolicy", env, verbose=1, tensorboard_log="./RL/tensorboard/"+filename)

# Learning
model.learn(total_timesteps=int(episode_length*number_of_episodes), callback=callback_list)


print('Saving Model as '+filename)
model.save('RL/Agent/'+filename)
print('Finished '+str(epi_n))
print('Learning Ended')