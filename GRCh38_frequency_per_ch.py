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

# chraccver_test = ['NC_000024.10']

GRCh38 = []
frequency_GRCh38 = ['Chraccver A T G C\n']
for chraccver in tqdm(chraccver_human, desc='Calculate...'):
    sequence = NCBIdna.get_chromosome_sequence(chraccver)

    i = sequence.replace("b", "").replace("d", "").replace("e", "").replace("f", "").replace("h", "") \
        .replace("i", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "") \
        .replace("o", "").replace("p", "").replace("q", "").replace("r", "").replace("s", "").replace("u", "") \
        .replace("v", "").replace("w", "").replace("x", "").replace("y", "").replace("z", "")

    proportions, proportions_output = NCBIdna.nucleotide_frequency(i.upper())

    GRCh38.append(f">{chraccver}\n{i}\n\n")
    frequency_GRCh38.append(f"{chraccver} {proportions_output}\n")

GRCh38_fasta = "GRCh38.txt"
frequency_GRCh38_fasta = "GRCh38_frequency.txt"
with open(GRCh38_fasta, "w") as fasta_file:
    fasta_file.writelines(GRCh38)
with open(frequency_GRCh38_fasta, "w") as fasta_file:
    fasta_file.writelines(frequency_GRCh38)
