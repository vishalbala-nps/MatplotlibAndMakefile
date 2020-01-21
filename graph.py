import matplotlib.pyplot as plt
import json

plt.style.use('ggplot')

subs = []
marks=[]
marksfile = open("./data.txt","r")
marksjson = json.loads(marksfile.read())
for sub,mark in marksjson.items():
   subs.append(sub)
   marks.append(mark)

x_pos = []
for i in range(0,len(subs)):
   x_pos.append(i)

plt.bar(x_pos, marks, color='green')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.xticks(x_pos, subs)

plt.show()