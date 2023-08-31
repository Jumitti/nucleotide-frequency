import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import logomaker as lm
import io

plt.ion()

f = 'TEST_weblogo_freq'
saliency_data_df = pd.read_csv(TEST_random_seq.txt, comment='#', sep=' ')

# preview dataframe
saliency_data_df.head()

# create saliency matrix
saliency_mat_df = lm.saliency_to_matrix(seq=saliency_data_df['character'],
                                        values=saliency_data_df['value'])
# preview saliency dataframe.
saliency_mat_df.head()

weblogo_img = lm.Logo(saliency_mat_df, figsize=(18, 3))
plt.savefig("weblogo.png", format="png")
