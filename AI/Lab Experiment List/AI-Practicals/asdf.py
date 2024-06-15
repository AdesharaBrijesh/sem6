class Q:
    def __init__(self):
        self.q_values = {
            ('rich', 'plant'): 0,
            ('rich', 'fallow'): 0,
            ('poor', 'plant'): 0,
            ('poor', 'fallow'): 0
        }


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
