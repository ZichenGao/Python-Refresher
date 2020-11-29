
import numpy as np
import matplotlib.pyplot as plt

def plotsc():
    x=np.linspace(-np.pi,np.pi,1024)
    s=np.sin(x)
    c=np.cos(x)
    plt.plot(x,s)
    plt.plot(x,c)
    plt.show()

if __name__ == "__main__":
    plotsc()