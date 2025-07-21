# cellular_models/simulation.py
import numpy as np
from scipy.integrate import odeint
from .cell import Host
from molecular_models.models import Virus
import random

REPLICATION_COST = {'ATP': 10.0, 'nucleotides': 4.0}
TRANSLATION_COST = {'ATP': 5.0, 'amino_acids': 1.0}

def gillespie_stochastic(reactions: list, initial_state: dict, cell: Host, max_time: int):
    state = initial_state.copy()
    time = 0
    history = [(0, state.copy())]

    while time < max_time and not cell.is_lysed:
        # Dynamic gene regulation and RNAi defense
        cell.regulate_genes(state.get('RNA', 0), state.get('Protein', 0))
        if np.random.random() < 0.1 * cell.gene_expression['IFN_gene']:
            state['RNA'] = max(0, state['RNA'] * 0.95) # RNAi degradation

        # Calculate reaction rates
        rates = [r['rate_func'](state, cell) for r in reactions]
        total_rate = sum(rates)
        if total_rate == 0: break

        # Advance time
        time += np.random.exponential(1 / total_rate)
        if time > max_time: break

        # Choose and execute reaction
        rxn_idx = np.random.choice(len(reactions), p=np.array(rates) / total_rate)
        rxn = reactions[rxn_idx]

        if cell.check_resources(rxn['cost']):
            rxn['update_func'](state, cell)
            cell.deplete_resources(rxn['cost'])
        else:
            # Under stress, increase mutation chance
            if np.random.random() < 0.2:
                # Placeholder for a mutation event that generates a new virus variant
                pass

        history.append((time, state.copy()))

    return history

def cytokine_model_ode(c, t, viral_load, virulence, cell):
    """ODE for cytokine levels."""
    energy_factor = cell.resources['ATP'] / 10000.0
    dc_dt = (0.1 * viral_load * virulence * energy_factor) - (0.05 * c)
    return dc_dt

def simulate_within_host(virus: Virus, host: Host) -> dict:
    print(f"--- Simulating infection of host '{host.name}' with virus '{virus.name}' ---")
    
    initial_state = {'RNA': 1, 'Protein': 0}
    
    reactions = [
        {
            'rate_func': lambda s, c: (0.1 * s['RNA']) * (c.resources['ATP'] / 10000.0),
            'update_func': lambda s, c: s.update({'RNA': s.get('RNA', 0) + 1}),
            'cost': REPLICATION_COST
        },
        {
            'rate_func': lambda s, c: (0.05 * s['RNA']) * (c.resources['amino_acids'] / 5000.0),
            'update_func': lambda s, c: s.update({'Protein': s.get('Protein', 0) + 1}),
            'cost': TRANSLATION_COST
        }
    ]
    
    history = gillespie_stochastic(reactions, initial_state, host, max_time=24) # 24-hour simulation
    
    final_state = history[-1][1]
    peak_viral_load = max(h[1].get('RNA', 0) for h in history)
    
    # Simple logic for evolved virus placeholder
    evolved_virus = None
    if host.is_lysed or np.random.random() < 0.05: # Chance to evolve a new strain
        evolved_virus = virus.copy(deep=True)
        evolved_virus.name = f"{virus.name}_v{random.randint(2, 9)}"
        # Tweak properties based on simulation outcome
        evolved_virus.virulence *= (1 + (peak_viral_load / 1000))
        evolved_virus.transmissibility *= (1 - (host.resources['ATP'] / 10000.0))
        print(f"--- New variant '{evolved_virus.name}' emerged! ---")

    return {
        "was_successful": peak_viral_load > 10,
        "is_lysed": host.is_lysed,
        "evolved_virus": evolved_virus
    }
