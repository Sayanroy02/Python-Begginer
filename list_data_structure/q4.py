"""
create 2 list and return common elements from two list 
"""

def common():
    l1 = [1,32,4,5,676,87,76]
    l2 = [22,1,678,78,5,76]
    list_1 = set(l1)  # create set of the list 
    list_2 = set(l2)  # create set of list 
    
    # apply the set theory method of intersection
    common = list_1.intersection(list_2)  # intersect list a with list b to find common
    all = list_1.union(list_2)  # union 


    print(f"Intersection = {common}")
    print(f"Union  = {all}")
common()