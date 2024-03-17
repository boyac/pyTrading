import numpy as np
import pandas as pd

# Load SPY trading data
spy_data = pd.read_csv('SPY.csv')  # Assuming SPY.csv contains historical trading data for SPY

# Define trading strategy function
def trading_strategy(data, params):
    short_ma_length, long_ma_length = params
    short_ma = data['Close'].rolling(window=short_ma_length).mean()
    long_ma = data['Close'].rolling(window=long_ma_length).mean()
    signals = np.where(short_ma > long_ma, 1, -1)
    returns = np.sum(np.diff(data['Close'].values) * signals[:-1])
    return returns

# Simulated Annealing Algorithm
def simulated_annealing(data, initial_params, iterations, temperature, cooling_rate):
    current_params = np.array(initial_params)
    current_loss = trading_strategy(data, initial_params)
    best_params = initial_params
    best_loss = current_loss

    for i in range(iterations):
        # Generate new parameters
        new_params = current_params + np.random.normal(0, 1, size=len(initial_params))
        new_params = np.maximum(new_params, 1)  # Ensure parameters are positive
        # Calculate loss with new parameters
        new_loss = trading_strategy(data, new_params)

        # Accept new parameters with probability according to Metropolis criterion
        if new_loss > current_loss or np.random.rand() < np.exp(-(new_loss - current_loss) / temperature):
            current_params = new_params
            current_loss = new_loss

        # Update best parameters and loss
        if new_loss > best_loss:
            best_params = new_params
            best_loss = new_loss

        # Lower the temperature
        temperature *= cooling_rate

    return best_params

# Set initial parameters and algorithm parameters
initial_params = [20, 50]  # Initial parameters, e.g., lengths of short and long moving averages
iterations = 1000  # Number of iterations
temperature = 1.0  # Initial temperature
cooling_rate = 0.95  # Cooling rate

# Run simulated annealing algorithm
best_params = simulated_annealing(spy_data, initial_params, iterations, temperature, cooling_rate)
print("Best parameters:", best_params)
