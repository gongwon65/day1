import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('.\OTg6QzA_activities.csv')


x = data.X.to_numpy()
#print(x)
y = data.Y.to_numpy()
#print(y)



font_title = {'family':'batang','color':'b','size':20}
font_X = {'family':'gulim','color':'k','size':10}
font_Y = {'family':'gulim','color':'k','size':10}

plt.title('노약자의 활동 로그', fontdict= font_title)
plt.xlabel('X 좌표', fontdict= font_X)
plt.ylabel('Y 좌표', fontdict= font_Y)




plt.plot(x, y, 'x',c= 'skyblue', ms= 5)
plt.show()




plt.close('all')