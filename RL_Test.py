import os
from simulation.RL_env import SimpleSat
from simulation.Simulation import SatelliteSim
from stable_baselines3 import PPO as agent
 
print('')
for filename in os.listdir("./RL/Agent"):
    filename=filename[:-4]
    print(filename)

filename = input('\nwhich file to evaluate? \n')
model = agent.load('RL/Agent/'+filename)

file_list = filename.split('_')
R_p = int(file_list[4])
Reward_version = int(file_list[3][1])
Simulation_version = int(file_list[1][1])

env = SimpleSat(Write_ouput=True, R_p=R_p, Reward_version=Reward_version, Simulation_version=Simulation_version)
obs = env.reset()

episode_length = SatelliteSim.MAX_ORBITS*env.SatSim.PERIOD 
number_of_episodes=1
Total_reward = 0
for i in range(int(episode_length*number_of_episodes)):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action) 
    Total_reward += rewards
    if i%(round(env.SatSim.PERIOD/4))== 0:    
        print('Accumulated Reward = {}'.format(Total_reward))
    env.render()

env.close()