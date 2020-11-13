import os
import csv
import random
import adjacencylist as G
import edges as E
import copy
import numpy



final_stack=[]

def delete_node(Dict,key):
    del Dict[key]
    for s in Dict:
        if key in Dict[s]:
            Dict[s].remove(key)

def chaitin_algo(Dict,k):
    stack=[]
    # print(graph)
    while(len(Dict)>0):
        i=0
        temp=0
        while(i<len(Dict)):
            keys_list = list(Dict)
            if(len(Dict[keys_list[i]])<k):
                stack.append(keys_list[i])
                delete_node(Dict,keys_list[i]) 
                temp=1
            else:
                i+=1

        if(temp==0):
            stack.clear()
            break
    return stack

def make_panel_graph(contents):
    fileName = "data/output/panel/review-panels.csv"
    if (not os.path.isfile(fileName)):
        print(fileName + ": file does not exist.")
    data = open(fileName, "r")
    csvData = csv.reader(data)
    graph = G.empty_graph()
    for row in csvData:
        contents[row[0]] = []
        for i in range(len(row)):
            if (i == 0):
                continue
            else:
                contents[row[0]].append(row[i])
    for f in contents.keys():
        for c in contents.keys():
            G.add_edge(E.make_edge(f, 0, c), graph)
    keys = list(contents.keys())
    for i in range(len(contents)):
        for j in range(len(contents)):
            if (any(val in contents[keys[i]] for val in contents[keys[j]])):
                if (keys[i] != keys[j]):
                    G.add_edge(E.make_edge(keys[i], 1, keys[j]), graph)
    graph_dict = {}
    for s in graph:
        graph_dict[s] = []
        for (d, w) in graph[s]:
            if (w != 0):
                graph_dict[s].append(d)
    return graph_dict


def write_mci(g):
    dim = G.number_of_nodes(g)
    print("mclheader\nmcltype matrix\ndimensions " + str(dim) + "x" + str(dim) + "\nmclmatrix\nbegin")
    for s in g:
        line = str(s)
        for (d, w) in g[s]:
            if (w != 0):
                line += " " + str(d) + ":" + str(w)
        line += "\t$"
        print(line)

# def find_key(graph,maxx):
#     start=1
#     end=maxx
#     ans = maxx
#     global final_stack
#     while(start<=end):
#         mid=int((start+end)/2)
#         stack,child=genetic_algo(copy.deepcopy(graph),mid)
#         if(stack==0):
#             start=mid+1
#         else:
#             end=mid-1
#             ans=mid
#     for i,j in child.items():
#         print("Candidate Email: "+str(i)+" :: Slot: "+str(j))
#     return ans


def find_key(graph,maxx):
    start=1
    end=maxx
    while(start<=end):
        mid=int((start+end)/2)
        stack=chaitin_algo(copy.deepcopy(graph),mid)
        if(len(stack)==0):
            start=mid+1
        else:
            end=mid-1
            ans=mid
    stack1,child =genetic_algo(copy.deepcopy(graph),ans)
    if(child != []):
        for i,j in child.items():
            print("Candidate Email: "+str(i)+" :: Slot: "+str(j))
    return ans

def genetic_algo(graph, color):
    chromosomes = []
    for i in range (200):
        colors = {}
        for i in graph.keys():
            colors[i] = random.randint(0, color - 1)
        chromosomes.append(colors)
    val, child = run(chromosomes, graph, color)
    if val <= color:
        return color ,child
    return 0 , []    

def run(population, graph, color):
    col = [i for i in range(color)]
    count = 0
    while(count < 300):
        parent1, parent2 = parentSelection(population)
        child = crossover(parent1, parent2, graph, population)
   
        child = mutate(child, graph, col)
        fitChild = fitness(child, graph)
        print(fitChild)

        fitP1 = fitness(population[parent1], graph)
        fitP2 = fitness(population[parent2], graph)
        if(len(population)<2):
            return fitChild ,child
        if(fitChild < fitP1 and fitChild < fitP2):
            population.pop(parent1)
            population.pop(parent2 - 1)
            population.append(child)
        elif(fitChild < fitP1):
            population.pop(parent1)
            population.append(child)
        elif(fitChild < fitP2):
            population.pop(parent2)
            population.append(child)
        count = count + 1
    return fitChild ,child

def crossover(parent1, parent2, graph, population):
    crosspoint = random.randint(0, len(population) - 1)
    child = {}
    vals = list(graph.keys())
    vals.sort()
    for i in range(crosspoint):
        child[vals[i]] = population[parent1][vals[i]]
    for i in range(crosspoint, len(vals)):
        child[vals[i]] = population[parent2][vals[i]]
    return child

def parentSelection(population):
    parent1 = random.randint( 0, len(population) - 1)
    parent2 = random.randint(0, len(population) - 1)

    return parent1, parent2

def fitness(chromosome, graph):
    conflict = 0
    for i in chromosome:
        conflict = conflict + fit(i, graph, chromosome[i], chromosome)
    return conflict

def fit(id, graph, col, chromosome):
    conflict = 0
    for val in graph[id]:
        if(col == chromosome[val]):
            conflict = conflict + 1
    return conflict

def mutate(chromosome, graph, colour):
    for i in chromosome:
        check(i, graph, chromosome[i], chromosome, colour)
    return chromosome

def check(id, graph, col, chromosome, colour):
    adjCol = []
    for d in graph[id]:
        adjCol.append(chromosome[d])
    validCol = Diff(colour, adjCol)
    for val in graph[id]:
        if(col == chromosome[val]):
            if(len(validCol)<1):
                break
            chromosome[val] = validCol[0]
            validCol.pop(0)
def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

if __name__ == "__main__":
    contents = {}
    graph_dict = make_panel_graph(contents)
    slots=find_key(graph_dict,len(graph_dict))
    print("\nMinimum number of slots to conduct the interview are:")
    print(slots)


























