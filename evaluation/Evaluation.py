import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

from agent import AgentInterface
from agent.AgentGreedy import GreedyAgent
from agent.AgentPDDL import PDDLAgent
from simulation.DrawSim import SatelliteView
from simulation.Simulation import SatelliteSim

def create_sim():
    # create simulation
    sim = SatelliteSim()
    sim.initRandomStations(2)
    sim.initRandomTargets(10)
    sim.goalRef.generateSingleGoals(list(range(len(sim.targets))), 5)
    sim.goalRef.generateCampaigns(list(range(len(sim.targets))), sim.goalRef.MAX_CAMPAIGNS)
    return sim

def create_agent():
    #agent = GreedyAgent()
    agent = PDDLAgent()
    agent.lock_step = True
    agent.verbose = 0
    return agent

def run_sim(sim: SatelliteSim, agent: AgentInterface):
    finished = False
    while not finished:
        action = agent.getAction(sim)
        finished = finished or sim.update(action, 1)
    return sim.goalRef.value

if __name__ == '__main__':
    pygame.display.init()

    results = []
    for i in range(10):
        s = create_sim()
        a = create_agent()
        v = run_sim(s,a)
        results.append(v)
        print(v)

    print(results)
    pygame.quit()
