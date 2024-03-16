import streamlit as st

st.write("# RNA INTO AMINO ACIDS CONVERTER")

def rna_to_amino_acid(rna_sequence):
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    print(len(rna_sequence))
    rna_sequence = rna_sequence.replace(" ","")
    print(len(rna_sequence))
    rna_sequence = rna_sequence.replace("T","U")

    update_seq = []
    counter = 1
    codon = ""
    for i in range(len(rna_sequence)):
        if rna_sequence[i] == '\n':
            continue
        codon = codon + rna_sequence[i]
        if counter == 3:
            update_seq.append(codon)
            codon = ""
            counter = 0
        counter = counter + 1
    
    
    amino_acid_sequence = []
    for i in update_seq:
        codon = i
        amino_acid = codon_table.get(codon, '')
        amino_acid_sequence.append(amino_acid)

    return ''.join(amino_acid_sequence).rstrip("*")

def rna_to_dna(rna_seq):
    dna = rna_seq.replace(" ","").replace("U","T")
    return dna
    
def dna_to_rna(dna_seq):
    rna = dna_seq.replace(" ","").replace("T","U")
    return rna


input1 = st.text_area('Enter the DNA or RNA sequence',height=300,placeholder='e.g ATGAAGCTCTTCATCTTCACC ')
mol = st.radio("Convert To: ",["DNA","RNA","PROTEIN"],captions=["DNA","RNA","PROTEIN"])
if mol == "PROTEIN":
    aa_seq = rna_to_amino_acid(input1)
    st.write('## Output ')

    st.write("### Protein Molecule")
    st.write(aa_seq)
elif mol == "DNA":
    dna = rna_to_dna(input1)
    st.write('## Output ')

    st.write("### DNA Molecule")
    st.write(dna)
else:
    rna = dna_to_rna(input1)
    st.write('## Output ')
    
    st.write("### RNA Molecule")
    st.write(rna)
