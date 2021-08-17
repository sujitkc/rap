
import networkx as nx
import interview as I

def encode(graph_dict):
    lookup_dict={}
    output_dict={}
    num = 0
    for i in graph_dict.keys():
      lookup_dict[i] = num
      num += 1
      
    for keys,values in graph_dict.items():
      output_dict[lookup_dict[keys]] = []
      if values is []:
        output_dict[lookup_dict[keys]].append([])
      else:
        for i in values:
          output_dict[lookup_dict[keys]].append(lookup_dict[i])
    # print(lookup_dict)
    # print(output_dict)
    return lookup_dict, output_dict

# encode({"shrey": ["shreyas", "samaksh"],
#           "shreyas": ["sujit"],
#           "sujit": ["samaeksh"],
#           "samaksh": []})

if __name__ == "__main__":
  contents={}
  graph_dict = I.make_panel_graph(contents)
  lookup_dict, output_dict = encode(graph_dict)

  graph = nx.from_dict_of_lists(output_dict)
        