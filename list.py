import random 
 
def generate_starting_list(n, min_val, max_val): 
    list = [] 
 
    for _ in range(n): 
        value = random.randint(min_val, max_val) 
        list.append(value) 
     
    return list 
 
 
