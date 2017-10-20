#!/usr/bin/python
import csv

class node:
    def __init__(self, w, x, y):
        self.value = w
        self.x_pos = x
        self.y_pos = y
        self.dist = -99999999
        self.visited = False


test = open("input.txt", "r")
n = int(test.read(2))

table = []
reader = csv.reader(test, delimiter=",")
i = 0
for row in reader:
    line = []
    for j in range(n):
        new_node = node(int(row[j]), j, i)
        line.append(new_node)
    table.append(line)
    i+=1

