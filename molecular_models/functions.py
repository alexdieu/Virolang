# molecular_models/functions.py
import random
import subprocess
import numpy as np
from Bio.Seq import Seq
from Bio import Entrez, SeqIO # ADDED
from Bio.Data.CodonTable import standard_rna_table
from data.codon_bias import HUMAN_CODON_BIAS

def fetch_genome_from_ncbi(accession_id: str, email: str) -> SeqIO.SeqRecord:
    """Fetches a full GenBank record from NCBI."""
    print(f"--- [NCBI] Fetching record '{accession_id}' ---")
    Entrez.email = email
    try:
        handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="gb", retmode="text")
        record = SeqIO.read(handle, "genbank")
        handle.close()
        return record
    except Exception as e:
        raise ConnectionError(f"Failed to fetch from NCBI: {e}")

def predict_structure_placeholder(protein_sequence: str, out_dir: str = "output") -> str:
    print(f"--- [TOOL CALL] Simulating AlphaFold prediction for sequence of length {len(protein_sequence)} ---")
    # In a real implementation, this would call AlphaFold's run_docker.py script.
    # For now, we just create a placeholder file.
    file_path = f"{out_dir}/predicted_structure.pdb"
    with open(file_path, "w") as f:
        f.write("REMARK 350 PLACEHOLDER PDB FILE\n")
    return file_path

def dock_binding_placeholder(receptor_pdb: str, ligand_pdb: str) -> float:
    print(f"--- [TOOL CALL] Simulating AutoDock Vina docking of {receptor_pdb} and {ligand_pdb} ---")
    # This would call AutoDock Vina and parse the output log for the binding affinity.
    # We return a random, favorable binding energy (in kcal/mol).
    return random.uniform(-12.0, -7.0)

def approximate_dynamics(static_dg: float, num_conformers: int = 10, std_dev: float = 1.5) -> float:
    """Approximates the effect of protein dynamics on binding energy."""
    dynamic_dgs = np.random.normal(static_dg, std_dev, num_conformers)
    return np.mean(dynamic_dgs)

def optimized_reverse_translate(protein_seq: str, host_bias: dict = HUMAN_CODON_BIAS) -> Seq:
    """Translates a protein sequence back to RNA using host codon bias."""
    rna_sequence = []
    aa_to_codons = {}
    for codon, aa in standard_rna_table.forward_table.items():
        if aa not in aa_to_codons:
            aa_to_codons[aa] = []
        aa_to_codons[aa].append(codon)

    for aa in protein_seq:
        if aa == '*': # Stop codon
            codons = standard_rna_table.stop_codons
        else:
            codons = aa_to_codons.get(aa, [])
        
        if not codons:
            continue

        weights = [host_bias.get(c, 0.1) for c in codons]
        chosen_codon = random.choices(codons, weights=weights, k=1)[0]
        rna_sequence.append(chosen_codon)
        
    return Seq("".join(rna_sequence))
