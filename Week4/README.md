# Poisson Neuron Models and Population Coding
For each of the neurons, we want to see the mean firing rate of the neuron as a function of the stimulus or the tuning curve
![Alt text](https://raw.githubusercontent.com/abaybektursun/Comp_Neuroscience_UoW/master/Week4/imgs/tuning_curves.png)

> Three of the neurons are Poisson neurons (they are accurately modeling using a Poisson process), but we believe that the remaining one might not be.

To see whether Neuron follows Poisson distribution, we plot time bin avergae spikes against skpike variance in those time bins. If the distribution is Poisson, the plot slope will be constant fano factor, so it's expected to equal 1
![Alt text](https://raw.githubusercontent.com/abaybektursun/Comp_Neuroscience_UoW/master/Week4/imgs/poisson.png)
![Alt text](https://raw.githubusercontent.com/abaybektursun/Comp_Neuroscience_UoW/master/Week4/imgs/hist.png)
