actionSimilarityMapping = {
    "0": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    "1": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    "2": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    "3": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    "4": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    "5": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    "6": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    "7": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    "8": [0, 0, 0, 0, 0, 0, 0, 0, 1],
}


def addFakeCarsToLane(state, lane, percentage):
    state['lane_waiting_vehicle_count'][lane] = state['lane_waiting_vehicle_count'][lane] + round(
        state['lane_waiting_vehicle_count'][lane] * percentage)
    return state


def swapLaneCounts(state, lane1, lane2):
    temp = state['lane_waiting_vehicle_count'][lane1]
    state['lane_waiting_vehicle_count'][lane1] = state['lane_waiting_vehicle_count'][lane2]
    state['lane_waiting_vehicle_count'][lane2] = temp
    return state


def adjustState(state):
    adjustedState = addFakeCarsToLane(state, 0, 0.1)
    adjustedState = swapLaneCounts(adjustedState, 2, 3)
    return adjustedState


def drawSimilarAction(action):
    from numpy.random import choice
    actions = [0, 1, 2, 3, 4, 5, 6, 7]
    actions.remove(action)
    probability_distribution = []
    for i in range(len(actions)):
        probability_distribution.append(actionSimilarityMapping[action][actions[i]])
    return choice(actions, 1, p=probability_distribution)
