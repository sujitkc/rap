import interview as I

def greedy(graph_dict):
    color_dict = {s:0 for s in graph_dict.keys()}
    keys = list(graph_dict.keys())
    for i in keys:
        for j in keys:
            if i in graph_dict[j] and j in graph_dict[i] and color_dict[i] == color_dict[j]:
                k = color_dict[j] + 1
                for l in keys:
                    if color_dict[l] == k and l in graph_dict[j]:
                        k += 1
                color_dict[j] = k
    return color_dict        

if __name__ == "__main__":
    contents={}
    graph_dict = I.make_panel_graph(contents)

    print(greedy(graph_dict))
    # graph_dict is { 'candidate1@gmail.com': ['candidate3@gmail.com'], 
    #   'candidate2@gmail.com': [], 
    #   'candidate3@gmail.com': ['candidate1@gmail.com']}

    # slots, final_stack=find_key(graph_dict,len(graph_dict))

    # colour_slots=slot_allotment(slots,graph_dict, final_stack)
    # print("\nSlots alloted to each Interview-Panel:\n")

    # print_interview_slots(colour_slots, contents)

    # print("\n\nMinimum number of slots for this dataset: "+str(slots))
    