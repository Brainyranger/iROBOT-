import matplotlib.pyplot as plt 
import math
import csv
from pulp import *
file = open("confiserie.csv")
data = csv.reader(file)
Lx=[]
Ly=[]
for row in data:
    print(row)
    _,y,z=row
    Lx.append(float(y))
    Ly.append(float(z))

#1.3)LAD plus robuste
#Ly[-1]=5.67    

model = LpProblem(name="Ex01", sense=LpMinimize) 

n=17

z = LpVariable.matrix("z", list(range(1,n+1)),lowBound=0)
a = LpVariable("a",  lowBound=0)
b = LpVariable("b",  lowBound=0)

model += lpSum(z)

i:int
for i in range(0,len(Lx)):
    model += (z[i]>=Ly[i]-a-b*Lx[i])
    model += (z[i]>=a+b*Lx[i]-Ly[i])
    
#18 a            B        25.9376             0               
#19 b            B        20.2464             0 
status = model.solve(solver=GLPK(msg=True,keepFiles=True)) 

print("Status:", LpStatus[model.status])

print("objective=", value(model.objective))
Lz=[]
for i in range(0,n):
    Lz.append(value(z[i]))
    print("z[",i,"]=",value(z[i]))




#1.2)
 
plt.scatter(Lx,Ly)
plt.plot(Lx,Lz)
plt.show()