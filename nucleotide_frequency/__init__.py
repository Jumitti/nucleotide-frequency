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

import time
import requests


class NCBIdna:
    def __init__(self,
                 gene_id,
                 species=None,
                 upstream=None,
                 downstream=None,
                 prom_term=None):
        self.gene_id = gene_id
        self.upstream = int(upstream) if upstream is not None else None
        self.downstream = int(downstream) if downstream is not None else None
        self.prom_term = prom_term if prom_term is not None else None
        self.species = species if species is not None else None

    @staticmethod
    # Get DNA sequence
    def get_random_sequence(chraccver, start, end):
        # Request for DNA sequence
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={chraccver}&from={start}&to={end}&rettype=fasta&retmode=text"
        response = requests.get(url)

        if response.status_code == 200:
            # Extraction of DNA sequence
            dna_sequence = response.text.split('\n', 1)[1].replace('\n', '')

            return dna_sequence

    @staticmethod
    # Get DNA sequence
    def get_chromosome_sequence(chraccver):
        # Request for DNA sequence
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={chraccver}&rettype=fasta&retmode=text"
        response = requests.get(url)

        if response.status_code == 200:

            dna_sequence = response.text.split('\n', 1)[1].replace('\n', '')

            return dna_sequence

    @staticmethod
    def nucleotide_frequency(sequence):
        sequence = sequence.lower()
        total_caracteres = len(sequence)
        compteur_caracteres = {}

        for caractere in sequence:
            if caractere.isalpha():
                compteur_caracteres[caractere] = compteur_caracteres.get(caractere, 0) + 1

        proportions = {caractere: count / total_caracteres for caractere, count in compteur_caracteres.items()}

        return proportions
