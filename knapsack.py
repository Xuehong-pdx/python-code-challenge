"""As a burgler robs a house, she finds the following items:
    Dirt - Weight: 4, Value: 0
    Computer - Weight: 10, Value: 30
    Fork - Weight: 5, Value: 1
    Problem Set - Weight: 0, Value: -10
She can only carry a weight of 14, and wishes to maximize the value to weight 
ratio of the things she carries. She employs three different metrics in an attempt to do 
this, and writes an algorithm in Python to determine which loot to take.

The algorithm works as follows:
    Evaluate the metric of each item. Each metric returns a numerical value for each item.
    For each item, from highest metric value to lowest, add the item if there is room in the bag.
"""

items = [['Dirt', 4, 0], 
        ['Computer',10, 30],
        ['Fork',5, 1],
        ['Problem Set', 0, -10]]

def knapsack(items, max_w):
    for item in items:
        if item[1] != 0:
            item.append(item[2]/item[1])
        else:
            item.append(0)
    
    items = sorted(items, reverse=True, key=lambda item: item[3])
    packed=[' ', 0, 0, 0]
    for item in items:
        if item[2] > 0:
            if (item[1] + packed[1]) <= max_w:
                packed[0] += ', '+ item[0]
                packed[1] += item[1]
                packed[2] += item[2]
    packed[0] = packed[0].lstrip(' ,')
    print(f'The best items to pack are {packed[0]} with total weight of {packed[1]} and value of {packed[2]}')   

knapsack(items, 14)