#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import sys


waypoint_file = 'D:\Coursera\CarlaSimulator\PythonClient\Course1FinalProject/racetrack_waypoints.txt'
waypoints = np.genfromtxt(waypoint_file, delimiter=',')

solution_file = 'D:\Coursera\CarlaSimulator\PythonClient\Course1FinalProject\controller_output/trajectory.txt'
solution = np.genfromtxt(solution_file, delimiter=',')

fig, (ax1,ax2,ax3) = plt.subplots(3,1)

ax1.plot(solution[:,3], solution[:,6], label='target speed')
ax1.plot(solution[:,3], solution[:,2], label='actual speed')

ax1.legend()
#ax1.set(xlabel='t (s)')
ax1.set(ylabel='speed (kmph)')
#ax1.title('kdd = 0.1')





ax2.plot(solution[:,3], solution[:,5], label='throttle cmd')

#ax2.legend()
#ax2.set(xlabel='t (s)')
ax2.set(ylabel='throttle cmd')
#ax2.title('Kdd = 1')
#ax2.show(block=True)






ax3.plot(solution[:,3], solution[:,4], label='steering cmd')

#ax3.legend()
ax3.set(xlabel='t (s)')
ax3.set(ylabel='steering cmd')
#ax3.title('Kdd = 10')
#ax3.show(block=True)
plt.show()