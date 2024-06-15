print('21012021001_ADESHARA BRIJESH')

class BayesNode:
    def __init__(self, name, dependent_list, prob_values):
        self.name = name
        self.dependent_list = dependent_list
        self.prob_values = prob_values

    def prob(self, obj_value, dependent_list):
        list_values = []
        for obj in self.dependent_list:
            list_values.append(dependent_list[obj.name])
        tuple_key = (obj_value, tuple(list_values))
        return self.prob_values.get(tuple_key, None)


class BurglaryAlarmProb:
    def __init__(self):
        self.burglary = BayesNode("B", [], {(True, ()): 0.001, (False, ()): 0.999})
        self.earthquake = BayesNode("E", [], {(True, ()): 0.002, (False, ()): 0.998})
        self.alarm = BayesNode("A", [self.burglary, self.earthquake], {
            (True, (True, True)): 0.95,
            (True, (True, False)): 0.94,
            (True, (False, True)): 0.29,
            (True, (False, False)): 0.001,
            (False, (True, True)): 0.05,
            (False, (True, False)): 0.06,
            (False, (False, True)): 0.71,
            (False, (False, False)): 0.999
        })
        self.J = BayesNode("J", [self.alarm], {
            (True, (True,)): 0.9,
            (True, (False,)): 0.05,
            (False, (True,)): 0.1,
            (False, (False,)): 0.95
        })
        self.M = BayesNode("M", [self.alarm], {
            (True, (True,)): 0.7,
            (True, (False,)): 0.01,
            (False, (True,)): 0.3,
            (False, (False,)): 0.99
        })

    def and_prob(self, J_value, B_value):
        prob = 0.0
        for A_value in [True, False]:
            prob1 = self.J.prob(J_value, {self.alarm.name: A_value})
            prob2 = 0.0
            for E_value in [True, False]:
                prob2 += self.alarm.prob(A_value, {self.burglary.name: B_value, self.earthquake.name: E_value}) * \
                         self.burglary.prob(B_value, {}) * self.earthquake.prob(E_value, {})
            prob += prob1 * prob2
        return prob

    def and_prob_JM(self, JM_value, B_value, consider_J):
        JM = self.J if consider_J else self.M
        prob = 0.0
        for A_value in [True, False]:
            prob1 = JM.prob(JM_value, {self.alarm.name: A_value})
            prob2 = 0.0
            for E_value in [True, False]:
                prob2 += self.alarm.prob(A_value, {self.burglary.name: B_value, self.earthquake.name: E_value}) * \
                         self.burglary.prob(B_value, {}) * self.earthquake.prob(E_value, {})
            prob += prob1 * prob2
        return prob

    def A_prob(self, A_value):
        prob = 0.0
        for B_value in [True, False]:
            for E_value in [True, False]:
                prob += self.alarm.prob(A_value, {self.burglary.name: B_value, self.earthquake.name: E_value}) * \
                        self.burglary.prob(B_value, {}) * self.earthquake.prob(E_value, {})
        return prob

burglary_alarm_prob = BurglaryAlarmProb()

print(f"P(J,B) = {burglary_alarm_prob.and_prob(True, True)}")
print(f"P(J',B) = {burglary_alarm_prob.and_prob(False, True)}")
print(f"P(J', B') = {burglary_alarm_prob.and_prob(False, False)}")
print(f"P(J,B') = {burglary_alarm_prob.and_prob(True, False)}")
print(f"P(M,B) = {burglary_alarm_prob.and_prob_JM(True, True, False)}")
print(f"P(M',B) = {burglary_alarm_prob.and_prob_JM(False, True, False)}")
print(f"P(M',B') = {burglary_alarm_prob.and_prob_JM(False, False, False)}")
print(f"P(M,B') {burglary_alarm_prob.and_prob_JM(True, False, False)}")
print(f"P(J) = {burglary_alarm_prob.J.prob(True, {burglary_alarm_prob.alarm.name: True})}")
print(f"P(M) = {burglary_alarm_prob.M.prob(True, {burglary_alarm_prob.alarm.name: True})}")
print(f"P(J') = {burglary_alarm_prob.J.prob(False, {burglary_alarm_prob.alarm.name: True})}")
print(f"P(M') = {burglary_alarm_prob.M.prob(False, {burglary_alarm_prob.alarm.name: True})}")
print(f"P(A) = {burglary_alarm_prob.A_prob(True)}")
print(f"P(A') = {burglary_alarm_prob.A_prob(False)}")
print(f"P(B|M) = {burglary_alarm_prob.and_prob_JM(True, True, False) / burglary_alarm_prob.M.prob(True, {burglary_alarm_prob.alarm.name: True})}")
print(f"P(B'|M) = {burglary_alarm_prob.and_prob_JM(False, False, False) / burglary_alarm_prob.M.prob(False, {burglary_alarm_prob.alarm.name: True})}")
print(f"P(B|J) = {burglary_alarm_prob.and_prob(True, True) / burglary_alarm_prob.J.prob(True, {burglary_alarm_prob.alarm.name: True})}")
print(f"P(B'|J) = {burglary_alarm_prob.and_prob(False, False) / burglary_alarm_prob.J.prob(False, {burglary_alarm_prob.alarm.name: True})}")