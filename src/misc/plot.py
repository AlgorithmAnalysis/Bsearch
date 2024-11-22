import matplotlib.pyplot as plt
import numpy as np

# just for plotting times
algorithms = ['Binary Search', 'Interpolation Search', 'Exponential Search']
distributions = ['Uniform', 'Skewed', 'NonUniform']
data = {
    'Binary Search': [32620, 22176, 19866],
    'Interpolation Search': [10053, 286953, 58811],
    'Exponential Search': [34574, 25716, 30167],
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
