import matplotlib.pyplot as plt
import json

plt.style.use('ggplot')

countries = []
population = []
populationfile = open("./data.txt","r")
populationjson = json.loads(populationfile.read())
for sub,pop in populationjson.items():
   countries.append(sub)
   population.append(pop)

x_pos = []
for i in range(0,len(countries)):
   x_pos.append(i)

plt.bar(x_pos, population, color='green')
plt.xlabel("Countries")
plt.ylabel("Population (in crores)")
plt.title("Population of Top 5 Countries")

plt.xticks(x_pos, countries)

plt.show()