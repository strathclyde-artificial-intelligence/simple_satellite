import os
import numpy as np
from stable_baselines3.common.env_checker import check_env
from simulation.RL_env import SimpleSat
from simulation.Simulation import SatelliteSim
from stable_baselines3 import PPO as agent
from stable_baselines3.common.monitor import Monitor
import IPython

R_p = int(input('Reward per succesful action: '))
Simulation_version = int(input('Simulation Version: '))
Reward_version = int(input('Reward Version: '))

# It will check your custom environment and output additional warnings if needed
env = SimpleSat(debug=True, R_p=R_p, Reward_version=Reward_version, Simulation_version=Simulation_version)
check_env(env)
env.close()

number_of_episodes = int(input("How many episodes to train? "))
filename = "Simulation_V{}_Reward_V{}_{}_Ep_{}".format(Simulation_version, Reward_version,R_p,number_of_episodes)

# Set agent and Wrappers
env.debug = False
env = Monitor(env, filename="RL/Log_RL")
model = agent("MultiInputPolicy", env, verbose=1, tensorboard_log="./RL/tensorboard/"+filename)


epi_min = 0
for filename in os.listdir("./RL/Agent"):
    filename=filename[:-4]
    file_list = filename.split('_')
    R_p_c = int(file_list[4])
    R_v_c = int(file_list[3][1])
    S_v_c = int(file_list[1][1])
    if R_p_c== R_p and R_v_c == Reward_version and S_v_c==Simulation_version:
        noE = int(file_list[6])
        if noE > epi_min:
            epi_min = noE
div_epi = [int(i*300) for i in range((epi_min//300),(number_of_episodes//300)+1)]
if number_of_episodes%300 != 0:
    div_epi.append(number_of_episodes)
filename = "Simulation_V{}_Reward_V{}_{}_Ep_{}".format(Simulation_version, Reward_version,R_p,epi_min)

# Train
print('\n-----------------------\n')
for i in range(1,len(div_epi)):
    epi_n = div_epi[i]
    if filename!="Simulation_V{}_Reward_V{}_{}_Ep_{}".format(Simulation_version, Reward_version,R_p,0):
        model.load('RL/Agent/'+filename)
        print('Loaded '+ filename)

    filename = "Simulation_V{}_Reward_V{}_{}_Ep_{}".format(Simulation_version, Reward_version,R_p,epi_n)
    episode_length = SatelliteSim.MAX_ORBITS*env.SatSim.PERIOD 
    model.learn(total_timesteps=int(episode_length*epi_n))
    #filename = input('save model as: ')


    print('Saving Model as '+filename)
    model.save('RL/Agent/'+filename)
    print('Finished '+str(epi_n))
print('Learning Ended')
