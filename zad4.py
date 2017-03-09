__author__ = 'student'
import matplotlib.pyplot as plt
import networkx as nx
s=str()
flag=bool
d={}
a={}
file_input=open('/home/student/фруктогорода.txt','r')
s=file_input.readlines()
for k in range(len(s)):
        if len(s[k].split())==3:
          d[s[k].split()[0]]={s[k].split()[1]:s[k].split()[2]}
G = nx.Graph(d)
dd = nx.to_dict_of_dicts(G)
K=nx.number_connected_components(G)
S=nx.is_connected(G)
p=nx.shortest_path_length(G,source='Мандариновый')
z=nx.shortest_path(G,source='Сливовый',target='Мандариновый')
for x in d:
    if x in z or d[x].keys() in z:
        a[x]=d[x]
A=nx.Graph(a)
nx.draw_circular(A)
plt.show()