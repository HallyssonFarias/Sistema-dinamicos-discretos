import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initial population
initial_conditions = [1, 2]  # [rabbits, foxes]
initial_conditions_2 = [4, 5]
# Parameters
a = 2  # rabbits birth rate
b = 2  # rate at which rabbits are eaten
c = 1  # foxes birth rate proportional to rabbits eaten
d = 2  # foxes death rate

# A grid of time points (in days)
t = np.linspace(0, 160, 160)

# The differential equations for the predator-prey model.
def deriv(y, t, a, b, c, d):
    rabbits, foxes = y
    d_rabbits_dt = a * rabbits - b * foxes * rabbits
    d_foxes_dt = c * foxes * rabbits - d * foxes
    return [d_rabbits_dt, d_foxes_dt]

# Integrate the equations over the time grid, t.
ret = odeint(deriv, initial_conditions, t, args=(a, b, c, d))
ret2 = odeint(deriv,initial_conditions_2,t, args=(a+1, b+1, c+1, d+1))

# Split the result into rabbit and fox populations
rabbits, foxes = ret.T
rabbits_2, foxes_2 = ret2.T
# Plot the results
fig1, ax1 = plt.subplots()
ax1.plot(t, rabbits, label="Rabbits")
ax1.plot(t, foxes, label="Foxes")
ax1.set_xlabel('Time (days)')
ax1.set_ylabel('Population')
ax1.legend()
fig2, ax2 = plt.subplots()
ax2.scatter(foxes, rabbits, label='foxes x rabbits', color='b', s=2)
ax2.scatter(foxes_2, rabbits_2, color='r', s=2)
ax2.set_xlabel('foxes')
ax2.set_ylabel('rabbits')
ax2.legend()
plt.show()
