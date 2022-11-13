# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
 
data1 = np.loadtxt("TbMK70.txt", dtype=np.float)
data2 = np.loadtxt("3YTb05MK.txt", dtype=np.float)
data3 = np.loadtxt("1YTb01MK.txt", dtype=np.float)
data4 = np.loadtxt("2YTb001MK.txt", dtype=np.float)
data5 = np.loadtxt("13YMK70.txt", dtype=np.float)


x1 = data1[:,0]             
y1 = np.log(data1[:,1])                 
x2 = data2[:,0]                    
y2 = np.log(data2[:,1])+5        
x3 = data3[:,0]                    
y3 = np.log(data3[:,1])+10       
x4 = data4[:,0]                    
y4 = np.log(data4[:,1])+15    
x5 = data5[:,0]                    
y5 = np.log(data5[:,1])+20                          

fig, ax = plt.subplots()                        

ax.plot(x1, y1, '-p', markersize=0, linewidth=1, color = 'black', label = 'T=70')
ax.plot(x2, y2, '-p', markersize=0, linewidth=1, color = 'dimgray', label = 'T=120')
ax.plot(x3, y3, '-p', markersize=0, linewidth=1, color = 'gray', label = '0,1Tb')
ax.plot(x4, y4, '-p', markersize=0, linewidth=1, color = 'darkgray', label = '0,01Tb')
ax.plot(x5, y5, '-p', markersize=0, linewidth=1, color = 'lightgray', label = 'Y')

ax.set_xlabel("2\u03B8, \u00B0")                              
ax.set_ylabel("ln(I), отн. ед.")                             
plt.xlim(5,50)
#plt.ylim(0,15) #ограничение по игрекам
ax.legend() 
#ax.legend(borderpad=1, fontsize=7)  #размеры легенды                                   
#ax.text(11, 37000, "001", rotation = 'vertical') #если надо напечатать текст
plt.show()              
fig.savefig('Y-Tb.jpg',dpi=600) 



