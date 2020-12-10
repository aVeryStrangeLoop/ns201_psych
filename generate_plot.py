import matplotlib.pyplot as plt
import sys
import numpy as np
from sklearn.linear_model import LinearRegression


def generate(slope, noise_sd, path):
    threshold = 0.00001

    # Generate a slope 0 line with y noise 
    x_points = np.arange(0.0,2.0,0.01)
    x_ = x_points.reshape((-1,1))

    y_noise = np.random.normal(0.0,noise_sd,200) 
    model = LinearRegression().fit(x_,y_noise)
    
    while abs(model.coef_)>threshold:
        y_noise = np.random.normal(0.0,noise_sd,200) 
        model = LinearRegression().fit(x_,y_noise)

    print(model.coef_)
        
    plt.scatter(x_points,x_points*slope+y_noise,marker=".")
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

