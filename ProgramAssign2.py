import numpy as np

list = [10,25,50,15,5]

min = min(list)
max = max(list)
mean = np.mean(list)
std = np.std(list)
var = np.var(list)

print("Min:", min, "Max:", max, "Mean:", mean, "Standard deviation:", std, "Variance:", var)