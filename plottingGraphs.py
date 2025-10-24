# 3 Plotting graphs using M/M/s/m

import math
import matplotlib.pyplot as plt

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
            Pn[n] = (r ** n) / (math.factorial(s) * (s ** (n - s))) * P0
    
    Pm = Pn[m]
    
    numerator = (r ** s) / math.factorial(s) * P0
    if rho != 1:
        denominator = (1 - rho ** (m - s + 1)) / (1 - rho)
    else:
        denominator = m - s + 1
    
    Lq = numerator * (rho - rho ** (m - s + 1) * (m - s + 1) * (1 - rho)) / ((1 - rho) ** 2 * denominator)
    lambdaeff = lambd * (1 - Pm)
    Wq = Lq / lambdaeff
    W = Wq + (1 / mu)
    L = lambdaeff * W
    
    return Lq, Wq, W, L, P0

lambd = 1.1750
mu = 1.0901
s = 3

mvalues = list(range(3, 101))
Lvals = []
Lqvals = []
Wvals = []
Wqvals = []
P0vals = []

for m in mvalues:
    results = mmsmmetrics(lambd, mu, s, m)
    Lqvals.append(results[0])
    Wqvals.append(results[1])
    Wvals.append(results[2])
    Lvals.append(results[3])
    P0vals.append(results[4])

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(mvalues, Lvals, label='L vs m')
plt.axhline(y=1.1391, color='r', linestyle='--', label='L 1.1391')
plt.xlabel('m')
plt.ylabel('L')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(mvalues, Lqvals, label='Lq vs m')
plt.axhline(y=0.0612, color='r', linestyle='--', label='Lq 0.0612')
plt.xlabel('m')
plt.ylabel('Lq')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(mvalues, Wvals, label='W vs m')
plt.axhline(y=0.9694, color='r', linestyle='--', label='W 0.9694')
plt.xlabel('m')
plt.ylabel('W')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(mvalues, Wqvals, label='Wq vs m')
plt.axhline(y=0.0521, color='r', linestyle='--', label='Wq 0.0521')
plt.xlabel('m')
plt.ylabel('Wq')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
