# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:31:40 2023

@author: Amalu Vincent
"""

import numpy as np
import matplotlib.pyplot as plt

# Read data from file and store in array
data = np.loadtxt('data4.csv')
fig = plt.figure(figsize=(8,5))
# Create histogram of newborn weights
n, bins, patches = plt.hist(data, bins=20,color='coral', edgecolor='white',alpha=0.7)
# Calculate average weight
W_mean = np.mean(data)
# Calculate fraction of babies born with weight between 0.9W and 1.1W
W_09 = 0.9 * W_mean
W_11 = 1.1 * W_mean
n_09_11 = sum((W_09 <= data) & (data <= W_11)) / len(data)

# Plot X and W values on histogram
plt.axvline(x=W_mean, color='black',linestyle='--', label='Average weight')
plt.axvspan(W_09, W_11, alpha=0.3, color='g', label='0.9W to 1.1W')
plt.legend()
plt.xlabel('Newborn weight (kg)',fontweight='bold')
plt.ylabel('Frequency', fontweight='bold')
plt.title('Distribution Of Newborn Weights',  fontweight='bold')


# Print values on graph
plt.text(0.05, 0.9, f'Average weight(W~)= {W_mean:.2f} kg\n', 
         transform=plt.gca().transAxes)
plt.text(0.05, 0.8, f'Fraction of babies  between \n 0.9W and 1.1W (X)={n_09_11:.2%}',
         transform=plt.gca().transAxes)
plt.savefig('histogram.png')
plt.show()
