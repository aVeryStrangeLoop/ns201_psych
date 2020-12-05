import os
from generate_plot import *

# Remove previous dataset directory
if os.path.exists('dataset'):
    os.rmdir('dataset')

# create new dataset directory
if not os.path.exists('dataset'):
        os.makedirs('dataset')

# create file
ofile = open("dataset/setdesc.csv","w+")
ofile.write("path,is_control,slope,noise,corrans\n")

## Tests
slopes = [0.01,0.05,0.1]
noises = [0.00,0.025,0.05,0.075,0.1,0.125,0.150,0.175,0.200,0.225,0.250,0.275,0.300]
repls = 2 # n positive, n negative

label_cnt = 0

for slope in slopes:
    for noise in noises:
        for repl_type in [-1.0,1.0]:
            for repl in range(repls):
                generate(repl_type*slope,noise,"dataset/"+str(label_cnt)+".png")
                corrans = "up" if repl_type>0.0 else "down"
                ofile.write("dataset/%d.png,false,%f,%f,%s\n" % (label_cnt,repl_type*slope,noise,corrans))
                label_cnt += 1
            


## Controls
## 6x controls
# 1. zero slope with no noise
# 2. zero slope with 0.300 noise
# 3. 0.5 slope with no noise
# 3. 0.5 slope with 0.300 noise
ctrl_slopes = [0.0,0.5]
ctrl_noises = [0.0,0.30]
ctrl_repls = 2

for slope in ctrl_slopes:
    for noise in ctrl_noises:
        for repl_type in [-1.0,1.0]:
            for repl in range(ctrl_repls):
                generate(repl_type*slope,noise,"dataset/"+str(label_cnt)+".png")
                corrans = "up" if repl_type>0.0 else "down"
                corrans = "none" if slope==0.0 else corrans
                ofile.write("dataset/%d.png,true,%f,%f,%s\n" % (label_cnt,repl_type*slope,noise,corrans))
                label_cnt += 1



