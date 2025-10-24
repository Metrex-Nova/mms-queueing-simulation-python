# 4 Real-time data simulation for queue

import random
import pandas as pd

SIMTIME = 120  # Total time in seconds (2 minutes)
LAMBDA = 1.2   # Arrival rate signals per second adjustable
MU = 1.0       # Service rate signals per second

currenttime = 0
nextarrivaltime = random.expovariate(LAMBDA)
serveravailabletime = 0
signallog = []
signalnumber = 1

while nextarrivaltime < SIMTIME:
    arrivaltime = nextarrivaltime
    servicestart = max(arrivaltime, serveravailabletime)
    serviceduration = random.expovariate(MU)
    serviceend = servicestart + serviceduration
    waittime = servicestart - arrivaltime
    
    signallog.append({
        "Signal": signalnumber,
        "Arrival Time s": round(arrivaltime, 2),
        "Service Start s": round(servicestart, 2),
        "Service End s": round(serviceend, 2),
        "Wait Time s": round(waittime, 2),
        "Service Duration s": round(serviceduration, 2)
    })
    
    signalnumber += 1
    serveravailabletime = serviceend
    nextarrivaltime = nextarrivaltime + random.expovariate(LAMBDA)

df = pd.DataFrame(signallog)

totaltime = SIMTIME
lambdasim = len(df) / totaltime
totalservicetime = df["Service Duration s"].sum()
musim = len(df) / totalservicetime

print(df.to_string(index=False))
print("--- SIMULATION SUMMARY ---")
print(f"Total simulation time {SIMTIME} seconds")
print(f"Total signals arrived {len(df)}")
print(f"Total signals served {len(df)}")
print(f"Estimated arrival rate {lambdasim:.4f} signals/sec")
print(f"Estimated service rate {musim:.4f} signals/sec")
