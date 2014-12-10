# Import of required modules
import os, sys, stat, subprocess

# Source (this) Directory
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# Direcory containing AutoDockVina binaries - vina and vina_split
MAIN_DIR = os.path.join(SRC_DIR, "autodock_vina_bin")
OS_DIR = "win32" if "win32" == sys.platform else ("mac" if "darwin" == sys.platform else "linux_x86")
VINA_BIN_DIR = os.path.join(MAIN_DIR, OS_DIR)

# Executables' Path - vina and vina_split
VINA_EXE = os.path.join(VINA_BIN_DIR, "vina")
VINA_SPLIT_EXE = os.path.join(VINA_BIN_DIR, "vina_split")


def vina(
		lig_path, rec_path, flex_path, 
		center, size, output_dir, logfiles_dir=None,
		exhaustiveness = None, seed = None, 
		max_binding_modes = None, energy_range = None
	):
	
	# File names of the Receptor and Ligand
	receptor, ligand = os.path.basename(rec_path), os.path.basename(lig_path)

	# Receptor, Ligand, and Flexible Side Chains (if any)
	lig_arg = " --ligand " + lig_path
	rec_arg = " --receptor " + rec_path
	flex_arg = " --flex " + flex_path if flex_path else ""
	# INPUT ARGUMENTS
	input_args = lig_arg + rec_arg + flex_arg

	# Center co-ordinates of the Search Space
	center_x_arg = " --center_x " + center[0]
	center_y_arg = " --center_y " + center[1]
	center_z_arg = " --center_z " + center[2]
	center_args = center_x_arg + center_y_arg + center_z_arg
	# Size of the Search Space
	size_x_arg = " --size_x " + size[0]
	size_y_arg = " --size_y " + size[1]
	size_z_arg = " --size_z " + size[2]
	size_args = size_x_arg + size_y_arg + size_z_arg
	# SEARCH SPACE ARGUMENTS
	search_space_args = center_args + size_args

	# Output Receptor__Ligand Molecule, and Logfile
	if not logfiles_dir: logfiles_dir = output_dir
	outfile = os.path.join(output_dir, receptor.replace(".pdbqt", "__") + ligand)
	logfile = os.path.join(logfiles_dir, receptor.replace(".pdbqt", "__") + ligand.replace(".pdbqt", ".txt"))
	# OUTPUT ARGUMENTS
	output_args = " --out " + outfile + " --log " + logfile
	
	# Custom Seed, Exhaustiveness, Max. Binding Modes generated, Max. Energy diff. between generated modes
	# Vina Defaults: Random seed, Exhaustiveness = 8, Max. Binding Modes = 9, Max. Energy diff. = 3
	ex_arg = " --exhaustiveness " + exhaustiveness if exhaustiveness else ""
	seed_arg = " --seed " + seed if seed else ""
	mbm_arg = " --num_modes " + max_binding_modes if max_binding_modes else ""
	er_arg = " --energy_range " + energy_range if energy_range else ""
	# OPTIONAL ARGUMENTS
	optional_args = ex_arg + seed_arg + mbm_arg + er_arg

	# ALL ARGUMENTS
	vina_args = input_args + search_space_args + output_args + optional_args
	
	# SUBPROCESS CALL
	subprocess.call(VINA_EXE + vina_args, shell=True)


def vina_split(input_mol):
	pass

	# INPUT ARGUMENT
	# input_arg = " --input " + input_mol

	# SUBPROCESS CALL
	# subprocess.call(VINA_SPLIT_EXE + input_arg, shell=True)


# Doesn't belong here...
# def status_msg(receptor, ligand, start=True):
# 	if start:
# 		msg = "Running docking analysis on the receptor " + receptor + ", and ligand " + ligand + "..."
# 	else:
# 		msg = "Finished the docking analysis on the receptor " + receptor + ", and ligand " + ligand + "."
