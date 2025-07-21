# Virolang 🧬

**A multi-scale, research-grade simulator for viral evolution and epidemiology, powered by a custom Domain-Specific Language (DSL).**

---

![Virolang GUI in Action]()

## About The Project

Virolang is a sophisticated simulation framework designed to model the complex dynamics of viral outbreaks from the molecular level to the entire population. Unlike traditional models that use static parameters, Virolang simulates the real-time evolution of new viral variants within individual hosts and tracks their competition and spread through a networked population.

The entire simulation is controlled by **Virolang**, a simple yet powerful scripting language designed specifically for setting up and running complex virological and epidemiological scenarios.

### Key Features ✨

* **Multi-Scale Modeling:** Simulates everything from the within-host battle for cellular resources to the between-host spread in a population.
* **Domain-Specific Language (DSL):** Use the intuitive Virolang (`.vl`) scripting language to define viruses, create populations, and run experiments.
* **Real-Time Viral Evolution:** The "Grand Feedback Loop" allows new variants with different traits (transmissibility, virulence) to emerge during the simulation and compete for dominance.
* **Data-Driven Simulation:** Load real-world viral genomes directly from the NCBI GenBank database (e.g., SARS-CoV-2, Ebola).
* **Automatic Calibration:** Automatically tunes simulation parameters (like transmissibility) to match user-defined targets for realistic outbreak severity.
* **Detailed Within-Host Dynamics:** Models cellular resource depletion (ATP, nucleotides), epigenetic warfare (gene expression changes), and stochastic effects (Gillespie algorithm).
* **Graphical Interface & Visualization:** A user-friendly GUI to run simulations and a built-in plotting feature to visualize the results of the outbreak (SIR curves).

## Architecture Overview

The project is built with a modular and extensible Python architecture:

* **`parser/`**: The ANTLR-based two-pass compiler (Lexer, Parser, Visitors) for the Virolang DSL.
* **`molecular_models/`**: Pydantic models for biological entities (`Virus`, `Genome`) and functions for handling real-world data and molecular interactions.
* **`cellular_models/`**: The within-host simulation engine, modeling the cell environment, resources, and immune responses.
* **`population_models/`**: The agent-based population model using `NetworkX` to simulate the spread of the virus between hosts.
* **`main.py`**: The main application entry point with the Tkinter-based graphical user interface.

## Getting Started

Follow these steps to get the simulator running on your local machine.

### Prerequisites

* Python 3.10+
* Java Development Kit (JDK) (for running ANTLR)
* The ANTLR v4 JAR tool. Download `antlr-4.x.x-complete.jar` from [antlr.org](https://www.antlr.org/download.html).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your_username/Virolang.git](https://github.com/your_username/Virolang.git)
    cd Virolang
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Generate the ANTLR Parser:** *Optional*
    Run the included bash script. **Remember to install** ANTLR4 on your computer.
    ```bash
    chmod +x regenerate_parser.sh
    ./regenerate_parser.sh
    ```

### Usage

Launch the graphical user interface by running `main.py`:

```bash
python main.py
```

1.  Click **"Browse..."** to select a Virolang script (e.g., `test_sars_paris.vl`).
2.  Enter your **email address** (required for fetching data from NCBI).
3.  Click **"Run Simulation"**.
4.  View the text output in the **"Console Output"** tab and the final epidemic curve in the **"Results Plot"** tab.

## The Virolang Language

Control the simulator by writing simple `.vl` scripts. Here are the core commands:

* **Load a Real Virus:**
    ```virolang
    // Loads the SARS-CoV-2 reference genome from NCBI
    SARS_CoV_2 = load_genome(id: "NC_045512.2");
    ```

* **Create a Population:**
    ```virolang
    // Creates a population of 1,000 agents with verbose logging
    Paris = create population(name: "Paris", size: 1000, verbose: true);
    ```

* **Calibrate the Model:**
    ```virolang
    // Runs test simulations to tune the model to a specific severity
    CalibratedParis = Paris calibrate(target_peak_infected: 250);
    ```

* **Run an Infection:**
    ```virolang
    // Unleashes the virus on the population using the '!' operator
    ParisOutbreakReport = SARS_CoV_2 ! CalibratedParis;
    ```

## Roadmap

* [ ] Implement full genetic-level mutation and protein re-folding.
* [ ] Integrate a more advanced MCMC-based calibration method.
* [ ] Add support for different network graph types (e.g., scale-free, small-world).
* [ ] Develop a web-based interface for running simulations and viewing results.

## License

Copyright (c) 2025 [Alexandre Divol]. All Rights Reserved.
