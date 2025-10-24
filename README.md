# M/M/s Queueing Simulation

This repository contains Python implementations and simulations of M/M/s queueing models with both infinite and finite capacity systems. It also includes plotting functions for visualizing queue metrics and a simple discrete-event simulation for real-time queue behavior.

## Codebase Overview

### 1. M/M/s Infinite Capacity Queue (mmsmetrics)
- Computes classic queueing metrics such as:
  - \( P_0 \): Probability of zero customers in the system.
  - \( L_q \): Average number of customers waiting in the queue.
  - \( W_q \): Average waiting time in the queue.
  - \( W \): Total average time in the system.
  - \( L \): Average number of customers in the system.
- Uses input parameters: arrival rate (\( \lambda \)), service rate (\( \mu \)), and number of servers (\( s \)).
- Raises error if system stability condition (\( \rho < 1 \)) is violated.

### 2. M/M/s Finite Capacity Queue (mmsmmetrics)
- Extends the infinite queue to account for finite system capacity \( m \).
- Calculates probabilities for all states up to capacity.
- Computes effective arrival rate considering blocking.
- Provides detailed metrics including blocking probability \( P_m \).

### 3. Plotting Queue Metrics
- Uses matplotlib to plot queue metrics \( L \), \( L_q \), \( W \), and \( W_q \) against varying system capacity \( m \).
- Visualizes how queue performance changes as capacity increases.

### 4. Real-time Queue Simulation
- Discrete event simulation modeling arrivals and service times using exponential distributions.
- Logs events with timestamps for arrivals, service starts, waiting, and service duration.
- Estimates arrival and service rates from simulated data.
- Useful for understanding dynamic behavior and performance estimation.

## How to Use

1. Modify parameters like arrival rate, service rate, number of servers, and capacity in each function call.
2. Run the scripts to compute analytics or perform simulations.
3. Use the plotting script to visualize impact of system capacity.
4. Analyze simulation logs for deeper insight into queue dynamics.

## Dependencies

- Python 3.x
- math (standard library)
- matplotlib
- pandas
- random (standard library)

Install required libraries using pip if necessary:

