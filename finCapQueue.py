# 2 M/M/s FCFS finite capacity queue

import math

def mmsmmetrics(lambd, mu, s, m):
    rho = lambd / (mu * s)
    r = lambd / mu
    if rho != 1:
        geometricsum = (1 - rho ** (m - s + 1)) / (1 - rho)
    else:
        geometricsum = m - s + 1
    sum1 = 0
    for n in range(s):
        sum1 += (r ** n) / math.factorial(n)
    sum2 = ((r ** s) / math.factorial(s)) * geometricsum
    S = sum1 + sum2
    P0 = 1 / S
    
    Pn = [0] * (m + 1)
    for n in range(m + 1):
        if n < s:
            Pn[n] = (r ** n) / math.factorial(n) * P0
        else:
            Pn[n] = (r ** n) / (math.factorial(s) * (s ** (n - s))) * P0  # fixed for exact formula
    
    Pm = Pn[m]
    
    numerator = (r ** s) / math.factorial(s) * P0
    if rho != 1:
        denominator = (1 - rho ** (m - s + 1)) / (1 - rho)
    else:
        denominator = m - s + 1
    
    # Calculate Lq average number in queue
    Lq = numerator * (rho - rho ** (m - s + 1) * (m - s + 1) * (1 - rho)) / ((1 - rho) ** 2 * denominator)
    
    lambdaeff = lambd * (1 - Pm)  # Effective arrival rate
    Wq = Lq / lambdaeff
    W = Wq + (1 / mu)
    L = lambdaeff * W
    
    return P0, Lq, Wq, W, L, Pm, lambdaeff

results = mmsmmetrics(1.1750, 1.0901, 3, 1)
for key, value in zip(["P0", "Lq", "Wq", "W", "L"], results[:5]):
    print(f"{key} = {value:.4f}")
