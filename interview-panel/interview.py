import os
import csv
import adjacencylist as G
import edges as E
import copy

final_stack=[]
def find_key(graph,maxx):
    start=1
    end=maxx
    global final_stack
    while(start<=end):
        mid=int((start+end)/2)
        stack=chaitin_algo(copy.deepcopy(graph),mid)
        if(len(stack)==0):
            start=mid+1
        else:
            end=mid-1
            ans=mid
            final_stack=stack
    return ans

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

def slot_allotment(slots,graph):
    colour_dict={}
    keys_list = list(graph)
    for s in keys_list:
        colour_dict[s]=0
    while(len(final_stack)>0):
        key=final_stack.pop();
        for count in range(1,slots+1):
            temp=0
            for val in graph[key]:
                if(colour_dict[val]==count):
                    temp=1
                    break
            if(temp==0):
                colour_dict[key]=count
                break
    return colour_dict


def make_panel_graph(contents):
    fileName = "data/output/panel/review-panels1.csv"
    if (not os.path.isfile(fileName)):
        print(fileName + ": file does not exist.")
    data = open(fileName, "r")
    csvData = csv.reader(data)
    graph = G.empty_graph()
    for row in csvData:
        contents[row[0]] = []
        for i in range(len(row)):
            if(i == 0):
                continue
            else:
                contents[row[0]].append(row[i])
    # print(contents)
    for f in contents.keys():
        for c in contents.keys():
            G.add_edge(E.make_edge(f, 0, c), graph)
    keys = list(contents.keys())
    for i in range(len(contents)):
        for j in range(len(contents)):
            if(any(val in contents[keys[i]] for val in contents[keys[j]])):
                if(keys[i]!=keys[j]):
                    G.add_edge(E.make_edge(keys[i], 1, keys[j]), graph)
    
    # write_mci(graph)


    # edge_pair = []
    # for s in graph:
    #     for (d, w) in graph[s]:
    #         if(w != 0):
    #             edge_pair.append((s,d))
    # print(edge_pair)

    graph_dict = {}
    for s in graph:
        graph_dict[s] = []
        for (d, w) in graph[s]:
            if(w != 0):
                graph_dict[s].append(d)
    return graph_dict





def write_mci(g):
  dim = G.number_of_nodes(g)
  # print ("mclheader\nmcltype matrix\ndimensions " + str(dim) + "x" + str(dim) + "\nmclmatrix\nbegin")
  for s in g:
    line = str(s)
    for (d, w) in g[s]:
      if(w != 0):
        line += " " + str(d) + ":" + str(w)
    line += "\t$"
    # print (line)

# def print_review_panels():
#   fout = open("data/output/interview-slots/panel-slots.txt", "w")
#   count=0
#   for app in review_panels:
#     fout.write("\n***************************************************")
#     count+=1
#     fout.write("\nInterview-panel : "+str(count))
#     fout.write("\n" + app)
#     panel = functools.reduce(lambda x, y: x + "\n\t" + y[0], review_panels[app][:PANEL_SIZE], "\n")
#     fout.write(panel)
#     fout.write("\n***************************************************")
#   fout.close()


if __name__ == "__main__":

    contents={}
    graph_dict=make_panel_graph(contents)
    slots=find_key(graph_dict,len(graph_dict))
    # print(final_stack)
    print("\n\nMinimum number of slots for this graph are: "+str(slots))

    colour_slots=slot_allotment(slots,graph_dict)
    print("\nSlots alloted to each Interview-Panel:\n")
    k=0
    for i in colour_slots:
        k+=1
        print("\nInterview-Panel: "+str(k)+" || candidate id: "+str(i)+" || prof id: "+ str(contents[i])+" \n------->>Slot: "+str(colour_slots[i]))

