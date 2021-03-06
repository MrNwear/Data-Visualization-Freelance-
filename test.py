# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gzkp0lwwDU5L4JiM42WedUAhDNQPqto1
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
employee = pd.read_csv("test.csv")
tick_label = ['[1 - 1.98]']
height = []
left = []
ranges = [.9999999999,1.98,2.96,3.94,4.92,5.90,6.88,7.86,8.84,9.82,10.8,11.78,12.76,13.74,14.72,15.7,16.68,17.66,18.64,19.62,20.6,21.58,22.56,23.54,24.52,25.5,26.48,27.46,28.44,29.42,30.4,31.38,32.36,33.34,34.32,35.3,36.28,37.26,38.24,39.22,40.2,41.18,42.16,43.14,44.12,45.1,46.08,47.06,48.04,49.02,50]
d=employee.groupby(pd.cut(employee.Weight, ranges,precision=12))
i=0

for name, group in d.Weight:
  if i !=0 :
    tick_label.append(name)
  height.append(group.count())
  left.append(i+1)
  i+=1
plt.bar(left, height, tick_label = tick_label,ec='yellow')
figure = plt.gcf() # get current figure
figure.set_size_inches(80, 60)
plt.savefig("myplot.png", dpi = 100)
plt.xticks(rotation=90)
plt.xlabel('category - axis')
plt.ylabel('weight - axis')
plt.title('weights distrubitions')
plt.show()
