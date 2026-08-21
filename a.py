import numpy as np
import matplotlib.pyplot as plt

# 1. Initialize a 15x40 matrix with zeros
M = np.zeros((15, 40))

# 2. Draw 'H'
M[1:6, 1] = 1       # Left bar
M[1:6, 5] = 1       # Right bar
M[3, 2:5] = 1       # Crossbar

# 3. Draw 'E'
M[3:8, 10] = 1      # Left bar
M[3, 11:14] = 1     # Top bar
M[5, 11:14] = 1     # Middle bar
M[7, 11:14] = 1     # Bottom bar

# 4. Draw first 'L'
M[5:10, 18] = 1     # Left bar
M[9, 19:22] = 1     # Bottom bar

# 5. Draw second 'L'
M[7:12, 26] = 1     # Left bar
M[11, 27:30] = 1    # Bottom bar

# 6. Draw 'O' (4 rows tall to ensure bottom-right is exactly at 13)
M[9:13, 34] = 1     # Left bar
M[9:13, 38] = 1     # Right bar
M[9, 35:38] = 1     # Top bar
M[12, 35:38] = 1    # Bottom bar

# Visualizing the sparse matrix to confirm it matches the exam paper
plt.spy(M)
plt.show()