#!/usr/bin/python

import random
import adjacencylist as G
import edges as E

faculty = [
  "Prof. Jyotsna Bapat",
  "Prof. Debabrata Das",
  "Prof. K V Dinesha",
  "Dr. Jaya Sreevalsan Nair",
  "Prof. V N Muralidhara",
  "Prof. Srinath R Naidu",
  "Prof. Balaji Parthasarathy",
  "Prof. G N Srinivasa Prasanna",
  "Prof. S Rajagopalan",
  "Prof. Chandrashekar Ramanathan",
  "Prof. Shrisha Rao",
  "Prof. S Sadagopan",
  "Prof. Srinath Srinivasa",
  "Dr. Meenakshi D'Souza",
  "Prof. Neelam Sinha",
  "Prof. Madhav Rao",
  "Prof. JayPrakash T Lal Chandani",
  "Prof. Manisha Kulkarni ",
  "Prof. G Srinivasaraghavan",
  "Prof. Balakrishnan Ashok",
  "Prof. Amit Prakash",
  "Prof. Sujit Kumar Chakrabarti",
  "Prof. Chetan Parikh",
  "Prof. Shiva Kumar Malapak",
  "Prof. Subir Kumar Roy",
  "Prof. Bidisha Chaudhuri",
  "Prof. Dinesh Babu Jayagopi",
  "Prof. Brijesh Kumar Mishra",
  "Prof. Subajit Sen",
  "Prof. Tricha Anjali",
  "Prof. Srikanth T K",
  "Prof. V Sridhar",
  "Prof. Ashish Choudhury",
  "Prof. Janaki Srinivasan",
  "Prof. Amit Chattopadhyay",
  "Prof. Sachit Rao",
]

topics = [
  "ICT for Development",
  "Chemistry: Structure & Energetics of van der Waals Complexes",
  "Computer Architecture",
  "Computational Topology",
  "Mixed-Signal Circuit Design in particular high speed & resolution ADCs",
  "Natural Language Processing",
  "Software Defined Networking",
  "Microprocessor design",
  "Physics: Physics including Complex Fluids",
  "Chemistry: Computational Chemistry",
  "Model Checking",
  "Physics: Complex Systems and Soft Matter",
  "Innovation Systems in the ICT Industry",
  "Biometrics and Digital Identities in Governance",
  "Governance Analytics and Toolkits",
  "Public Information Infrastructure",
  "Computational Sustainability",
  "Internet of Things",
  "Computational Geometry",
  "Social Media",
  "Verification and Validation",
  "ICT and Work Practices in Organizations",
  "Cryptography",
  "Assistive Wearable Medical Devices",
  "Software Architecture",
  "Political Economy of Information",
  "Microprocessor Design",
  "Open Development",
  "Theorem Proving",
  "Requirement Engineering",
  "Gender and ICTs",
  "Mathematics: Number Theory",
  "ICT and Health (specifically related to aspects concerning household data",
  "e-Governance",
  "Automated Assessment",
  "Visual Analytics of Geospatial Data",
  "Computational Biology",
  "Physics: Dynamical Systems Theory",
  "Services Computing",
  "Chemistry: Electronic Structure Calculations",
  "Model Based Hardware-Software Co-Synthesis of Embedded Systems",
  "Feedback Control Systems",
  "Geometric Computation",
  "Communication for IoT",
  "Galois Module Structure and Elliptic Curves",
  "Optimisation",
  "Algorithms",
  "community/frontline workers and the public health system",
  "Program Analysis",
  "Diophantine Equations",
  "Physics: studies of Instabilities & Synchronization in Nonlinear Systems (both physical",
  "Physics: Cavitation & Bubble Dynamics",
  "Robotics",
  "Physics: 3D Simulations and Modeling of Hydrodynamic and Magnetohydrodynamic Turbulent Flows (involving research in fundamental physics/astrophysics/mechanical engineering)",
  "Computational Modelling",
  "Geometric Algorithms",
  "Network Optimization",
  "Speech processing",
  "Intelligent Transportation Systems",
  "Discrete Geometry",
  "Security and Privacy for IoT",
  "Topological Data Analysis and Visualisation",
  "Software Testing",
  "Algebraic Number Theory",
  "Artificial Intelligence"
]

F = [
    "GSR",
    "SKC",
    "MD",
    "RC",
    "SS",
    "JN",
    "SR"
  ]

T = [
    "Machine learning",            # 0
    "Data analytics",              # 1
    "Software engineering",        # 2
    "Formal methods",              # 3
    "Software testing",            # 4
    "Software verification",       # 5

    "Requirement analysis",        # 6
    "Education technology",        # 7
    "Model checking",              # 8
    "Data modelling",              # 9
    "Web science",                 # 10
    "Social network analysis",     # 11
    "Computer graphics",           # 12

    "Visualisation",               # 13
    "Formal verification",         # 14
    "VLSI",                        # 15
    "Hardware software co-design", # 16
    "Software architecture",       # 17
    "Reverse engineering"          # 18
  ]

def read_faculty_topic_map():
  FT1 = {
    0 : [0, 1],
    1 : [2, 3, 4, 5, 6, 7, 18],
    2  : [2, 3, 4, 5, 6, 17],
    3  : [1, 9, 7],
    4  : [10, 11],
    5  : [12, 13],
    6  : [14, 3, 15, 16]
  }
  FT2 = {
    0 : [0, 1, 5],
    1 : [2, 3, 4],

    2  : [8, 6, 11, 12],
    3  : [10, 11, 6, 9],

    4  : [13, 14],
    5  : [16, 13],
    6  : [14, 13, 17, 18]
  }

  return FT2

def read_candidate_topic_map():
  CT1 = {
    7: [0, 4, 5],
    8: [1, 5, 3],
    9: [5, 1, 0, 2, 3],

    10: [9, 11, 10],
    11: [6, 10, 7],
    12: [9, 8, 12],

    13: [15, 13, 16],
    14: [16, 13, 14, 18],
    15: [15, 17],
    16: [16, 15, 14, 17, 18]
  }
  CT2 = {
    7 :  [2, 3, 4, 5, 6, 7, 18],
    8 : [2, 3, 4, 5, 6, 7, 18],
    9 : [2, 3, 4, 5, 6, 17],
    10 : [2, 3, 4, 5, 6, 17],
    11 : [10, 11],
    12 : [10, 11],
    13 : [14, 3, 15, 16],
    14 :  [14, 3, 15, 16],
    15 : [15, 8],
    16 : [16, 19, 1, 0, 14, 7, 10]
  }

  return CT1
'''
  numOfCandidates = int(len(F) * 1.5)
  CT = {}
  for i in range(numOfCandidates):
    CT[i] = []
    n = random.randint(3, 8)
    for j in range(n):
      next_topic = random.randint(0, len(T))
      if(not next_topic in CT[i]):
        CT[i].append(next_topic)
  return CT
'''
 

def build_graph(FT, CT):
  FC = G.empty_graph()

  for f in FT.keys():
    for c in CT.keys():
      G.add_edge(E.make_edge(f, 0, c), FC)

  edges = G.get_edges(FC)

  F = list(FT.keys())
  C = list(CT.keys())
  for f in F:
    for t in FT[f]:
      for c in C:
        if t in CT[c]:
          G.add_edge(E.make_edge(f, 1, c), FC)

  for i in range(len(F)):
    f1 = F[i]
    for t in FT[f1]:
      for j in range(i + 1, len(F)):
        f2 = F[j]
        if t in FT[f2]:
          G.add_edge(E.make_edge(f1, 1, f2), FC)

  for i in range(len(C)):
    c1 = C[i]
    for t in CT[c1]:
      for j in range(i + 1, len(C)):
        c2 = C[j]
        if t in CT[c2]:
          G.add_edge(E.make_edge(c1, 1, c2), FC)

  return FC

def write_mci(g):
  dim = G.number_of_nodes(g)
  print ("mclheader\nmcltype matrix\ndimensions " + str(dim) + "x" + str(dim) + "\nmclmatrix\nbegin")
  for s in g:
    line = str(s)
    for (d, w) in g[s]:
      if(w != 0):
        line += " " + str(d) + ":" + str(w)
    line += "\t$"
    print (line)

if __name__ == "__main__":
  FT = read_faculty_topic_map()
  CT = read_candidate_topic_map()
  FC = build_graph(FT, CT)
  write_mci(FC)
#  print FC
