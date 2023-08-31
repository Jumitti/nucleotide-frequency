import numpy as np

def calculer_coefficient_dispersion(proportions):
    proportions_array = np.array(list(proportions.values()))
    mean_proportions = np.mean(proportions_array)
    squared_deviations = (proportions_array - mean_proportions) ** 2
    variance = np.sum(squared_deviations) / len(proportions)
    dispersion_coefficient = np.sqrt(variance) / mean_proportions
    return dispersion_coefficient

# Proportions égales de 0.25 pour chaque lettre
proportions = {
    'A': 0.275,
    'T': 0.275,
    'G': 0.225,
    'C': 0.225
}

dispersion = calculer_coefficient_dispersion(proportions)
print("Dispersion coefficient:", dispersion)