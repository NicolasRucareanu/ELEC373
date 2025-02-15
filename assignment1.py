import matplotlib.pyplot as plt
import random

#list of the arrival rates to be tested
arrivalRate = [0.2,0.4,0.5,0.6,0.65,0.7,0.72,0.74,0.745]
#number of time slots to run the simulations
runTime = int(1e6)
#keep track of queue length and average queueing delay
queueLength = []
queueDelay = []
theoreticalDelay = []

for lmbda in arrivalRate:
    serviceQueue = 0
    averageQueue = 0

    for count in range(runTime):
        #create random arrival rate based on lambda
        arrival = bool(random.random() < lmbda)
        #create the random service rate mu = 0.75
        service = bool(random.random() < 0.75)

        if arrival:
            serviceQueue += 1
        if (service and serviceQueue != 0):
            serviceQueue -= 1

        #compute the average queue length
        averageQueue += serviceQueue
    averageQueue = averageQueue / runTime
    queueLength.append(averageQueue)

    #calculate queue delay using little's law
    # W = L / lambda
    averageDelay = averageQueue / lmbda
    queueDelay.append(averageDelay)

    #calculate theoretical queueing delay
    # 1 / (mu - lambda)
    delayTheoretical = 1 / (0.75 - lmbda)
    theoreticalDelay.append(delayTheoretical)

#plot
plt.figure(figsize=(8, 5))
plt.plot(arrivalRate, queueDelay, 'bo-', label="Simulated Delay")
plt.plot(arrivalRate, theoreticalDelay, 'r--', label="Theoretical Delay")
plt.xlabel("Arrival Rate")
plt.ylabel("Expected Queueing Delay")
plt.title("Simulated vs. Theoretical Queueing Delay")
plt.legend()
plt.grid()
plt.show()