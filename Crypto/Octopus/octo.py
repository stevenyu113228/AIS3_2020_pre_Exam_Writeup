import numpy as np


# qubit
# →: 1j
# ↑: 1+0j
# ↘: 0.707-0.707j
# ↗: 0.707+0.707j

def Q(x):
    return {
        '1j': 1j,
        '(1+0j)': 1+0j,
        '(0.707-0.707j)': 0.707-0.707j,
        '(0.707+0.707j)': 0.707+0.707j
    }[x]

LEN = 1024
basis = ['+', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', '+', 'x', '+', 'x', '+', '+', 'x', 'x', '+', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', '+', '+', '+', '+', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '+', '+', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', '+', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', '+', '+', '+', '+', '+', '+', 'x', 'x', 'x', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', '+', '+', 'x', '+', '+', '+', 'x', '+', '+', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', '+', 'x', '+', '+', '+', 'x', 'x', '+', 'x', '+', '+', '+', '+', '+', '+', 'x', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', 'x', 'x', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', '+', '+', '+', '+', 'x', '+', '+', 'x', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', '+', 'x', 'x', '+', 'x', '+', 'x', '+', '+', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', '+', 'x', '+', '+', 'x', 'x', '+', 'x', '+', '+', '+', 'x', '+', '+', '+', '+', '+', '+', 'x', '+', '+', '+', 'x', '+', '+', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', '+', '+', '+', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', 'x', 'x', 'x', '+', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', '+', '+', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', '+', '+', 'x', '+', '+', '+', 'x', '+', 'x', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', '+', 'x', '+', 'x', '+', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', '+', '+', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', '+', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', '+', '+', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', '+', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', '+', '+', 'x', '+', '+', '+', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', '+', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', '+', '+', 'x', 'x', '+', '+', 'x', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', '+', '+', '+', '+', 'x', '+', '+', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', '+', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', '+', '+', '+', 'x', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', '+', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', '+', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', '+', '+', 'x', '+', 'x', '+', '+', '+', '+', '+', '+', '+', 'x', '+', '+', '+', '+', 'x', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', '+', 'x', '+', 'x', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', '+', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', '+', 'x']

qubits = [1j, 1j, (1+0j), (1+0j), 1j, 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), (1+0j), (1+0j), 1j, (0.707-0.707j), 1j, (0.707+0.707j), (0.707+0.707j), 1j, (0.707+0.707j), (0.707-0.707j), (1+0j), 1j, (1+0j), (0.707-0.707j), (0.707+0.707j), (1+0j), 1j, 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), (0.707-0.707j), (1+0j), (0.707+0.707j), (1+0j), (1+0j), (0.707-0.707j), (0.707-0.707j), (1+0j), (1+0j), (0.707-0.707j), (1+0j), 1j, (1+0j), 1j, (0.707+0.707j), (0.707+0.707j), (1+0j), 1j, (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (1+0j), (0.707-0.707j), (1+0j), (1+0j), (0.707+0.707j), (1+0j), 1j, (0.707+0.707j), (0.707+0.707j), (1+0j), 1j, 1j, (1+0j), (1+0j), (0.707+0.707j), 1j, (1+0j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), 1j, 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), 1j, 1j, (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), 1j, (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (0.707+0.707j), 1j, (0.707-0.707j), 1j, (0.707-0.707j), 1j, (0.707-0.707j), (1+0j), 1j, (1+0j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (1+0j), (1+0j), 1j, (1+0j), 1j, 1j, (1+0j), (1+0j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), 1j, (1+0j), (1+0j), 1j, (1+0j), (0.707-0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), 1j, (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), 1j, 1j, (1+0j), (1+0j), 1j, (0.707+0.707j), 1j, (1+0j), 1j, (0.707-0.707j), 1j, 1j, (0.707-0.707j), (0.707-0.707j), 1j, (1+0j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (1+0j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (1+0j), 1j, (0.707-0.707j), (0.707-0.707j), 1j, (0.707+0.707j), 1j, (0.707-0.707j), (0.707-0.707j), (1+0j), 1j, (0.707-0.707j), (1+0j), (1+0j), 1j, (0.707+0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (1+0j), 1j, 1j, (1+0j), (1+0j), (1+0j), (0.707+0.707j), (1+0j), 1j, (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), 1j, (0.707-0.707j), (0.707-0.707j), (1+0j), (1+0j), (0.707+0.707j), (1+0j), (1+0j), (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), 1j, (0.707+0.707j), 1j, (0.707+0.707j), 1j, 1j, 1j, 1j, (0.707+0.707j), 1j, (1+0j), (0.707-0.707j), (1+0j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (1+0j), (1+0j), (1+0j), 1j, (0.707+0.707j), (0.707-0.707j), 1j, (0.707-0.707j), 1j, (0.707-0.707j), 1j, 1j, (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (1+0j), 1j, (0.707+0.707j), (1+0j), (0.707-0.707j), 1j, 1j, (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707-0.707j), 1j, 1j, (1+0j), (0.707+0.707j), 1j, (1+0j), (1+0j), (1+0j), (1+0j), 1j, (0.707-0.707j), 1j, (1+0j), (1+0j), (0.707+0.707j), 1j, 1j, (0.707-0.707j), 1j, (0.707+0.707j), (0.707+0.707j), 1j, (0.707+0.707j), 1j, (0.707-0.707j), 1j, (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (1+0j), (1+0j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), 1j, (1+0j), 1j, 1j, (0.707-0.707j), 1j, (0.707-0.707j), (0.707-0.707j), 1j, (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), 1j, 1j, (1+0j), (1+0j), (1+0j), 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), 1j, (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), 1j, (1+0j), 1j, 1j, (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), 1j, (0.707-0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707-0.707j), 1j, 1j, (0.707-0.707j), 1j, 1j, (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (1+0j), 1j, 1j, 1j, (0.707+0.707j), (1+0j), (1+0j), (1+0j), (0.707-0.707j), (1+0j), (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), (1+0j), 1j, (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (1+0j), (0.707+0.707j), (1+0j), 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), 1j, (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), 1j, (0.707+0.707j), 1j, (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), (1+0j), 1j, 1j, (0.707-0.707j), 1j, (0.707-0.707j), 1j, (0.707-0.707j), 1j, (0.707+0.707j), 1j, (0.707-0.707j), 1j, (0.707-0.707j), (1+0j), (0.707+0.707j), 1j, 1j, 1j, (0.707-0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (1+0j), (0.707+0.707j), 1j, (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), (1+0j), (1+0j), 1j, (0.707+0.707j), (1+0j), 1j, (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), (1+0j), 1j, (1+0j), (0.707+0.707j), (0.707+0.707j), (1+0j), 1j, 1j, 1j, 1j, (1+0j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), (1+0j), (0.707+0.707j), (1+0j), (0.707-0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (1+0j), (1+0j), (0.707-0.707j), (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), 1j, (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (1+0j), (1+0j), (1+0j), 1j, (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), (1+0j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), 1j, (1+0j), (0.707-0.707j), 1j, 1j, (0.707+0.707j), (1+0j), (1+0j), (0.707+0.707j), 1j, 1j, (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707+0.707j), (1+0j), (1+0j), 1j, (0.707+0.707j), (1+0j), (1+0j), 1j, (1+0j), (1+0j), 1j, 1j, 1j, (0.707-0.707j), (0.707-0.707j), (1+0j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), (0.707-0.707j), 1j, 1j, (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), 1j, (0.707-0.707j), 1j, (0.707-0.707j), 1j, (0.707+0.707j), (1+0j), 1j, (0.707-0.707j), (0.707-0.707j), (1+0j), 1j, (1+0j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (0.707-0.707j), (1+0j), (1+0j), (1+0j), 1j, (0.707-0.707j), 1j, (0.707+0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (0.707+0.707j), 1j, (0.707-0.707j), (1+0j), (1+0j), 1j, (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), 1j, (0.707+0.707j), (0.707+0.707j), 1j, (0.707-0.707j), (0.707-0.707j), 1j, (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), 1j, (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (1+0j), (0.707+0.707j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), (1+0j), 1j, 1j, (0.707-0.707j), (1+0j), 1j, (0.707+0.707j), (0.707-0.707j), (1+0j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), 1j, (1+0j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), 1j, (1+0j), 1j, (0.707-0.707j), (0.707+0.707j), (1+0j), 1j, (0.707-0.707j), 1j, 1j, 1j, (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), 1j, 1j, (1+0j), (1+0j), 1j, (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (0.707+0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707+0.707j), (0.707+0.707j), (1+0j), 1j, 1j, 1j, (0.707-0.707j), (1+0j), (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707+0.707j), (1+0j), (0.707+0.707j), (1+0j), (0.707+0.707j), 1j, (1+0j), (1+0j), (1+0j), (0.707-0.707j), (1+0j), 1j, (0.707-0.707j), (0.707-0.707j), 1j, (0.707+0.707j), (1+0j), (1+0j), (0.707+0.707j), (1+0j), (1+0j), (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), 1j, (1+0j), (1+0j), (1+0j), (0.707-0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), 1j, 1j, (1+0j), (0.707-0.707j), 1j, (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), 1j, 1j, (0.707+0.707j), 1j, 1j, 1j, (0.707-0.707j), 1j, (0.707-0.707j), 1j, (1+0j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), (1+0j), 1j, 1j, (0.707+0.707j), (0.707+0.707j), 1j, (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), 1j, 1j, (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), 1j, (0.707+0.707j), 1j, (1+0j), (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), (0.707+0.707j), 1j, (1+0j), 1j, 1j, (0.707-0.707j), (0.707-0.707j), 1j, (1+0j), 1j, (0.707+0.707j), 1j, (0.707-0.707j), (0.707+0.707j), (0.707+0.707j), 1j, (0.707+0.707j), 1j, (1+0j), (0.707+0.707j), (0.707+0.707j), (1+0j), 1j, 1j, 1j, 1j, (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), 1j, (0.707+0.707j), (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), (0.707+0.707j), (0.707-0.707j), (0.707+0.707j), 1j, 1j, (0.707-0.707j), (0.707+0.707j), 1j, (1+0j), 1j, (0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), (0.707+0.707j), (1+0j), (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), 1j, (1+0j), 1j, 1j, (0.707+0.707j), (1+0j), 1j, (0.707-0.707j), 1j, (0.707+0.707j), 1j, 1j, (1+0j), 1j, 1j, (1+0j), 1j, (0.707+0.707j), (1+0j), 1j, (1+0j), 1j, (0.707-0.707j), 1j, 1j, (0.707-0.707j), 1j, (0.707+0.707j), (1+0j), (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707+0.707j), (0.707-0.707j), 1j, (0.707+0.707j), (0.707-0.707j), (1+0j), (1+0j), (1+0j), (0.707+0.707j), 1j, (0.707-0.707j), (0.707-0.707j), 1j, 1j, (0.707+0.707j), (1+0j), (0.707+0.707j), (1+0j), (0.707+0.707j), (0.707-0.707j), 1j, 1j, (1+0j), (0.707-0.707j), (1+0j), (0.707-0.707j), (0.707+0.707j), 1j, 1j, (0.707+0.707j), (0.707-0.707j), 1j, 1j, (0.707+0.707j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (0.707-0.707j), (0.707+0.707j), (1+0j), (1+0j), (0.707-0.707j), (0.707-0.707j), (1+0j), (0.707+0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j), 1j, (0.707+0.707j), (1+0j), (1+0j), (1+0j), (0.707-0.707j)]

my_basis = ['+', 'x', '+', '+', 'x', '+', 'x', '+', 'x', 'x', '+', '+', 'x', '+', '+', 'x', 'x', '+', 'x', '+', '+', '+', '+', 'x', 'x', 'x', 'x', '+', '+', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', 'x', '+', 'x', 'x', '+', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', '+', '+', '+', 'x', '+', '+', '+', '+', '+', '+', '+', '+', 'x', '+', '+', 'x', '+', '+', 'x', '+', '+', '+', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', '+', '+', '+', 'x', '+', '+', '+', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', '+', '+', 'x', 'x', 'x', '+', '+', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', '+', 'x', '+', '+', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', '+', 'x', 'x', '+', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', 'x', 'x', '+', '+', '+', '+', 'x', '+', '+', '+', '+', '+', '+', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', 'x', '+', '+', '+', 'x', '+', '+', 'x', '+', '+', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', '+', '+', '+', 'x', '+', '+', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', '+', '+', '+', 'x', 'x', 'x', '+', 'x', '+', '+', '+', '+', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', '+', '+', 'x', '+', '+', 'x', 'x', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', '+', '+', '+', 'x', 'x', '+', '+', 'x', 'x', '+', '+', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', '+', '+', 'x', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', '+', 'x', '+', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', 'x', 'x', '+', '+', 'x', '+', '+', '+', 'x', '+', 'x', '+', '+', 'x', '+', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', '+', '+', '+', '+', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', '+', '+', 'x', '+', '+', 'x', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', '+', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', '+', '+', '+', 'x', 'x', '+', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', '+', '+', '+', '+', 'x', '+', 'x', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', 'x', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', 'x', 'x', '+', '+', '+', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', '+', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', '+', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', '+', '+', 'x', '+', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', '+', '+', '+', '+', 'x', '+', '+', '+', 'x', '+', '+', '+', 'x', 'x', '+', '+', 'x', '+', '+', 'x', '+', '+', '+', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', '+', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', '+', '+', '+', '+', 'x', 'x', 'x', '+', 'x', '+']

final = 2114605261815340712424659413225647507317872952942366497800823462312932228799031989657646284020761432666257418566252521668

def rotate(q):
    # For diagonal basis measure
    return q * complex(0.707, -0.707)

# recover initial bitstream
bitstream = ''
for i in range(LEN):
    # print(qubits[i] == '1j')
    if basis[i] == '+' and qubits[i] == 1j:
        bitstream += '0'
    elif basis[i] == '+' and qubits[i] == 1+0j:
        bitstream += '1'
    elif basis[i] == 'x' and qubits[i] == 0.707-0.707j:
        bitstream += '0'
    elif basis[i] == 'x' and qubits[i] == 0.707+0.707j:
        bitstream += '1'

print(bitstream)
# print(len(bitstream)) # len = 1024

measured_bits = ''
for q, b in zip(qubits, basis):
    if b == 'x':
        q = rotate(q)
    
    probability_zero = round(pow(q.real, 2), 1) # if not correct, swap the two
    probability_one = round(pow(q.imag, 2), 1)

    measured_bits += str(np.random.choice(np.arange(0, 2), p=[probability_zero, probability_one]))


print(measured_bits)
# print(len(measured_bits)) # len = 1024

shared_key = ''
for bit, tx_base, rx_base in zip(measured_bits, basis, my_basis):
    if tx_base == rx_base:
        shared_key += bit

print(shared_key)
print(len(shared_key))

flag = int(shared_key[:400],2) ^ int(final)
flag_bin = hex(flag)[2:]

for i in range(0,len(flag_bin),2):
    print(chr(int(flag_bin[i:i+2],16)),end='')
