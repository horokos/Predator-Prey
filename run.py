from model import Model
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation

model = Model(20, 100, 20, 0.2, 0.1)

for i in range(200):
    model.step()

preys = [i['preys'] for i in model.data]
predators = [i['predators'] for i in model.data]
indexes = range(200)
plt.plot(indexes, preys, label="Prey")
plt.plot(indexes, predators, label="Predator")
plt.legend()
plt.show()
