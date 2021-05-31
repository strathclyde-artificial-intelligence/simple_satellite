from stable_baselines3.common.env_checker import check_env

from simulation.RL_env import SimpleSat
from simulation.Simulation import SatelliteSim
from stable_baselines3 import PPO as agent
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor
Sim = SatelliteSim()
time_step =  Sim.PERIOD/SatelliteSim.CIRCUNFERENCE

# It will check your custom environment and output additional warnings if needed
env = SimpleSat(Sim, time_step, debug=True)
check_env(env)
env.close()

# Set agent and Wrappers
env.debug = False
env = Monitor(env, filename="Log_RL")
model = agent("MultiInputPolicy", env, verbose=1)

# Train
number_of_episodes = int(input("How many episodes to train? "))
episode_length = SatelliteSim.MAX_ORBITS*Sim.PERIOD 
model.learn(total_timesteps=int(episode_length*number_of_episodes))

# Evaluate the trained agent
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=100)
print(f"mean_reward:{mean_reward:.2f} +/- {std_reward:.2f}")
model.save("RL/Agent_{}".format(number_of_episodes))