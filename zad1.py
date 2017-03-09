__author__ = 'student'
import matplotlib.pyplot as plt
import networkx as nx
s=str()
flag=bool
d={}
file_input=open('/home/student/фруктогорода.txt','r')
s=file_input.readlines()
for k in range(len(s)):
        if len(s[k].split())==3:
          d[s[k].split()[0]]={s[k].split()[1]:s[k].split()[2]}
print(d)
G = nx.Graph(d)
dd = nx.to_dict_of_dicts(G)
nx.draw_circular(G)
plt.show()