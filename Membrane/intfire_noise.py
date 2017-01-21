from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt

a_noise_lvl = int(sys.argv[1])
# input current
I = 1 # nA

# capacitance and leak resistance
C = 1 # nF
R = 40 # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 2000
abs_ref = 5 # absolute refractory period 
ref = 0 # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10 # spike threshold
spiketimes = [] # list of spike times

# input current
noiseamp = a_noise_lvl # amplitude of added noise
I += noiseamp*np.random.normal(0, 1, (tstop,)) # nA; Gaussian noise

intervals = []
msecs = 0

for t in range(tstop):
   msecs += 1
    
   if not ref:
       V = V - (V/(R*C)) + (I[t]/C)
   else:
       ref -= 1
       V = 0.2 * V_th # reset voltage
   
   if V > V_th:
       intervals.append(msecs)
       msecs = 0
       V = 50 # emit spike
       ref = abs_ref # set refractory counter

   V_trace += [V]


#plt.plot(V_trace)
plt.hist(intervals)
plt.show()