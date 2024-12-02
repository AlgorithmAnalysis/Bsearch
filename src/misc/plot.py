import matplotlib.pyplot as plt
import numpy as np

# just for plotting times
algorithms = ['Binary Search', 'Interpolation Search', 'Exponential Search']
distributions = ['Uniform', 'Skewed', 'NonUniform']
data = {
    'Binary Search': [7524, 9060, 9774],
    'Interpolation Search': [1832, 157157, 40404],
    'Exponential Search': [15922, 13748, 13457],
}

x = np.arange(len(distributions))
width = 0.25 

fig, ax = plt.subplots(figsize=(10, 6))

offset = -width
for algorithm, times in data.items():
    ax.bar(x + offset, times, width, label=algorithm)
    offset += width

ax.set_xlabel('Data Distributions')
ax.set_ylabel('Execution Time (ns)')
ax.set_title('Search Algorithms Execution Time by Data Distribution')
ax.set_xticks(x)
ax.set_xticklabels(distributions)
ax.legend()

ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
