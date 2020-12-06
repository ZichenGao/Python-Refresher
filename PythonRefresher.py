import numpy as np
import matplotlib.pyplot as plt

def main():
    x=np.linspace(0,2*np.pi)

    tan_x = np.linspace(0, 2 * np.pi)
    tan_y = np.tan(x)
    max_index = tan_y.argmax()
    min_idex = tan_y.argmin()

    tan_x[max_index] = np.nan
    tan_x[min_idex] = np.nan
    tan_y[max_index] = np.nan
    tan_y[min_idex] = np.nan

    s=np.sin(x)
    c=np.cos(x)
    plt.plot(x,s)
    plt.plot(x,c)
    plt.plot(tan_x, tan_y, color="red", label="tan")
    plt.ylim(-1, 1)
    plt.show()


if __name__=="__main__":
    main()
