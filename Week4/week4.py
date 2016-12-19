import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load the data
with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

neuron1  = data['neuron1']
neuron2  = data['neuron2']
neuron3  = data['neuron3']
neuron4  = data['neuron4']
stimulus = data['stim']

# Debug
print ("Matrices:", data.keys())
print ("Stimulus Vector:", data['stim'])
print("Neuron Matrix Lengths: \n\tCols:", len(neuron1), " Rows:", len(neuron1[0]))
print("Stimulus Length: ", len(stimulus))

# For each of the neurons plot the tuning curve
#   - The mean firing rate of the neuron as a function of the stimulus
experiment_sums = np.zeros(len(stimulus))
for col in neuron1:
    for stim_idx, a_rate in enumerate(col):
        experiment_sums[stim_idx] += a_rate

experiment_means = experiment_sums / len(neuron1)

plt.subplot(221)
plt.plot(stimulus, experiment_means)
plt.title('Neuron 1')

experiment_sums = np.zeros(len(stimulus))
for col in neuron2:
    for stim_idx, a_rate in enumerate(col):
        experiment_sums[stim_idx] += a_rate

experiment_means = experiment_sums / len(neuron2)

plt.subplot(222)
plt.plot(stimulus, experiment_means)
plt.title('Neuron 2')

experiment_sums = np.zeros(len(stimulus))
for col in neuron3:
    for stim_idx, a_rate in enumerate(col):
        experiment_sums[stim_idx] += a_rate

experiment_means = experiment_sums / len(neuron3)

plt.subplot(223)
plt.plot(stimulus, experiment_means)
plt.title('Neuron 3')

experiment_sums = np.zeros(len(stimulus))
for col in neuron4:
    for stim_idx, a_rate in enumerate(col):
        experiment_sums[stim_idx] += a_rate

experiment_means = experiment_sums / len(neuron4)

plt.subplot(224)
plt.plot(stimulus, experiment_means)
plt.title('Neuron 4')
plt.show()