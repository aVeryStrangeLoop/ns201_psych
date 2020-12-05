import matplotlib.pyplot as plt
import sys
import numpy as np


def generate(slope,noise_y_sd,path):
    x_points = np.arange(0.0,2.0,0.025)
    y_points = slope*x_points
    y_noise = np.random.normal(0.0,noise_y_sd,80)
    y_points = y_points+y_noise

    plt.scatter(x_points,y_points,marker=".")
    plt.axis('equal')
    plt.xlim(-0.1,2.1)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    #plt.gca().axis("off")
    #plt.axhline(y=np.mean(y_points),color="black",linewidth=.5)
    plt.savefig(path)
    plt.close()

if __name__=="__main__":
    slope = float(sys.argv[1])
    noise_y_sd = float(sys.argv[2])
    path = sys.argv[3]

    generate(slope,noise_y_sd,path)

