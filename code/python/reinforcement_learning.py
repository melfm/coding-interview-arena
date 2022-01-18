import numpy as np
"""
Value Iteration Algorithm
"""


def one_step_lookahead(states, current_state, actions, transition, reward,
                       value, w):
    """
    Helper function to calculate the value for all action in a given state.
    
    Args:
        states: Array of states
        current_state: The state to consider (int)
        actions: Array of all actions
        transition: Transition matrix
        V: The value to use as an estimator, Vector of length env.nS
    
    Returns:
        A vector of length num_actions containing the expected value of each action.
    """
    act_len = len(actions)
    A = np.zeros(act_len)

    if current_state >= len(states) - 1:
        next_state = 0
    else:
        next_state = current_state + 1

    for a in range(act_len):
        prob = transition[current_state][w]
        if next_state == 0:
            next_state_val = 0
        else:
            next_state_val = value[next_state][w]
        A[a] += prob * (reward[current_state][a] + next_state_val)

    return A


def value_iteration():
    """
    This function uses the following value iteration algorithm:
    0. Set value function for all states to 0.
    1. For every state update the value function to:
            value[state] = optimal_reward + discount_factor * value(next_state)
        Where optimal_payoff is the maximum of expected payoffs when taking
        every possible action from the current state.
    2. Goto 1. unless the maximal value function update is less than tolerance.
    3. Extract the final optimal policy from the optimal value function.
    """

    states = [1, 2]
    W = [1, 2, 3]

    actions = [1, 2, 3]

    num_states = 2
    num_ws = 3
    num_actions = 3

    # P [from state] [to state] [action]
    P = [[0.25, 0.15, 0.05], [0.30, 0.10, 0.15]]

    cost = [[[3, 5, 1], [2, 3, 1]], [[4, 3, 1], [1, 2, 8]],
            [[1, 2, 2], [4, 1, 3]]]

    value = np.zeros(shape=(2, 3))

    num_iterations = 10

    for step in range(num_iterations):

        # Rows in the state space
        for s in range(num_states):
            # Cols in the state space
            for w in range(num_ws):
                cost_w = cost[w]
                # Do a one-step lookahead to find the best action
                A = one_step_lookahead(states, s, actions, P, cost_w, value, w)
                best_action_value = np.max(A)
                value[s][w] = best_action_value

    # Create a deterministic policy using the optimal value function
    policy = np.zeros([num_states, num_actions])
    for s in range(num_states):
        for w in range(num_ws):
            cost_w = cost[w]
            # One step lookahead to find the best action for this state
            A = one_step_lookahead(states, s, actions, P, cost_w, value, w)
            best_action = np.argmax(A)
            print('Best action ', best_action)
            # Always take the best action
            policy[s, best_action] = best_action

    print('Value \n', value)
    print('Policy \n', policy)


def main():
    value_iteration()


if __name__ == "__main__":
    main()
