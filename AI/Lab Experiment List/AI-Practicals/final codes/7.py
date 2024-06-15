print('21012021001_ADESHARA BRIJESH\n')

class Q:
    def __init__(self):
        self.q_values = {
            ('rich', 'plant'): 0,
            ('rich', 'fallow'): 0,
            ('poor', 'plant'): 0,
            ('poor', 'fallow'): 0
        }

    def __str__(self):
        return '\n'.join([f'Q({state}, {action}) = {value:.2f}' for (state, action), value in self.q_values.items()])

class FarmerEnvironment:
    def __init__(self, gamma=0.9):
        self.states = ['rich', 'poor']
        self.actions = ['plant', 'fallow']
        self.transition_probs = {
            ('rich', 'plant'): {'rich': 0.1, 'poor': 0.9},
            ('rich', 'fallow'): {'rich': 0.9, 'poor': 0.1},
            ('poor', 'plant'): {'rich': 0.1, 'poor': 0.9},
            ('poor', 'fallow'): {'rich': 0.9, 'poor': 0.1}
        }
        self.rewards = {
            ('rich', 'plant'): 100,
            ('rich', 'fallow'): 0,
            ('poor', 'plant'): 10,
            ('poor', 'fallow'): 0
        }
        self.gamma = gamma
        self.q_values = Q()

    def q_value_iteration(self, num_iterations=1000, epsilon=0.01):
        for _ in range(num_iterations):
            q_values_prev = self.q_values.q_values.copy()
            for state in self.states:
                for action in self.actions:
                    q_value = self.rewards[(state, action)]
                    for next_state, prob in self.transition_probs[(state, action)].items():
                        q_value += self.gamma * prob * max([self.q_values.q_values[(next_state, next_action)] for next_action in self.actions])
                    self.q_values.q_values[(state, action)] = q_value
            max_diff = max([abs(self.q_values.q_values[(state, action)] - q_values_prev[(state, action)]) for state in self.states for action in self.actions])
            if max_diff < epsilon:
                break

    def get_optimal_policy(self):
        policy = {}
        for state in self.states:
            optimal_action = max([(action, self.q_values.q_values[(state, action)]) for action in self.actions], key=lambda x: x[1])[0]
            policy[state] = optimal_action
        return policy

if __name__ == '__main__':
    env = FarmerEnvironment()
    env.q_value_iteration()
    print('Q-values:')
    print(env.q_values)
    optimal_policy = env.get_optimal_policy()
    print('\nOptimal policy:')
    for state, action in optimal_policy.items():
        print(f'State: {state}, Action: {action}')