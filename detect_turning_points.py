import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    #signal= np.array(signal)
    
    diff = np.zeros(len (signal) - 1)
    for i in range(len(diff)):
        diff[i] = signal[i + 1] - signal[i]
        
        
    signs = np.zeros(len(diff))
    for i in range(len(diff)):
        if diff[i] > 0:
            signs[i] = 1
        elif diff[i] < 0:
            signs[i] = -1
        else:
            signs[i] = 0
            
    turning_indices = []
    for i in range(1, len(signs)):
        if signs[i] != 0 and signs[i-1] != 0 and signs[i] != signs[i-1]:
            turning_indices.append(i)
            
    turning_indices = np.array(turning_indices)
    
    
    plt.plot(signal, label = "Signal")
    plt.scatter(turning_indices, signal[turning_indices], marker = '*', label = "turning points")
    plt.title ('Turning Points in Signal')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.savefig(filename)
    plt.show()
    
    return turning_indices

signal = np.array([1,2,3,8,6,5,4])
turning_indices = detect_turning_points(signal)
print(turning_indices)
    
