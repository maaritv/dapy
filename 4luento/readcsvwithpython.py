import numpy as np

# Load CSV into a NumPy array
data = np.genfromtxt('./bookloans.csv', delimiter=';', skip_header=1, dtype=None, encoding=None)

# Iterate and print each row in the array
for row in data:
    print(row)

