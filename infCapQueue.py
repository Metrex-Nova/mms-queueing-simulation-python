# 1 M/M/s FCFS infinite capacity queue

import math

def mmsmetrics(lambd, mu, s):
    rho = lambd / (mu * s)
    if rho >= 1:
        raise ValueError("System is unstable (rho >= 1). Ensure that s*mu > lambda.")
    # traffic intensity total
    r = lambd / mu
    # traffic intensity per server
    # Compute P0
    sumterms = 0
    for n in range(s):
        sumterms += (r ** n) / math.factorial(n)
    lastterm = (r ** s) / (math.factorial(s) * (1 - rho))
    P0 = 1 / (sumterms + lastterm)
    
    # Compute Lq average number in queue
    Lq = (P0 * (r ** s) * rho) / (math.factorial(s) * (1 - rho) ** 2)
    # Compute Wq average waiting time in queue
    Wq = Lq / lambd
    # Compute W total time in system
    W = Wq + (1 / mu)
    # Compute L average number in system
    L = lambd * W
    
    return L, Lq, W, Wq, P0

results = mmsmetrics(1.1750, 1.0901, 3)
for key, value in zip(["L", "Lq", "W", "Wq", "P0"], results):
    print(f"{key} = {value:.4f}")
