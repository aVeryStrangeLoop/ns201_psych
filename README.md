# ns201_psych
@Bhaskar Kumawat

Scripts to generate data for NS201 psychometry curve experiment.

- `generate_plot.py`: takes line slope, standard deviation of gaussian noise, and output file path to generate a graph containing data points. The main driver function `generate` can be imported to another python script in order to be used directly.

Syntax: `python3 generate_plot.py <line_slope:float> <gaussian noise standard deviation:float> <path to output:string>`

- `generate_set.py`: Generates an entire set of data containing graphs generated with different values of slope and noise. All these images are generated in a directory called "dataset" in the current folder. It also generates a file called setdesc.csv containing information each of the images in the dataset folder. 

Syntax: `python3 generate_set.py`

All the parameters are given as variables in the script

`slopes`: List of slopes from which to generate data.
`noises`: List of gaussian noise standard deviations.
`repls` : Number of replicates of each type. There are two types of replicates - positive and negative. For each value of slope and noise, 2\*repls graphs are generated. Half of these have positive slope and half have negative slope.

`ctrl_slopes`: Slopes for the control graphs
`ctrl_noises`: Noises for the cotrol graphs
`ctrl_repls`: Number of control replicates. Actual number of graphs for each slope and noise is 2\*ctrl\_repls - with half positive and half negative.

For particular values of these parameters, the total size of the dataset can be calculated as.  
`n(slopes)*n(noises)*n(repls)*2+n(ctrl_slopes)*n(ctrl_noises)*n(ctrl_repls)*2`

- `bulk_analyse.py`: Takes a folder containing .csv files obtained from PsychoPy experiments and calculates the accuracies for different slopes and noise values for each participant. This creates two files in a folder called "analysis" - 'accuracies.csv' containing accuracies for different slope and noise values for each participant (aggregates images together), and 'per\_image.csv' containing the responses for each participant for each image.

Syntax: `python3 bulk_analyse.py <folder path containing response data:string>`

- `plot_accuracies.r`: Takes the accuracies.csv file and generates a plot of the accuracy for different values of slopes and noises.
Requires R

Syntax: `RScript plot_accuracies.r <path to accuracies.csv:string>`
