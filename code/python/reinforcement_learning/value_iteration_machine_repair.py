import numpy as np
import matplotlib.pyplot as plt

actions = [0, 1]
states = [1, 2, 3]
theta = 0.3
lamb = 3.0
cost = np.array([[lamb, 0], [lamb, 1], [lamb, 5]])
gamma = 0.9
probs = np.array([[[1., 0., 0.], [1., 0., 0.], [1., 0., 0.]],
                  [[1 - theta, theta, 0], [0, 1 - theta, theta], [0, 0, 1]]])

max_iter = 100
delta = 1e-5
values = [0, 0, 0]
pi = [None, None, None]
iter = 0

val_hist = []
pi_hist = []
iters = []


def get_policy_based_on_value(opt_val, gamma=0.9):

    policy = [None, None, None]

    for s_indx, _ in enumerate(states):
        act_value = [0, 0]
        for a_indx, _ in enumerate(actions):
            act_value[a_indx] = 0
            for next_state in range(s_indx, len(states)):
                act_value[a_indx] += (
                    cost[s_indx, a_indx] + gamma *
                    (probs[a_indx][s_indx][next_state] * opt_val[next_state]))
        policy[s_indx] = np.argmax(act_value)

    return policy


def plot_values(value, iters):

    # plot the state-value function
    plt.plot(iters,
             value[:, 0],
             color='green',
             marker='o',
             linestyle='dashed',
             linewidth=2,
             markersize=5,
             label='State 1')

    plt.plot(iters,
             value[:, 1],
             color='red',
             marker='o',
             linestyle='dashed',
             linewidth=2,
             markersize=5,
             label='State 2')

    plt.plot(iters,
             value[:, 2],
             color='blue',
             marker='o',
             linestyle='dashed',
             linewidth=2,
             markersize=5,
             label='State 3')

    plt.legend()
    plt.xlabel("Iteration K")
    plt.ylabel("Value")
    plt.title('State-Value Function')
    plt.show()


# Value Iteration Algorithm
while True:
    iter += 1
    max_diff = 0
    values_new = [0, 0, 0]
    for s_indx, _ in enumerate(states):
        max_val = 0
        next_act_vals = []
        for a_indx, _ in enumerate(actions):
            # The next_state will include the first-step reward
            # So we can start with zero.
            val = 0
            for next_state in range(s_indx, len(states)):
                val += (
                    cost[next_state, a_indx] + gamma *
                    (probs[a_indx][s_indx][next_state] * values[next_state]))
            next_act_vals.append(val)

        values_new[s_indx] = max(np.asarray(next_act_vals))
        max_diff = max(max_diff, abs(values[s_indx] - values_new[s_indx]))

    # Update value functions
    values = values_new
    current_pi = get_policy_based_on_value(values)
    val_hist.append(values[::-1])
    iters.append(iter)

    if max_diff < delta:
        print('It took iterations ', iter)
        pi = get_policy_based_on_value(values)
        # Adding one index because its zero-indexed
        pi = [x + 1 for x in pi]
        print('Policy ', pi[::-1])
        plot_values(np.asarray(val_hist), iters)
        break