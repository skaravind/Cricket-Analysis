import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Matches.csv")
captains = pd.read_csv("Captains.csv")
array = dataset.as_matrix()
arrayCaps = captains.as_matrix()
labels = []
x = []
xt = []
y = []
i = 0
size = len(dataset)
countries = ['India', 'West Indies','WI', 'New Zealand','NZ', 'Bangladesh','BDESH', 'Australia','AUS', 'Pakistan','PAK', 'South Africa','SA','Zimbabwe','ZIM','Sri Lanka','SL']
while(1):
    try:
        labels.append(array[i][5])
        xt.append(i)
        i = i+150
    except:
        labels.append(array[size-1][5])
        xt.append(size-1)
        break


ans = raw_input("Performance of which country do you want to see? (type full name, with first letter of each word capital) - ")

for c in countries:
    if ans in c:
        flag = 1
        country = c
        break
    else:
        flag = 0

if flag == 0:
    print("Not found")
    exit()

points = 1000

for i in range(size):
    if country == array[i][1]:
        if array[i][3] == 'won':
            points += 5
        elif array[i][3] == 'lost':
            points -= 5
        else:
            continue
        y.append(points)
        x.append(i)

'''
#Linear Regression

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
x = np.asarray(x).reshape(-1,1)
y = np.asarray(y).reshape(-1,1)
lin_reg.fit(x, y)
'''

plt.title(str(country) + " over the years [ODI]")
plt.plot(x,y)
plt.legend()
plt.xticks(xt, labels, rotation = 'vertical')
plt.ylabel("Points")
plt.axhline(y=1000, xmin=0, xmax=1, hold=None)

j = 0
flag = 0


from sklearn.linear_model import LinearRegression

x_start = 0
x_lin = []
y_lin = []
for i in range(len(arrayCaps)):
    for k in range(len(countries)):
        if country in countries[k]:
            name,place = arrayCaps[i][1].split("(")
            if (countries[k].lower() in place.lower()) or (countries[k+1].lower() in place.lower()):
                a,b = arrayCaps[i][2].split("-")
                for label in labels:
                    if (b in label) and (flag == 0):
                        plt.axvline(x=xt[j],ymin=0, ymax = 1, linewidth=5, color='g')
                        print(xt[j])
                        flag = 1
                        print(str(xt[j]) + ' - ' + str(xt[x_start]))
                        for i in range(len(x)):
                            if (x[i] <= xt[j]) and (x[i] >= xt[x_start]):
                                x_lin.append(x[i])
                                y_lin.append(y[i])
                            else:
                                continue
                        x_lin = np.asarray(x_lin).reshape(-1, 1)
                        y_lin = np.asarray(y_lin).reshape(-1, 1)
                        lin_reg = LinearRegression()
                        try:
                            lin_reg.fit(x_lin, y_lin)
                            plt.plot(x_lin, lin_reg.predict(x_lin), color='red', linewidth=2)
                            print("plotted")
                        except:
                            print("dint work")
                            pass
                        x_lin = []
                        y_lin = []
                        x_start = j

                    j = j+1
                j = 0
                flag = 0



plt.margins(0.2)

plt.show()