from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt


# input current
#I = 1 # nA
#I = 0.25 # nA
I = 9 # nA

# capacitance and leak resistance
C = 1 # nF
R = 40 # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 200
abs_ref = 5 # absolute refractory period 
ref = 0 # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10 # spike threshold
spike_count = 0
for t in range(tstop):
  
   if not ref:
       V = V - (V/(R*C)) + (I/C)
   else:
       ref -= 1
       V = 0.2 * V_th # reset voltage
   
   if V > V_th:
       spike_count += 1
       V = 50 # emit spike
       ref = abs_ref # set refractory counter

   V_trace += [V]

print('Spikes:{}'.format(spike_count))
plt.plot(V_trace)
plt.show()