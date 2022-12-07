"""Value iteration toy example.
http://incompleteideas.net/book/ebook/node44.html
"""

import numpy as np

# Initialize Markov Decision Process model
# actions (0=left, 1=right)
actions = [0, 1]
states = [0, 1, 2, 3, 4]
# reward per state
rewards = [-1, -1, 10, -1, -1]
gamma = 0.9
# deterministic transition prob
transition_p = 1.0
iterations = 50
stopping_threshold = 0.5


def lookahead_best_act_value(values, current_s):
    best_act_val = np.zeros(len(actions))
    for a in actions:
        reward = rewards[current_s]
        # Terminal state
        if (current_s + a) >= len(states):
            best_act_val[a] = reward
        else:
            best_act_val[a] += transition_p * (reward +
                                               gamma * values[current_s + a])

    return best_act_val


def value_iteration():

    new_values = np.zeros(len(states))

    for iter in range(iterations):
        delta = 0
        for s in range(len(states)):
            best_act_val = lookahead_best_act_value(new_values, s)
            delta = max(delta, abs(max(best_act_val) - new_values[s]))
            new_values[s] = max(best_act_val)

        if delta < stopping_threshold:
            break

        print('Iteration : ', iter, ' Values: ', new_values)

    return new_values


def optimal_policy(values):
    policy = np.zeros([len(states), len(actions)])

    for s in range(len(states)):
        best_act_val = lookahead_best_act_value(values, s)
        best_action = np.argmax(best_act_val)
        policy[s, best_action] = 1.0

    print('Optimal Policy ', policy)
    return policy

values = value_iteration()
policy = optimal_policy(values)
