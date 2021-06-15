from simulation.Simulation import SatelliteSim
import IPython
def Reward_v1(new_state, state, action, R_p=1000):
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
    elif state['Busy']==0:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=R_p
            else:
                R-=10
        if action == SatelliteSim.ACTION_ANALYSE:
            if any([new_state['Analysis'][i] != state['Analysis'][i] for i in range(SatelliteSim.MEMORY_SIZE)]):
                R+=R_p
            else:
                R-=10
                
        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=R_p
            else:
                R-=10

        if action==SatelliteSim.ACTION_DO_NOTHING:
            # So the spacecraft does something
            if any([state['Target Location'][i, 0] < state['Position'][0] < state['Target Location'][i, 1] for i in range(SatelliteSim.MAX_TARGETS)]):
                R -= 1
            elif any([state['Analysis'][i] == 0 and state['Images'][i]>-0.5 for i in range(SatelliteSim.MEMORY_SIZE)]): 
                R -= 1
            elif any([state['Station Location'][i, 0] < state['Position'][0] < state['Station Location'][i, 1] for i in range(SatelliteSim.MAX_STATION)]):
                R -= 1
    #if R > 1:
    #    print('Yeah reward\n')
    return R


def Reward_v2(new_state, state, action, R_p=1000):
    R = 0
    if action!=3 and state['Busy']==1:
        R -= 50
    elif state['Busy']==0:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=R_p
            else:
                R-=10
        if action == SatelliteSim.ACTION_ANALYSE:
            if any([new_state['Analysis'][i] != state['Analysis'][i] for i in range(SatelliteSim.MEMORY_SIZE)]):
                R+=2*R_p
            else:
                R-=10
                
        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=4*R_p
            else:
                R-=10

        if action==SatelliteSim.ACTION_DO_NOTHING:
            # So the spacecraft does something
            if any([state['Target Location'][i, 0] < state['Position'][0] < state['Target Location'][i, 1] for i in range(SatelliteSim.MAX_TARGETS)]):
                R -= 1
            elif any([state['Analysis'][i] == 0 and state['Images'][i]>-0.5 for i in range(SatelliteSim.MEMORY_SIZE)]): 
                R -= 1
            elif any([state['Station Location'][i, 0] < state['Position'][0] < state['Station Location'][i, 1] for i in range(SatelliteSim.MAX_STATION)]):
                R -= 1
    #if R > 1:
    #    print('Yeah reward\n')
    return R

def Reward_v3(new_state, state, action, R_p=1000):
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
    elif state['Busy']==0:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=R_p
            else:
                R-=10
        if action == SatelliteSim.ACTION_ANALYSE:
            if any([new_state['Analysis'][i] != state['Analysis'][i] for i in range(SatelliteSim.MEMORY_SIZE)]):
                R+=.1*R_p
            else:
                R-=10
                
        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=4*R_p
            else:
                R-=10

        if action==SatelliteSim.ACTION_DO_NOTHING:
            # So the spacecraft does something
            if any([state['Target Location'][i, 0] < state['Position'][0] < state['Target Location'][i, 1] for i in range(SatelliteSim.MAX_TARGETS)]):
                R -= 1
            elif any([state['Analysis'][i] == 0 and state['Images'][i]>-0.5 for i in range(SatelliteSim.MEMORY_SIZE)]): 
                R -= 1
            elif any([state['Station Location'][i, 0] < state['Position'][0] < state['Station Location'][i, 1] for i in range(SatelliteSim.MAX_STATION)]):
                R -= 1
    #if R > 1:
    #    print('Yeah reward\n')
    return R

def Reward_v4(new_state, state, action, R_p=1000):
    R = 0
    if action!=3 and state['Busy']==1:
        R -= 500
    elif state['Busy']==0:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=R_p
            else:
                R-=10
        if action == SatelliteSim.ACTION_ANALYSE:
            if any([new_state['Analysis'][i] != state['Analysis'][i] for i in range(SatelliteSim.MEMORY_SIZE)]):
                R+=.1*R_p
            else:
                R-=10
                
        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=4*R_p
            else:
                R-=10

        if action==SatelliteSim.ACTION_DO_NOTHING:
            # So the spacecraft does something
            if any([state['Target Location'][i, 0] < state['Position'][0] < state['Target Location'][i, 1] for i in range(SatelliteSim.MAX_TARGETS)]):
                R -= 1
            elif any([state['Analysis'][i] == 0 and state['Images'][i]>-0.5 for i in range(SatelliteSim.MEMORY_SIZE)]): 
                R -= 1
            elif any([state['Station Location'][i, 0] < state['Position'][0] < state['Station Location'][i, 1] for i in range(SatelliteSim.MAX_STATION)]):
                R -= 1
    return R

def Reward_v5(new_state, state, action, R_p=1000):
    R = 0
    if action!=3 and state['Busy']==1:
        R -= 50000
    elif state['Busy']==0:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=R_p
            else:
                R-=10
        if action == SatelliteSim.ACTION_ANALYSE:
            if any([new_state['Analysis'][i] != state['Analysis'][i] for i in range(SatelliteSim.MEMORY_SIZE)]):
                R+=R_p
            else:
                R-=10
                
        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=2*R_p
            else:
                R-=10
        """
        if action==SatelliteSim.ACTION_DO_NOTHING:
            # So the spacecraft does something
            if any([state['Target Location'][i, 0] < state['Position'][0] < state['Target Location'][i, 1] for i in range(SatelliteSim.MAX_TARGETS)]):
                R -= 1
            elif any([state['Analysis'][i] == 0 and state['Images'][i]>-0.5 for i in range(SatelliteSim.MEMORY_SIZE)]): 
                R -= 1
            elif any([state['Station Location'][i, 0] < state['Position'][0] < state['Station Location'][i, 1] for i in range(SatelliteSim.MAX_STATION)]):
                R -= 1
        """
    return R

def Reward_v6(new_state, state, action, R_p=1000):
    R = 0
    if action!=3 and state['Busy']==1:
        R -= 500
    elif state['Busy']==0:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=R_p
            else:
                R-=10
        if action == SatelliteSim.ACTION_ANALYSE:
            if any([new_state['Analysis'][i] != state['Analysis'][i] for i in range(SatelliteSim.MEMORY_SIZE)]):
                R+=R_p
            else:
                R-=10
                
        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=2*R_p
            else:
                R-=10

        if action==SatelliteSim.ACTION_DO_NOTHING:
            # So the spacecraft does something
            if any([state['Target Location'][i, 0] < state['Position'][0] < state['Target Location'][i, 1] for i in range(SatelliteSim.MAX_TARGETS)]):
                R -= 10
            elif any([state['Analysis'][i] == 0 and state['Images'][i]>-0.5 for i in range(SatelliteSim.MEMORY_SIZE)]): 
                R -= 10
            elif any([state['Station Location'][i, 0] < state['Position'][0] < state['Station Location'][i, 1] for i in range(SatelliteSim.MAX_STATION)]):
                R -= 10
            else:
                R+=0.1*R_p
    return R

def Reward_v7(new_state, state, action, R_p=1000):
    R = 0
    if action!=3 and state['Busy']==1:
        R -= 50
    elif state['Busy']==0:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=R_p
            else:
                distance = [abs((state['Target Location'][i, 0] + state['Target Location'][i, 1])/2-state['Position']) for i in range(SatelliteSim.MAX_STATION)]
                min_dis = min(distance)
                R-= min_dis[0]

        if action == SatelliteSim.ACTION_ANALYSE:
            if any([new_state['Analysis'][i] != state['Analysis'][i] for i in range(SatelliteSim.MEMORY_SIZE)]):
                R+=2*R_p
            else:
                R-=10
                
        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=4*R_p
            else:
                distance = [abs((state['Station Location'][i, 0] + state['Station Location'][i, 1])/2-state['Position']) for i in range(SatelliteSim.MAX_STATION)]
                min_dis = min(distance)
                R-= min_dis[0]

        if action==SatelliteSim.ACTION_DO_NOTHING:
            # So the spacecraft does something
            if any([state['Target Location'][i, 0] < state['Position'][0] < state['Target Location'][i, 1] for i in range(SatelliteSim.MAX_TARGETS)]):
                R -= 1
            elif any([state['Analysis'][i] == 0 and state['Images'][i]>-0.5 for i in range(SatelliteSim.MEMORY_SIZE)]): 
                R -= 1
            elif any([state['Station Location'][i, 0] < state['Position'][0] < state['Station Location'][i, 1] for i in range(SatelliteSim.MAX_STATION)]):
                R -= 1
    #if R > 1:
    #    print('Yeah reward\n')
    return R

def Reward_v8(new_state, state, action, R_p=1000):
    R = 0
    if action!=3 and state['Busy']==1:
        R -= 50
    elif state['Busy']==0:
        if action == SatelliteSim.ACTION_TAKE_IMAGE:
            # Picture were correctly taken
            if state['Memory']<new_state['Memory']:
                R+=R_p
            else:
                R-=10
        if action == SatelliteSim.ACTION_ANALYSE:
            if any([new_state['Analysis'][i] != state['Analysis'][i] for i in range(SatelliteSim.MEMORY_SIZE)]):
                R+=R_p
            else:
                R-=10
                
        if action == SatelliteSim.ACTION_DUMP:
            # Files have been correctly dumped
            if state['Memory'] > new_state['Memory']:
                R+=2*R_p
            else:
                R-=10

        if action==SatelliteSim.ACTION_DO_NOTHING:
            # So the spacecraft does something
            if any([state['Target Location'][i, 0] < state['Position'][0] < state['Target Location'][i, 1] for i in range(SatelliteSim.MAX_TARGETS)]):
                R -= 1
            elif any([state['Analysis'][i] == 0 and state['Images'][i]>-0.5 for i in range(SatelliteSim.MEMORY_SIZE)]): 
                R -= 1
            elif any([state['Station Location'][i, 0] < state['Position'][0] < state['Station Location'][i, 1] for i in range(SatelliteSim.MAX_STATION)]):
                R -= 1
    #if R > 1:
    #    print('Yeah reward\n')
    return R
Reward_f = [Reward_v1, Reward_v2, Reward_v3, Reward_v4, Reward_v5, Reward_v6, Reward_v7, Reward_v8]