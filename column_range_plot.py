import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    no_colums = A.shape[1]
    
    ranges = np.zeros(no_colums)
    for i in range(no_colums):
        ranges[i] = A[:, i].max() - A[:, i].min()
        
    plt.bar(np.arange(no_colums), ranges)
    plt.xlabel('Index')
    plt.ylabel('Range')
    plt.title('Column Ranges')
    plt.savefig(filename)
    plt.show()
    
    return ranges

A = np.array([[6, 4, 3],
              [5, 7, 1],
              [1, 0, 6]])

ranges = column_range_plot(A)
print(ranges)

