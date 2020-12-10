import os
import glob
import sys

folder = sys.argv[1]

if not os.path.exists("analysis"):
        os.makedirs("analysis")

ofile1 = open("analysis/per_image.csv","w+")
ofile1.write("exp_code,img_label,slope,noise,correct\n")

slopes = []
noises = []


for fname in glob.glob(folder+"/*.csv"):
    exp_code = fname.split("/")[-1].split(".")[0]
    with open(fname) as ifile:
        header = next(ifile) # Skip first two lines
        header_words = header.split(",")
        is_control_col = header_words.index("is_control") 
        img_path_col = header_words.index("path")
        slope_col = header_words.index("slope")
        noise_col = header_words.index("noise")
        corrans_col = header_words.index("corrans")
        resp_col = header_words.index("key_resp.keys")
        for line in ifile:
            words = line.split(",")
            if words[is_control_col] == "false":
                img_label = int(words[img_path_col].split("/")[-1].split(".")[0])
                slope = float(words[slope_col])
                if not abs(slope) in slopes:
                    slopes.append(abs(slope)) 
                noise = float(words[noise_col])
                if not noise in noises:
                    noises.append(noise)
                correct = 1 if words[corrans_col]==words[resp_col] else 0
                ofile1.write("%s,%d,%f,%f,%d\n" % (exp_code,img_label,slope,noise,correct))

ofile1.close()

ofile2 = open("analysis/accuracies.csv","w+")
ofile2.write("exp_code,abs_slope,noise,num_correct,num_total,accuracy\n")

for fname in glob.glob(folder+"/*.csv"):
    exp_code = fname.split("/")[-1].split(".")[0]
    for slope in slopes:
        for noise in noises:
            num_correct = 0
            num_total = 0
            with open(fname) as ifile:
                header = next(ifile) # Skip first two lines
                header_words = header.split(",")
                is_control_col = header_words.index("is_control") 
                img_path_col = header_words.index("path")
                slope_col = header_words.index("slope")
                noise_col = header_words.index("noise")
                corrans_col = header_words.index("corrans")
                resp_col = header_words.index("key_resp.keys")
                for line in ifile:
                    words = line.split(",")
                    if words[is_control_col] == "false" and abs(float(words[slope_col]))==slope and float(words[noise_col])==noise :
                        is_correct = 1 if words[corrans_col]==words[resp_col] else 0
                        num_correct += is_correct
                        num_total += 1

            ofile2.write("%s,%f,%f,%d,%d,%f\n" % (exp_code,slope,noise,num_correct,num_total,(float(num_correct)/float(num_total)*100.)))

ofile2.close()
