# import modules 
from matplotlib_venn import venn2 
from matplotlib_venn import venn3 
from matplotlib import pyplot as plt 
import pylab as plt
from matplotlib_venn import venn3, venn3_circles

# dict_key = {
#         "Union" :"U",
#         "Intersection" : "∩",
#         "Complement" : "c",
#         "-" : "minus",
#         "Minus" : "minus",

# }

# # set_A = {10, 20, 30}
# # set_B = []

# set1 = set(['A', 'B', 'C', 'D'])
# set2 = set(['B', 'C', 'D', 'E'])
# set3 = set(['C', 'D',' E', 'F', 'G'])

# # venn3([set1, set2, set3], ('Set1', 'Set2', 'Set3'))
# # 



# v = venn3(subsets=(1,1,0,1,0,0,0))
# v.get_label_by_id('100').set_text('First')
# v.get_label_by_id('010').set_text('Second')
# v.get_label_by_id('001').set_text('Third')
# plt.title("Not a Venn diagram")
# plt.show()




# # # depict venn diagram 
# # venn2(subsets = (10, 15, 30), set_labels = ('Group A', 'Group B'), set_colors = (("orange", "blue"))) 
# plt.show()

# # client_input = input()

import numpy as np
from matplotlib_venn import venn3

def venn_diagram(a, b, c, labels=['A', 'B', 'C']):

    a = set(a)
    b = set(b)
    c = set(c)

    only_a = len(a - b - c)
    only_b = len(b - a - c)
    only_c = len(c - a - b)

    only_a_b = len(a & b - c)
    only_a_c = len(a & c - b)
    only_b_c = len(b & c - a)

    a_b_c = len(a & b & c)

    venn3(subsets=(only_a, only_b, only_a_b, only_c, only_a_c, only_b_c, a_b_c), set_labels=labels)

a, b, c = np.round(np.random.rand(3, 50000), 5)
venn_diagram(a, b, c)

plt.show()