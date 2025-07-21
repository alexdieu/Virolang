import networkx as nx
import random
from cellular_models.cell import Host
from cellular_models.simulation import simulate_within_host
from molecular_models.models import Virus, Genome

class Population:
    def __init__(self, name: str, size: int, verbose: bool = False):
        self.name = name
        self.graph = nx.erdos_renyi_graph(size, p=0.05)
        self.agents = {i: Host(name=f"agent_{i}") for i in range(size)}
        self.status = {i: "susceptible" for i in range(size)}
        self.history = []
        self.verbose = verbose
        self.base_transmissibility = 1.0

    def seed_infection(self, virus: Virus, num_infected: int = 1):
        if num_infected > len(self.agents):
            raise ValueError("Cannot infect more agents than exist in the population.")
        infected_nodes = random.sample(list(self.graph.nodes), num_infected)
        for node_id in infected_nodes:
            self.status[node_id] = "infected"
            self.agents[node_id].virus = virus

    def run_spread_cycle(self):
        newly_infected = {}
        for node_id, state in list(self.status.items()):
            if state == "infected":
                host_agent = self.agents[node_id]
                virus_to_spread = getattr(host_agent, 'virus', None)
                if not virus_to_spread or host_agent.is_lysed:
                    continue

                sim_result = simulate_within_host(virus_to_spread, host_agent)

                if self.verbose:
                    resources = {k: f"{v:.1f}" for k, v in host_agent.resources.items()}
                    genes = {k: f"{v:.2f}" for k, v in host_agent.gene_expression.items()}
                    print(f"  > Sim Report for Host '{host_agent.name}': "
                          f"Lysed={host_agent.is_lysed}, "
                          f"Resources={resources}, "
                          f"Genes={genes}")

                if sim_result["is_lysed"]:
                    self.status[node_id] = "dead"
                else:
                    self.status[node_id] = "recovered"
                    host_agent.memory_pool.append(hash(virus_to_spread.genome.sequence))

                if sim_result["evolved_virus"]:
                    virus_to_spread = sim_result["evolved_virus"]
                
                virus_to_spread.transmissibility = self.base_transmissibility

                for neighbor_id in self.graph.neighbors(node_id):
                    if self.status[neighbor_id] == "susceptible":
                        transmission_prob = virus_to_spread.transmissibility / (1 + self.graph.degree(node_id))
                        if random.random() < transmission_prob:
                            newly_infected[neighbor_id] = virus_to_spread
        
        for node_id, virus in newly_infected.items():
            self.status[node_id] = "infected"
            self.agents[node_id].virus = virus
        
        counts = {s: list(self.status.values()).count(s) for s in set(self.status.values())}
        self.history.append(counts)
        print(f"Cycle Results: {counts}")

    def calibrate(self, target_peak_infected: int):
        print(f"\n--- Calibrating model to target a peak of ~{target_peak_infected} infected agents ---")
        if target_peak_infected > len(self.agents):
            target_peak_infected = len(self.agents)

        for i in range(10):
            temp_pop = Population(self.name, len(self.agents), verbose=False)
            temp_pop.base_transmissibility = self.base_transmissibility
            
            calib_virus = Virus(name="calib_virus", genome=Genome(sequence="AUGUGA", type="ssRNA+", definition="calib"))
            temp_pop.seed_infection(calib_virus, 1)
            
            for _ in range(50):
                temp_pop.run_spread_cycle()
                # CORRECTED: Convert to list before calling .count()
                if not list(temp_pop.status.values()).count("infected"):
                    break
            
            peak_infected = max([h.get("infected", 0) for h in temp_pop.history], default=0)
            error = target_peak_infected - peak_infected
            
            print(f"  > Attempt {i+1}: Transmissibility={self.base_transmissibility:.3f}, Peak Infected={peak_infected}, Error={error}")

            if abs(error) < max(5, target_peak_infected * 0.1):
                print("--- Calibration successful! ---")
                return
            
            self.base_transmissibility += error * 0.005
            self.base_transmissibility = max(0.1, min(5.0, self.base_transmissibility))
        
        print("--- Calibration finished (may not have converged perfectly). ---")
