# class node:
#     def _init_(self,name,dep,val):
#         self.name=name
#         self.dep=dep
#         self.val=val
# burglary=node("B",[],{True:0.001})
# earthquake=node("E",[],{True:0.002})
# alarm=node("A",[burglary,earthquake],{(True,True):0.95,(True,False):0.94,(False,True):0.29,(False,False):0.001,})
# john=node("J",[alarm],{True:0.90,False:0.05})
# mary=node("M",[alarm],{True:0.70,False:0.01})
# def prob(obj,dic):
#     list1=[]
#     for i in dic:
#         list1.append(dic[i])
#     print(obj.val[tuple(list1)])
# prob(alarm,{"B":True,"E":True})

# def and_prob(j_value, b_value):
#     prob = 0.0
#     for a_value in (True, False):
#         prob1 = j_prob(j_value, {a.name, a_value})
#         prob2 = 0.0
#         for e_value in (True, False):
#             prob2 += a_prob(a_value, {b.name, b_value, e.name, e_value}) * b_prob(b.value, {}) * e_prob(e.value, {})
#             prob += prob1 * prob2
#     return prob

# def a_prob(a_value):
#     prob = 0.0
#     for b_value in (True, False):
#         for e_value in (True, False):
#             prob += a_prob(a_value, {b.name, b_value, e.name, e_value}) * b_prob(b.value, {}) * e_prob(e.value, {})
#     return prob

# def j_prob(j_value):
#     prob = 0.0
#     for a_value in (True, False):
#         prob += j_prob(j_value, {a.name, a_value})
#     return prob

# def b_prob(b_value):
#     return b_prob(b_value, {})

# def e_prob(e_value):
#     return e_prob(e_value, {})

# print(and_prob(True, True)) # should be close to 0.8496
# print(and_prob(True, False)) # should be close to 0.0004
# print(and_prob(False, True)) # should be close to 0.0096
# print(and_prob(False, False)) # should be close to 0.1404
