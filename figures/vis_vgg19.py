#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:50:22 2019

@author: avneesh
"""

import matplotlib.pyplot as plt
import numpy as np

        
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
        
colors=['darkorange', 'crimson', 'darkseagreen', 'navy', 'wheat', 'gray', 'palevioletred', 'gold', 'lightcoral', 'forestgreen', 'cornflowerblue']

participants = ['p{:02}'.format(index) for index in range(15)]
print(participants)

#            0     1     2*     3*    4**   5     6     7*      8     9*   10*   11**    12   13     14
values = [  4.35, 4.66, 5.55, 5.95, 7.42, 6.023, 5.56, 6.74,  6.17, 6.85, 5.44, 6.39, 5.43, 6.12, 6.21 ]

v_cyclic = [4.25, 4.94, 5.54, 5.47, 6.93, 6.25, 5.88,  6.57,  6.44, 7.13, 5.33, 6.33, 5.7, 6.18, 6.17 ]

v_rlrop = [ 4.70, 4.25, 5.69, 5.30, 7.12, 6.28, 5.46,  6.56,  5.98, 6.55, 5.83, 6.50, 5.30, 6.0, 6.0 ]

v_rlrop1 = [4.53, 4.39, 5.50, 5.33, 7.62, 6.02, 5.36,  6.69,  6.08, 6.84, 5.44, 6.46, 5.51, 6.03, 6.01 ]

v_resnet = [3.98, 5.21, 5.89, 6.00, 7.39, 6.19, 5.56,  6.63,  6.12,  6.95, 6.45, 5.48,  5.62, 6.24, 5.89 ]
## issues with 11 major, 2 
### ae 7.4 for p04 is worse than ae for b-32 which was 6.9
print(values,'\n', v_cyclic, '\n', v_rlrop, '\n', v_rlrop1)
x = np.arange(len(participants))  # the label locations

width = 0.35  # the width of the bars
figg, ax = plt.subplots(figsize=(9,5))
fig = ax.bar(participants, v_resnet, color=colors)
ax.set_ylabel("Angle Error (deg)")
ax.set_xlabel("Subject Ids")
ax.set_title("VGG19 \n Using ReduceLROPlateau \n Mean Angle Error = {}".format(np.mean(v_resnet)))
ax.set_xticks(x)
ax.set_xticklabels(participants)


#plt.title("vgg19 \n using cyclic_lr \n Mean Angle Error = {}".format(np.mean(v_cyclic)))
#plt.bar(participants, v_cyclic) 
#plt.bar(participants, values)

figg.tight_layout()
#figg.subplots_adjust(wspace=20)
autolabel(fig)
plt.show()