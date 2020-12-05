# ns201_psych
@Bhaskar Kumawat

Scripts to generate data for NS201 psychometry curve experiment.

`generate_plot.py`: takes line slope, standard deviation of gaussian noise, and output file path to generate a graph containing data points. The main driver function `generate` can be imported to another python script in order to be used directly.

Syntax: `python3 generate_plot.py <line_slope:float> <gaussian noise standard deviation:float> <path to output:string>`

`generate_set.py`: Generates an entire set of data containing graphs generated with different values of slope and noise.

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
