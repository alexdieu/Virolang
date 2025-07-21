# cellular_models/cell.py
from pydantic import BaseModel, Field
from typing import Optional
from molecular_models.models import Virus  # 1. ADD THIS IMPORT

class Host(BaseModel):
    name: str
    is_lysed: bool = False
    virus: Optional[Virus] = None  # 2. ADD THIS FIELD
    
    resources: dict[str, float] = Field(
        default_factory=lambda: {
            'ATP': 10000.0,
            'amino_acids': 5000.0,
            'nucleotides': 5000.0
        }
    )
    
    gene_expression: dict[str, float] = Field(
        default_factory=lambda: {
            'IFN_gene': 1.0,       # Interferon (antiviral alarm)
            'Receptor_gene': 1.0,  # e.g., ACE2
            'Apoptosis_gene': 0.1 # Programmed cell death
        }
    )
    
    memory_pool: list[str] = Field(default_factory=list, description="Hashes of encountered antigens")

    def check_resources(self, cost: dict) -> bool:
        return all(self.resources.get(k, 0) >= v for k, v in cost.items())

    def deplete_resources(self, cost: dict):
        for k, v in cost.items():
            self.resources[k] = max(0, self.resources[k] - v)

    def regulate_genes(self, viral_rna_load: float, viral_suppression_factor: float):
        # Host response
        self.gene_expression['IFN_gene'] += 0.005 * viral_rna_load
        self.gene_expression['Apoptosis_gene'] += 0.002 * viral_rna_load
        self.gene_expression['Receptor_gene'] -= 0.003 * viral_rna_load

        # Viral counter-response
        self.gene_expression['IFN_gene'] -= 0.01 * viral_suppression_factor

        # Clamp values between 0 and 2 for stability
        for k in self.gene_expression:
            self.gene_expression[k] = max(0, min(2, self.gene_expression[k]))

        # Check for apoptosis
        if self.gene_expression['Apoptosis_gene'] > 1.5:
            self.is_lysed = True
