from re import A
import numpy as np

actions = [0, 1]
states = [1, 2, 3]
theta = 0.3
lamb = 3.0
cost = np.array([[lamb, 0], [lamb, 1], [lamb, 5]])
gamma = 0.9
probs = np.array([[[1., 0., 0.], [1., 0., 0.], [1., 0., 0.]],
                  [[1 - theta, theta, 0], [0, 1 - theta, theta], [0, 0, 1]]])

max_iter = 100
values = [0, 0, 0]
pi = [0, 0, 0]
iter = 0
delta = 1e-5


def get_policy_based_on_value(opt_val, gamma=0.9):

    policy = [None, None, None]

    for s_indx, _ in enumerate(states):
        act_value = [0, 0]
        for a_indx, _ in enumerate(actions):
            act_value[a_indx] = cost[s_indx][a_indx]
            for next_state in range(s_indx, len(states)):
                act_value[a_indx] += (
                    cost[s_indx, a_indx] + gamma *
                    (probs[a_indx][s_indx][next_state] * opt_val[next_state]))
        policy[s_indx] = np.argmax(act_value)

    return policy


# Value Iteration Algorithm
while True:

    optimal_policy_found = True
    pi_current = [x + 1 for x in pi]
    print('Current Policy ', pi_current[::-1])

    iter += 1
    max_diff = 0
    V_new = [0, 0, 0]

    # Polic Evaluation Step
    for s_indx, _ in enumerate(states):
        max_val = 0
        for a_indx, _ in enumerate(actions):
            val = cost[s_indx][a_indx]
            for next_state in range(s_indx, len(states)):
                val += (
                    cost[next_state, a_indx] + gamma *
                    (probs[a_indx][s_indx][next_state] * values[next_state]))

        max_diff = max(max_diff, abs(val - values[s_indx]))

        values[s_indx] = val

    if max_diff < delta:
        break

    # Policy Iteration Step
    for s_indx, _ in enumerate(states):
        val_max = values[s_indx]
        act_value = [0, 0]
        for a_indx, a in enumerate(actions):
            val = cost[s_indx][a_indx]
            for next_state in range(s_indx, len(states)):
                val += (
                    cost[s_indx, a_indx] + gamma *
                    (probs[a_indx][s_indx][next_state] * values[next_state]))

            if val > val_max and pi[s_indx] != a:
                pi[s_indx] = a
                val_max = val
                optimal_policy_found = False

    if optimal_policy_found:
        pi_x = [x + 1 for x in pi[::-1]]
        print('Optimal Policy ', pi_x)
        print('Converged after ', iter)
        break