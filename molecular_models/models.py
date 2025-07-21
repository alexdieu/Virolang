# molecular_models/models.py
from pydantic import BaseModel, Field, model_validator
from typing import Literal, Optional

class Genome(BaseModel):
    sequence: str = Field(..., min_length=3)
    type: Literal['ssRNA+', 'dsDNA', 'ssRNA-']
    definition: str

    # CORRECTED: Use a model_validator to check fields against each other
    @model_validator(mode='after')
    def check_sequence_and_type(self) -> 'Genome':
        seq = self.sequence.upper()
        genome_type = self.type

        is_rna = 'RNA' in genome_type
        
        # Check for 'T' in RNA sequences
        if is_rna and 'T' in seq:
            raise ValueError('RNA sequence cannot contain "T"')
        
        # Check for 'U' in DNA sequences
        if not is_rna and 'U' in seq:
            raise ValueError('DNA sequence cannot contain "U"')
        
        # Ensure the sequence is stored in uppercase
        self.sequence = seq
        return self

class Protein(BaseModel):
    sequence: str
    structure_path: Optional[str] = Field(None, description="Path to PDB file")
    
class Virus(BaseModel):
    name: str
    genome: Genome
    proteins: dict[str, Protein] = {}
    
    # Fitness metrics determined by simulation
    transmissibility: float = Field(1.0, description="Base transmission factor")
    virulence: float = Field(1.0, description="Factor affecting host cell damage")
    metabolic_efficiency: float = Field(1.0, description="Lower is better (less resource cost)")
    epigenetic_suppression: float = Field(0.0, description="Factor for suppressing host immune genes")
