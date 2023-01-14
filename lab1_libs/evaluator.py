from random import randint, shuffle
from colorama import Fore, Back, Style
from .searchtree import SearchNode

def correct_dfs(root, goal):
    stack = [root]
    
    current_nodes = [] # this will store the history of current nodes
    added_nodes = [] # this will store the history of nodes that were added
    
    while stack: # this loop will terminate when the stack is empty
        # pop the last element from the list and assign it to a variable called current
        
        current = stack.pop(-1)
        
        current_nodes.append(current.label)
        
        # if ever we reach the goal, the function will return early with our history
        if current.label == goal:
            return True, current_nodes, added_nodes # returns a tuple containing our history
        
        if current.children is not None: # checks if the current node has children
            # add the children to the stack, starting with the first child, in order
            # remember *not* to pop the children; your code will misbehave if you do!
            
            for child in current.children:
                stack.append(child)
            
            added_nodes.append(current.children)
        else:
            added_nodes.append([]) # to keep track of our steps properly, add an empty list
    
    # If the search didn't return early, it means we failed (if it did, we'll never reach this point)
    return False, current_nodes, added_nodes

def correct_bfs(root, goal):
    stack = [root]
    
    current_nodes = [] # this will store the history of current nodes
    added_nodes = [] # this will store the history of nodes that were added
    
    while stack: # this loop will terminate when the stack is empty
        # pop the last element from the list and assign it to a variable called current
        
        current = stack.pop(0)
        
        current_nodes.append(current.label)
        
        # if ever we reach the goal, the function will return early with our history
        if current.label == goal:
            return True, current_nodes, added_nodes # returns a tuple containing our history
        
        if current.children is not None: # checks if the current node has children
            # add the children to the stack, starting with the first child, in order
            # remember *not* to pop the children; your code will misbehave if you do!
            
            for child in current.children:
                stack.append(child)
            
            added_nodes.append(current.children)
        else:
            added_nodes.append([]) # to keep track of our steps properly, add an empty list
    
    # If the search didn't return early, it means we failed (if it did, we'll never reach this point)
    return False, current_nodes, added_nodes

def childnames(children):
    return [child.label for child in children]

def make_a_tree():
    i, e, g, h = (SearchNode(lbl, heur) for lbl, heur in (("I", 3), ("E", 2), ("G", 1), ("H", 4)))
    b, f, d = (SearchNode(lbl, heur, ch) for lbl, heur, ch in (("B", 4, e), ("F", 3, i), ("D", 1, h)))
    c = SearchNode("C", 3, [f, g])
    root = SearchNode("A", 4, [b, c, d])
    return root

def evaluate(f):
    if f.__name__ == 'loop_summer':
        things_to_try = []
        
        for _ in range(50):
            thing = list(range(randint(-1000, 1000), randint(-1000, 1000)))
            shuffle(thing)
            things_to_try.append(thing)
            
        for thing in things_to_try:
            result = f(thing)
            if result != sum(thing):
                print(f'Oops! Function {Fore.RED}got the wrong sum{Fore.BLACK} for the following list:\n {list(thing)}')
                return
            elif type(result) is not int:
                print(f'Oops! Function {Fore.RED}did not return an integer{Fore.BLACK} for the following list:\n{list(thing)}')
                return
            
        exsol = 'a for loop, written "for i in ints:" that adds each element of the list to a variable, which has been initialized to 0 earlier.'
        
    elif f.__name__ == 'stack_pop':
        things_to_try = []
        for _ in range(50):
            thing = list(range(randint(0, 100), randint(110, 1000)))
            shuffle(thing)
            
            for i, v in enumerate(thing):
                match randint(0, 5):
                    case 1:
                        thing[i] = str(v)
                    case 2:
                        thing[i] = float(v)
                    case 3:
                        thing[i] = [v]
                    case 4:
                        thing[i] = {'i': v}
            
            things_to_try.append(thing)
            
            for thing in things_to_try:
                if len(thing) < 5:
                    continue
                result = f(thing.copy())
                
                if result != [thing.pop(-1) for _ in range(5)][-1]:
                    print(f'Oops! Function {Fore.RED}got the wrong value{Fore.BLACK} ({result}) for list:\n{thing}')
                    return
            
            exsol = 'a while loop that iterates five times, setting a variable equal to ls.pop(-1) at each step, which is returned at the end of the loop.'
        
    elif f.__name__ == 'queue_pop':
        things_to_try = []
        for _ in range(50):
            thing = list(range(randint(0, 100), randint(110, 1000)))
            shuffle(thing)
            
            for i, v in enumerate(thing):
                match randint(0, 5):
                    case 1:
                        thing[i] = str(v)
                    case 2:
                        thing[i] = float(v)
                    case 3:
                        thing[i] = [v]
                    case 4:
                        thing[i] = {'i': v}
            
            things_to_try.append(thing)
            
            for thing in things_to_try:
                if len(thing) < 5:
                    continue
                result = f(thing.copy())
                
                if result != [thing.pop(0) for _ in range(5)][-1]:
                    print(f'Oops! Function {Fore.RED}got the wrong value{Fore.BLACK} ({result}) for list:\n{thing}')
                    return
            
            exsol = 'a while loop that iterates five times, setting a variable equal to ls.pop(0) at each step, which is returned at the end of the loop.'
        
    elif f.__name__ == 'dfs': 
        root = make_a_tree()
        
        goals = ["I", "H", "W", "Q", "A", "C", "V", "G"]
        
        for goal in goals:
            _, result_c, result_a = f(root, goal)
            
            _, correct_c, correct_a = correct_dfs(root, goal)
            
            if len(correct_c) != len(result_c):
                print(f'Oops! Function got the wrong value for goal {goal}')
                print(f'Got {result_c}, \nexpected {correct_c}')
                print("Make sure you're adding children in the right order!")
                return
            
            for res, cor in zip(result_c, correct_c):
                if res != cor:
                    print(f'Oops! Function got the wrong value for goal {goal}')
                    print(f'Got {result_c}, \nexpected {correct_c}')
                    print("Make sure you're adding children in the right order!")
                    return
                
            if len(correct_a) != len(result_a):
                print(f'Oops! Function got the wrong value for goal {goal}')
                print(f'Got {childnames(result_a)}, \nexpected {childnames(correct_a)}')
                print("Make sure you're adding children in the right order!")
                return
            
            for res, cor in zip(result_a, correct_a):
                if len(res) != len(cor):
                    print(f'Oops! Function got the wrong value for goal {goal}')
                    print(f'Got {childnames(result_a)}, \nexpected {childnames(correct_a)}')
                    print("Make sure you're adding children in the right order!")
                    return
                for rc, cc in zip(childnames(res), childnames(cor)):
                    if rc != cc:
                        print(f'Oops! Function got the wrong value for goal {goal}')
                        print(f'Got {childnames(result_a)}, \nexpected {childnames(correct_a)}')
                        print("Make sure you're adding children in the right order!")
                        return
                    
        exsol = 'in position [1], set current = stack.pop(0), and in position [2] write a for loop\n\nfor child in current.children:\n    stack.append(child)'
            
                
    elif f.__name__ == 'bfs':
        root = make_a_tree()
        
        goals = ["I", "H", "W", "Q", "A", "C", "V", "G"]
        
        for goal in goals:
            _, result_c, result_a = f(root, goal)
            
            _, correct_c, correct_a = correct_bfs(root, goal)
            
            if len(correct_c) != len(result_c):
                print(f'Oops! Function got the wrong value for goal {goal}')
                print(f'Got {result_c}, \nexpected {correct_c}')
                print("Make sure you're adding children in the right order!")
                return
            
            for res, cor in zip(result_c, correct_c):
                if res != cor:
                    print(f'Oops! Function got the wrong value for goal {goal}')
                    print(f'Got {result_c}, \nexpected {correct_c}')
                    print("Make sure you're adding children in the right order!")
                    return
                
            if len(correct_a) != len(result_a):
                print(f'Oops! Function got the wrong value for goal {goal}')
                print(f'Got {childnames(result_a)}, \nexpected {childnames(correct_a)}')
                print("Make sure you're adding children in the right order!")
                return
            
            for res, cor in zip(result_a, correct_a):
                if len(res) != len(cor):
                    print(f'Oops! Function got the wrong value for goal {goal}')
                    print(f'Got {childnames(result_a)}, \nexpected {childnames(correct_a)}')
                    print("Make sure you're adding children in the right order!")
                    return
                for rc, cc in zip(childnames(res), childnames(cor)):
                    if rc != cc:
                        print(f'Oops! Function got the wrong value for goal {goal}')
                        print(f'Got {childnames(result_a)}, \nexpected {childnames(correct_a)}')
                        print("Make sure you're adding children in the right order!")
                        return
                    
        exsol = 'in position [1], set current = stack.pop(-1), and in position [2] write a for loop\n\nfor child in current.children:\n    stack.append(child)\n'
    else:    
        print('Invalid function name, remember not to rename your function!')
        return
        
    print(f'\nEvaluation of {f.__name__}\n===')
    print(f'{Fore.RED}Tests look good. How did you solve the problem?{Fore.BLACK}\n')
    input()
    print(f'{Fore.GREEN}\nAn example solution would be {exsol}\n{Fore.BLACK}')
    print(f'{Fore.RED}Was this the same as your solution? If it differed, how? Did your explanation contain any mistakes or missing details?\n{Fore.BLACK}')
    input()
