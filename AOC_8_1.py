# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:49:18 2023

@author: Varun
"""

data = """AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

navigate = list("RL")
rules = {line.split(' = ')[0]: tuple(map(str.strip, line.split('=')[1].replace("(", "").replace(")", "").split(','))) for line in data.split('\n')}
count = 0
key = "AAA"

def nextNode(key):
    global count
    v =  rules.get(key)
    path = navigate.pop(0)
    print(key + str(rules.get(key)) + " path : " + path)
    navigate.append(path)
    nextKey = v[1 if path == "R" else 0]
    return nextKey;

while key != "ZZZ":
    key = nextNode(key)
    count += 1
print(count)
    
    
