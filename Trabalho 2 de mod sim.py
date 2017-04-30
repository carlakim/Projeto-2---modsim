import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def Func_aspirina(Y,t):
    G = Y[0]
    S = Y[1]
    if G >0:
        dGdt = -0.0333*500
    else:
        dGdt = 0
        
    if G >0:
        dSdt = 0.0333*500 - S*0.0057
    else:
        dSdt = -S*0.0057
    return [dGdt,dSdt]

tempo = np.arange(0,240,1)

solucao= odeint(Func_aspirina,[500,0],tempo)

plt.plot(tempo,solucao[:,0],"y")
plt.grid(True)
plt.title("Quantidade de aspirina no sistem gastroinstetinal")
plt.xlabel("Tempo(min)")
plt.ylabel("Gastrointestinal")
plt.show()

plt.plot(tempo,solucao[:,1],"r")
plt.grid(True)
plt.title("Quantidade de aspirina no sangue")
plt.xlabel("Tempo(min)")
plt.ylabel("Sangue")
plt.show()



