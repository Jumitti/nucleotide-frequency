# MIT License

# Copyright (c) 2023 Minniti Julien

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random
from nucleotide_frequency import NCBIdna
from tqdm import tqdm
from collections import Counter
import numpy as np


def lire_sequences(filename):
    sequences = []
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        current_sequence = None
        current_sequence_data = []
        for line in lines:
            if line.startswith('>'):
                if current_sequence is not None:
                    sequences.append((current_sequence, ''.join(current_sequence_data)))
                current_sequence = line[1:]
                current_sequence_data = []
            else:
                current_sequence_data.append(line)
        if current_sequence is not None:
            sequences.append((current_sequence, ''.join(current_sequence_data)))
    return sequences


def generer_morceaux(sequence, longueurs, nombre):
    morceaux = {}
    for longueur in longueurs:
        morceaux[longueur] = []
        for _ in range(nombre):
            start = random.randint(0, len(sequence) - longueur)
            morceaux[longueur].append(sequence[start:start + longueur])
            pbar.update(1)
    return morceaux


def calculer_coefficient_dispersion(proportions):
    proportions_array = np.array(list(proportions.values()))
    mean_proportions = np.mean(proportions_array)
    squared_deviations = (proportions_array - mean_proportions) ** 2
    variance = np.sum(squared_deviations) / len(proportions)
    dispersion_coefficient = np.sqrt(variance) / mean_proportions
    return dispersion_coefficient


min_truncation = 100
max_truncation = 20000
step = 100
longueurs = list(range(min_truncation, max_truncation + step, step))
nombre_morceaux = 1000

filename = 'GRCh38.txt'
sequences = lire_sequences(filename)

freq_per_seq = ['Chraccver Lenght A T G C Disp\n']
disp_per_seq = []
dis_stat = ['Lenght Mean SEM SD\n']
dispersion_par_longueur = {}

iterations = len(sequences) * (max_truncation - min_truncation) / step * nombre_morceaux * 3

with tqdm(total=iterations, desc='Generate truncations...', mininterval=0.1) as pbar:
    for name, sequence in sequences:
        morceaux = generer_morceaux(sequence.upper(), longueurs, nombre_morceaux)
        for longueur, liste_morceaux in morceaux.items():
            for idx, morceau in enumerate(liste_morceaux):
                proportions, proportions_output = NCBIdna.nucleotide_frequency(morceau)
                pbar.update(1)
                dispersion_coefficient = calculer_coefficient_dispersion(proportions)
                pbar.update(1)
                freq_per_seq.append(f"{name} {longueur} {proportions_output} {dispersion_coefficient}\n")
                disp_per_seq.append(f"{longueur} {dispersion_coefficient}\n")

print('Truncation, frequency and dispersion done :)')
for disp_value in tqdm(disp_per_seq, desc='Generating dispersion per lenght table...', mininterval=0.1):
    longueur, dispersion = map(float, disp_value.strip().split())
    if longueur not in dispersion_par_longueur:
        dispersion_par_longueur[longueur] = []
    dispersion_par_longueur[longueur].append(dispersion)

print('Generate dispersion per lenght done :)')
for longueur, dispersions in tqdm(dispersion_par_longueur.items(), desc="Calcul of mean SEM and SD...",
                                  mininterval=0.1):
    moyenne = np.mean(dispersions)
    sem = np.std(dispersions, ddof=1) / np.sqrt(len(dispersions))
    sd = np.std(dispersions, ddof=1)
    dis_stat.append(f'{longueur} {moyenne:.4f} {sem:.4f} {sd:.4f}\n')

print('Mean SEM and SD done :)')
frequency = "freq_per_seq.txt"
with open(frequency, "w") as fasta_file:
    fasta_file.writelines(freq_per_seq)

disp = "disp_stat.txt"
with open(disp, "w") as fasta_file:
    fasta_file.writelines(dis_stat)

print('All done :)')
