# AMBER Scripts

This directory contains scripts and input files for running MixMD and dewetting simulations using AMBER and PLUMED.

## Folder Structure

- [Metadynamics](./Metadynamics)  
  Contains AMBER and PLUMED input files required to run dewetting simulations.

- [MixMD](./MixMD/)  
  Contains all files and scripts for setting up and running MixMD simulations. This folder has the following subdirectories:
  
  - [System_preparation](./MixMD/System_preparation/)  
    Files and scripts for preparing the MixMD simulation system.  
    **Workflow:**  
    1. Create a simulation box containing only probe molecules.  
    2. Equilibrate the probe box and extract an equilibrated frame.  
    3. Use `shell_leap.in` and then `solvate.in` to build the system.  
    4. Use `VbyV_check.py` to check the %v/v (volume/volume) of the probe to water.  
    5. Adjust the number of water molecules in `solvate.in` until the probe concentration reaches 5% v/v (probe/water).
  
  - [MD_run](./MixMD/MD_run/)  
    Contains AMBER scripts for running the MixMD production simulations.
  
  - [Probe_density_calc](./MixMD/MD_run/Probe_density_calc/)  
    Contains cpptraj input files for calculating probe density from the simulation trajectories.

## Usage

- Use the files in `System_preparation` to build MixMD system with the desired probe concentration.
- Run your MixMD simulations using the scripts in `MD_run`.
- Analyze probe densities using the cpptraj scripts in `Probe_density_calc`.
- For dewetting simulations, refer to the input files in the `Metadynamics` folder.

