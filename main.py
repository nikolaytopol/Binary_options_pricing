import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
import cufflinks as cf

pd.set_option('display.max_rows', 300)
np.set_printoptions(suppress=True)

def simulate_path(s0, r, sigma,T, t, n):
    
    dt = T/t       
    S = zeros((t+1, n))
    S[0] = s0
    for i in range(1, t+1):                         
        z = random.standard_normal(n)    
        S[i] = S[i-1] * (1+r*dt + sigma * sqrt(dt) * z) 
    return S

price_path = pd.DataFrame(simulate_path(100, 0.05, 0.20, 1, 252, 100000))
price_path.iloc[:,:100].iplot(title='Simulated Geometric Brownian Motion Paths', xTitle='Time Steps', yTitle='Index Levels')
