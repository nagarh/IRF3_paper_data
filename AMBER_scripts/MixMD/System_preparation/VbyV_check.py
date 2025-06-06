import argparse
import numpy as np

####################################################################################
#To run this code use " python VbyV_check.py --pdb 'input .pdb solavted file name' "
#####################################################################################


# Molecular weights and densities of probes and water
probe_data = {
    'C3N': (0.777, 41.05),
    'EOH': (0.789, 46.07),
    'IMI': (1.0303, 68.08),
    'IPA': (0.7809, 60.01),
    '1P3': (1.016, 80.09),
    'NMA': (0.9371, 73.09)
}
water_data = (1.0, 18.015)  # Density and molecular weight of water

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Calculate the ratio R for a probe in a PDB file.')
parser.add_argument('-p', '--pdb', type=str, help='PDB file name')
#parser.add_argument('--dim', type=float, nargs=3, help='Dimensions: Lx Ly Lz')
args = parser.parse_args()

# Check if the file name is provided
if not args.pdb:
    parser.error('Please provide the PDB file name using -p or --pdb argument.')
#if not args.dim:
    #parser.error('Please provide the dimensions using --dim argument.')

# File name and path
file_path = args.pdb

# Dimensions
#Lx, Ly, Lz = args.dim

# File name and path
#file_path = '1qwt_shell_solvated.pdb'

# Read file content
with open(file_path, 'r') as file:
    content = file.readlines()

# Initialize counters
#N_probe = 0
#N_water = 0

probe_count = 0
water_count = 0
in_probe_section = False
in_water_section = False

for line in content:
    if line.startswith('TER'):
        if in_probe_section:
            probe_count += 1
            in_probe_section = False
        elif in_water_section:
            water_count += 1
            in_water_section = False
    elif line.startswith('ATOM') or line.startswith('HETATM'):
        atom_name = line[17:20].strip()
        if atom_name in probe_data:
            probe_name = atom_name
            in_probe_section = True
        elif atom_name == 'WAT':
            in_water_section = True

#print(probe_count)
#print(water_count)

# Iterate over each line in the content
#for line in content:
#    if line.startswith('ATOM') or line.startswith('HETATM'):
#        atom_name = line[17:20].strip()
#        #print(atom_name)
#        if atom_name in probe_data:
#            probe_name=atom_name
#            N_probe += 1
#        elif atom_name == 'WAT':
#            N_water += 1

#print(N_probe)
#print(N_water)
# Calculate the ratio R
rho_water, Mw_water = water_data
#print(water_data)
#print(rho_water)
#print(Mw_water)
#print(probe_data[probe_name][1])
#print(probe_data[probe_name][0])

R = (probe_count / water_count) * (probe_data[probe_name][1] / Mw_water) * (rho_water / probe_data[probe_name][0])
R_perct= R*100

#V_manual = Lx*Ly*Lz
N_water_actual= 20 *(probe_count) * (probe_data[probe_name][1] / Mw_water) * (rho_water / probe_data[probe_name][0])
#V_actual=(water_count/N_water_actual)*V_manual
#L= np.ceil(np.cbrt(V_actual))
#Print the values
print("*************** Information of syatem ***************")
print(f"The probe name in the .pdb file is: {probe_name}")
print(f"density(g/cm3) of the probe is: {probe_data[probe_name][0]}")
print(f"Moleculr weight(g/mol) of the probe is: {probe_data[probe_name][1]}")
print(f"density(g/cm3) of the water is: {rho_water}")
print(f"Molecular weight (g/mol) of the water is: {Mw_water}")
print(f"No of probes in the .pdb file is: {probe_count}")
print(f"No of water molecules in the .pdb file is: {water_count}")
print(f"No of water molecules required for 5%v/v : {N_water_actual}")
#print(f"Manual volume of the box : {V_manual}")
#print(f"Actual volume required to achieve 5%v/v : {V_actual}")
#print(f"Dimension required to achieve 5%v/v : {L} {L} {L}")

print("*************** Final Result ***************")
print(f"The calculated ratio %v/v of probe to water is: {R_perct:.3f}")
