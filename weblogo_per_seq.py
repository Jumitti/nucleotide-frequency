import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import logomaker as lm
import io

plt.ion()

f = 'TEST_weblogo_freq_per_seq.txt'
saliency_data_df = pd.read_csv(f, comment='#', sep='\t', skipinitialspace=True, skiprows=1)

# Créer une matrice de saliency à partir des données chargées
saliency_mat_df = saliency_data_df.set_index('pos').drop(columns=['A', 'C', 'G', 'T'])
saliency_mat_df.columns = ['A', 'C', 'G', 'T']

# Créer le logo WebLogo
weblogo_img = lm.Logo(saliency_mat_df, figsize=(18, 3))

# Enregistrer le logo en tant qu'image PNG
plt.savefig("weblogo.png", format="png")