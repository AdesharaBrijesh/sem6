class Node:
    def __init__(self, name, child, parent):
        self.name = name
        self.child = child
        self.parent = parent
        
class Tree:
    def __init__(self, root):
        self.root = root
        
    def Insert_node(self, name, parent):
        child_node = Node(name, [], parent)
        parent.child.append(child_node)
        return child_node
    
 


obj_amit = Node("Amit", [], None)
tree = Tree(obj_amit)

obj_rahul = tree.Insert_node("Rahul", obj_amit)
obj_sanjay = tree.Insert_node("Sanjay", obj_rahul)
obj_ravi = tree.Insert_node("Ravi", obj_rahul)
obj_deepak = tree.Insert_node("Deepak", obj_sanjay)
obj_raj = tree.Insert_node("Raj", obj_sanjay)
obj_suresh = tree.Insert_node("Suresh", obj_sanjay)
obj_meena = tree.Insert_node("Meena", obj_suresh)
obj_reena = tree.Insert_node("Reena", obj_meena)
obj_gaurav = tree.Insert_node("Gaurav", obj_raj)
obj_aditya = tree.Insert_node("Aditya", obj_gaurav)
obj_sneha = tree.Insert_node("Sneha", obj_gaurav)
obj_alice = tree.Insert_node("Alice", obj_gaurav)
obj_carol = tree.Insert_node("Carol", obj_alice)
obj_dave = tree.Insert_node("Dave", obj_alice)
obj_anjali = tree.Insert_node("Anjali", obj_sneha)
obj_arjun = tree.Insert_node("Arjun", obj_sneha)
obj_sachin = tree.Insert_node("Sachin", obj_arjun)
obj_sumit = tree.Insert_node("Sumit", obj_arjun)
obj_nidhi = tree.Insert_node("Nidhi", obj_anjali)
obj_prem = tree.Insert_node("Prem", obj_nidhi)
obj_lina = tree.Insert_node("Lina", obj_nidhi)
obj_akash = tree.Insert_node("Akash", obj_deepak)
obj_vinay = tree.Insert_node("Vinay", obj_deepak)
obj_ankit = tree.Insert_node("Ankit", obj_vinay)
obj_harsh = tree.Insert_node("Harsh", obj_vinay)
obj_puneet = tree.Insert_node("Puneet", obj_harsh)
obj_vikas = tree.Insert_node("Vikas", obj_harsh)
obj_varun = tree.Insert_node("Varun", obj_harsh)
obj_abhishek = tree.Insert_node("Abhishek", obj_ankit)
obj_rohan = tree.Insert_node("Rohan", obj_abhishek)
obj_ajay = tree.Insert_node("Ajay", obj_abhishek)
obj_aruna = tree.Insert_node("Aruna", obj_rohan)
obj_ramji = tree.Insert_node("Ramji", obj_rohan)
obj_virat = tree.Insert_node("Virat", obj_ajay)
obj_isha = tree.Insert_node("Isha", obj_ajay)


obj_priya = tree.Insert_node("Priya", obj_amit)
obj_nisha = tree.Insert_node("Nisha", obj_priya)
obj_claire = tree.Insert_node("Claire", obj_priya)
obj_eric = tree.Insert_node("Eric", obj_claire)
obj_lisa = tree.Insert_node("Lisa", obj_nisha)
obj_sam = tree.Insert_node("Sam", obj_lisa)
obj_john = tree.Insert_node("John", obj_lisa)


   
def bfs_search(tree, search_string):
    queue = [tree.root]
    execution = 0
    while(len(queue)!= 0):
        execution += 1
        pop_node = queue.pop(0)
        if(pop_node.name == search_string):
            print("execution with BFS : ", execution)
            return pop_node
        queue.extend(pop_node.child)
    return None    
    
def dfs_search(tree, search_string):
    queue = [tree.root]
    execution = 0
    while(len(queue)!= 0):
        execution += 1
        pop_node = queue.pop(len(queue)-1)
        if(pop_node.name == search_string):
            print("execution with DFS : ", execution)
            return pop_node
        queue.extend(pop_node.child)
    return None  


def print_path(Node):
    r_list = []
    while(Node != None):
        r_list.append(Node.name)
        Node = Node.parent
    rev_list = r_list[::-1]
    print("path:",'->'.join(rev_list))
    print("path cost : ", len(rev_list))
    
    
search_string = input("enter the node to search : ")
result1 = dfs_search(tree, search_string)
result = bfs_search(tree, search_string)


if(result!= None):
    print_path(result)
else:
    print("search string is not a variable in tree")
