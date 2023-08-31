import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import logomaker as lm

plt.ion()


with lm.open_example_datafile('nn_saliency_values.txt') as f:
    saliency_data_df = pd.read_csv(f, comment='#', sep='\t')

# preview dataframe
saliency_data_df.head()

# create saliency matrix
saliency_mat_df = lm.saliency_to_matrix(seq=saliency_data_df['character'],
                                        values=saliency_data_df['value'])
# preview saliency dataframe.
saliency_mat_df.head()

lm.Logo(saliency_mat_df, figsize=(18, 3))
