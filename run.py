from model import Model
from matplotlib import pyplot as plt

model = Model(20, 100, 20, 0.2, 0.1)

for i in range(200):
    model.step()

preys = [i['preys'] for i in model.data]
predators = [i['predators'] for i in model.data]
indexes = range(200)
plt.plot(indexes, preys)
plt.plot(indexes, predators)
plt.show()
