# tests/test_models.py
import pytest
from pydantic import ValidationError
from molecular_models.models import Genome
from cellular_models.cell import Host

def test_genome_validation_success():
    Genome(sequence="AUGUAC", type="ssRNA+", definition="test RNA")
    Genome(sequence="ATGTAC", type="dsDNA", definition="test DNA")

def test_genome_validation_fails():
    with pytest.raises(ValidationError):
        # DNA with 'U'
        Genome(sequence="AUGUAC", type="dsDNA", definition="bad DNA")
    with pytest.raises(ValidationError):
        # RNA with 'T'
        Genome(sequence="ATGTAC", type="ssRNA+", definition="bad RNA")

def test_host_resource_depletion():
    host = Host(name="test_host")
    initial_atp = host.resources['ATP']
    cost = {'ATP': 100}
    
    assert host.check_resources(cost) is True
    host.deplete_resources(cost)
    assert host.resources['ATP'] == initial_atp - 100

def test_host_resource_check_fails():
    host = Host(name="test_host")
    cost = {'ATP': 20000} # More than available
    assert host.check_resources(cost) is False
