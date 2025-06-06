# Dewetting/Wetting Data

This directory contains CSV files with dewetting/wetting analysis data from metadynamics simulations of the IRF3 protein. Each file corresponds to a specific coordination number (CN) window, as indicated in the filename (e.g., `biased_simulation_CN_1062_1092_water_molecules_all_residues.csv` contains data for frames with CN in the 1062–1092 range).

## File Format

Each CSV file contains the following columns:

- **Res_number**: Residue number of the IRF3 protein.
- **frame_\***: Each column labeled `frame_*` corresponds to a PDB frame extracted from the simulation trajectory with a coordination number in the specified range. The values under these columns represent the number of water molecules within 4 Å of the given residue in that frame.
- **Average**: The average number of water molecules within 4 Å of the residue across all `frame_*` PDB files.
- **StdDev**: The standard deviation of the number of water molecules within 4 Å of the residue across all `frame_*` PDB files.

## Example

| Res_number | frame_... | ... | Average | StdDev |
|------------|-----------|-----|---------|--------|
| 1          | 0         | ... | 1.39    | 0.97   |
| 2          | 10        | ... | 11.35   | 2.19   |
| ...        | ...       | ... | ...     | ...    |

- Each row corresponds to a residue.
- Each value under a `frame_*` column is the count of water molecules within 4 Å of that residue in the corresponding frame.

## Usage

These files can be used to analyze the hydration environment of each residue in IRF3 under different coordination number conditions, helping to identify regions of dewetting or wetting during the simulation.

## Related

- See [README.md](../README.md) for an overview of the project and folder structure.
