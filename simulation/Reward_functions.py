from simulation.Simulation import SatelliteSim

def Reward_v1(new_state, state, action):
    """
    First version of the reward function. The structure is define as:
        +10 Dumps analyzed image
        -10 per big fails (takes image over non valid zone, dumps image over non valid zone)
    
    Input: 
        - new_state =  dictionary
        - state = dictionary
        - action = integer representing each action
        - sim = curreent satellite simulation
    """ 
    R = 0
    if action!=3 and state['Busy']==1:
        R -= 50
    else:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=0.01*(new_state[3]-state[3])
            else:
                R-=10

        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=10*(new_state[4]-state[4])
            else:
                R-=10

    if action==3:
        # So the spacecraft does something
        R -= 0.001 
    return R