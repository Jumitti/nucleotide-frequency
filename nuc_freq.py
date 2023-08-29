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

from nucleotide_frequency import NCBIdna
from tqdm import tqdm

chraccver_human = ['NC_000001.11', 'NC_000002.12', 'NC_000003.12', 'NC_000004.12', 'NC_000005.10', 'NC_000006.12',
                   'NC_000007.14', 'NC_000008.11', 'NC_000009.12', 'NC_000010.11', 'NC_000011.10', 'NC_000012.12',
                   'NC_000013.11', 'NC_000014.9', 'NC_000015.10', 'NC_000016.10', 'NC_000017.11', 'NC_000018.10',
                   'NC_000019.10', 'NC_000020.11', 'NC_000021.9', 'NC_000022.11', 'NC_000023.11', 'NC_000024.10']

chraccver_test = ['NC_000024.10']

GRCh38 = []

for chraccver in chraccver_test:
    sequence = NCBIdna.get_chromosome_sequence(chraccver)
    ATGCseq = []
    i = sequence.lower().replace("b", "").replace("d", "").replace("e", "").replace("f", "").replace("h", "") \
        .replace("i", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "") \
        .replace("o", "").replace("p", "").replace("q", "").replace("r", "").replace("s", "").replace("u", "") \
        .replace("v", "").replace("w", "").replace("x", "").replace("y", "").replace("z", "")
    ATGCseq.append(i.upper())
    caractere_frequency = NCBIdna.nucleotide_frequency(ATGCseq)
    dna_sequence = f">{chraccver}\n{ATGCseq}\n"
    GRCh38.append(dna_sequence)
    print(GRCh38)
    print(f"{chraccver}: {caractere_frequency}")

fasta_filename = "GRCh38.fasta"

with open(fasta_filename, "w") as fasta_file:
    fasta_file.writelines(GRCh38)

with open('With N', "w") as fasta_file_2:
    fasta_file_2.writelines(sequence)

