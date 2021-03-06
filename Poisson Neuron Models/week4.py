import pickle
import itertools
import numpy as np
from operator import add
import matplotlib.pyplot as plt

# Cartesian coordinates to polar coordinates
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

# Polar coordinates to cartesian coordinates
def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

# Load the data
with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

neuron1  = data['neuron1']
neuron2  = data['neuron2']
neuron3  = data['neuron3']
neuron4  = data['neuron4']
stimulus = data['stim']

num_experiments = len(neuron1)
neurons_r_max   = []

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
neurons_r_max.append(max(experiment_means))

plt.subplot(221)
plt.plot(stimulus, experiment_means)
plt.title('Neuron 1')

experiment_sums = np.zeros(len(stimulus))
for col in neuron2:
    for stim_idx, a_rate in enumerate(col):
        experiment_sums[stim_idx] += a_rate

experiment_means = experiment_sums  / len(neuron2)
neurons_r_max.append(max(experiment_means))

plt.subplot(222)
plt.plot(stimulus, experiment_means)
plt.title('Neuron 2')

experiment_sums = np.zeros(len(stimulus))
for col in neuron3:
    for stim_idx, a_rate in enumerate(col):
        experiment_sums[stim_idx] += a_rate

experiment_means = experiment_sums  / len(neuron3)
neurons_r_max.append(max(experiment_means))

plt.subplot(223)
plt.plot(stimulus, experiment_means)
plt.title('Neuron 3')

experiment_sums = np.zeros(len(stimulus))
for col in neuron4:
    for stim_idx, a_rate in enumerate(col):
        experiment_sums[stim_idx] += a_rate

experiment_means = experiment_sums  / len(neuron4)
neurons_r_max.append(max(experiment_means))

plt.subplot(224)
plt.plot(stimulus, experiment_means)
plt.title('Neuron 4')
plt.show()

# Check if all the neurons follow Poisson distribution
# Variance vs mean rate
# In poisson, slope should be close to 1

for id, a_neuron in enumerate([neuron1, neuron2, neuron3, neuron4]):
    variance = []
    mean_hz  = []
    plt.subplot(220 + id + 1)
    for row in range(len(stimulus)):
        variance.append(np.var(a_neuron[:, row]))
        mean_hz.append(np.mean(a_neuron[:, row])/10)
        plt.plot(variance, mean_hz, 'ro')

    slope, intercept = np.polyfit(variance, mean_hz, 1)
    plt.title('Neuron {0}: {1:.2f} | {2:.2f}'.format(id+1, round(slope, 2), round(intercept, 2)))

plt.show()


for id, a_neuron in enumerate([neuron1, neuron2, neuron3, neuron4]):
    plt.subplot(220 + id + 1)
    for idx in range(len(stimulus)):
        plt.hist(a_neuron[:,idx])
    plt.title('Neuron ' + str(id+1))

plt.show()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Load the data
with open('pop_coding_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

# Debug
print ("Matrices:", data.keys())

# r1, r2, r3, and r4 that contain the responses (firing rate in Hz) of the four neurons
# c1, c2, c3, and c4 are the basis vectors corresponding to neurons

r1 = data['r1']
r2 = data['r2']
r3 = data['r3']
r4 = data['r4']
c1 = data['c1']
c2 = data['c2']
c3 = data['c3']
c4 = data['c4']

print (r1)
print (c1)

print (r2)
print (c2)

# Compute the Population vector

# Sum projections of stimulus onto neuron bases

population_vectors_x = []
population_vectors_y = []
angles               = []
for trial_num in range (len(r1)):
    popSum = [0, 0]
    for neuron_id, a_neuron in enumerate([neuron1, neuron2, neuron3, neuron4]):
        popSum = [sum(vec) for vec in zip(popSum, (data['r'+str(neuron_id+1)][trial_num]/neurons_r_max[neuron_id])*np.array(data['c'+str(neuron_id+1)]))]
        #popSum = [sum(vec) for vec in zip(
        #    popSum,
        #    [x * (data['r'+str(neuron_id+1)][trial_num]/neurons_r_max[neuron_id]) for x in data['c'+str(neuron_id+1)]]
        #)]

    print (popSum)
    population_vectors_x.append(popSum[0])
    population_vectors_y.append(popSum[1])

    angles.append(np.rad2deg(cart2pol(popSum[0],popSum[1])[1]))

print(angles)

print("Mean angle: " + str(np.mean(angles)%360))
print("Mean angle 2: " + str(360 + np.mean(angles)))

print("New Mean angle: " + str(
    np.rad2deg(
        cart2pol(
            np.mean(population_vectors_x),
            np.mean(population_vectors_y)
        )[1]
    )%360)
)

# test
popSum = [0, 0]
for neuron_id, a_neuron in enumerate([neuron1, neuron2, neuron3, neuron4]):
    popSum = [sum(vec) for vec in zip(popSum, (np.mean(data['r' + str(neuron_id + 1)]) / neurons_r_max[neuron_id]) * np.array(data['c' + str(neuron_id + 1)]) )]

print (np.rad2deg(cart2pol(popSum[0],popSum[1])[1])%360)
print ("0 to point in the direction of the positive y-axis and 90 to point in the direction of the positive x-axis: ", 90 - np.rad2deg(cart2pol(popSum[0],popSum[1])[1]))
print ("Convention: ", 90 - np.mean(angles))