import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def Func_aspirina(Y,t):
    G = Y[0]
    S = Y[1]
    x = 688 
    if S > x and G >0:
        dSdt = 0.0333*500 - x*0.00077
        dGdt = -0.0333*500 
    elif S > x and G < 0:
        dGdt = 0
        dSdt = - x*0.00077
    elif G >0:
        dGdt = -0.0333*500
        dSdt = 0.0333*500 - S*0.00077
    else:
        dGdt = 0 
        dSdt = -S*0.0057
    
    return [dGdt,dSdt] 
x = 120
y = 7
tempo = np.arange(0,x,1)

solucao= odeint(Func_aspirina,[500,0],tempo)
Listona = []
Listona.append(solucao[:,1])


for i in range(y):
    solucao= odeint(Func_aspirina,[500,solucao[:,1][-1]],tempo)
    Listona.append(solucao[:,1])
Listona = np.append(Listona,solucao[:,1][-1])   





plt.plot(tempo,solucao[:,0],"y")
plt.grid(True)
plt.title("Quantidade de aspirina no sangue")
plt.xlabel("Tempo(min)")
plt.ylabel("Sangue")
plt.show()
tempo = np.arange(0,x*(y+1)+1,1)

plt.plot(tempo,Listona,"r")
plt.grid(True)
plt.title("Quantidade de aspirina no sangue")
plt.xlabel("Tempo(min)")
plt.ylabel("Sangue")
plt.show()



