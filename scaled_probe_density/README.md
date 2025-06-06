# Scaled Probe Density Maps

This directory contains the scaled probe density data of probes from MixMD simulations of the IRF3 protein.

## Description

In the MixMD simulations, the IRF3 protein chain is simulated in the presence of different probe molecules. The goal is to identify regions on the protein surface where the probes accumulate, which may indicate potential binding sites.

The entire simulation box is divided into grids with a resolution of 0.5 Å. For each voxel in the grid, the average occupancy of probe molecules is determined. A normalized density, $\zeta$, is then calculated for each voxel as:  
$$
\zeta = \frac{x - \mu}{\sigma}
$$

where:
- $x$ is the ensemble-averaged occupancy in the voxel,
- $\mu$ is the mean occupancy across all voxels,
- $\sigma$ is the standard deviation of occupancy across all voxels.

The occupancy of a voxel is defined as the fraction of all simulation configurations in which the center of a heavy atom of a probe molecule lies inside the voxel.

Contour maps of constant $\zeta$ are generated to visualize regions on the protein surface where probe molecules accumulate. A region where four or more probes accumulate is classified as a potential binding site (BS).

## Usage

You can use the provided Python scripts ([`load_all_outer_protein.py`](load_all_outer_protein.py)) to load and visualize these probe density maps in PyMOL.

## Files

- **Density data files:** Scaled probe density maps for different probes.
- **Visualization script:** Python scripts for rendering protein structures and overlaying probe density isomeshes in PyMOL.
- **CPPTRAJ scripts:** Scripts for calculating the density of probes are available [here](../AMBER_scripts/MixMD/MD_run/Probe_density_calc)

## Requirements

- [PyMOL](https://pymol.org/) (for visualization)
- Python 3.x (for running visualization scripts)
