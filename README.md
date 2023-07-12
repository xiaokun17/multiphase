
# Multiphase Fluid Project

## Introduction
This is a fluid dynamics simulation project that uses Python and the Taichi programming language. Different solvers can be employed for the simulation, and the program operates in GUI-free mode.

## Dependencies
1. Python: You need to have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).

2. Taichi Programming Language: This project uses Taichi for performing simulations. You can install it by running the following command:
```
pip install taichi
```

3. Other Dependencies: Please make sure to install other related dependencies as per the project requirements.

## Getting Started

### Running the Demo
To run the demo, execute the `main.py` file as follows:
```
python main.py
```

### Configuration
You can change the scenario for the demo by altering the `scenario_file_path` string in the `main.py` file.

Simulation configuration can be changed by modifying the file indicated by the `config_file_path`. Here, you can specify whether to use the CPU or GPU for running the simulation, decide on the solver for the simulation, and other relevant settings.

## Output
The program outputs data in three folders: `VFSPH`, `DFSPH`, and `JL21`, based on the solver used for the simulation.

Each folder contains the following sub-folders:

- `json`: Contains logs about the basic statistical data for each simulation frame.
- `part_data`: Contains the basic position and velocity data as `.npy` files for the fluid field.
- `ply`: Contains more specific multiphase information in `.ply` format.
