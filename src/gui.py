#!/usr/bin/env python3

try:
	from tkinter import *
	from tkinter import ttk
	from tkinter import filedialog as tkFileDialog
	from tkinter import messagebox as tkMessageBox
except ImportError: # Python 2
	from Tkinter import *
	import ttk
	import tkFileDialog
	import tkMessageBox

from vina import *
import os


root = Tk()
root.title("VinaGUI 1.0")
notebook_ui = ttk.Notebook(root)
inputs_frame = ttk.Frame(notebook_ui)
vina_frame = ttk.Frame(notebook_ui)


# ------------------------------------------------------------------------------------
# RECEPTOR INPUTS
# ------------------------------------------------------------------------------------

# helper functions for browsing receptor, and flex. side chains files
def browse_receptors():
	filepath = tkFileDialog.askopenfilename()
	receptor_path.set(filepath)
def browse_flexchains():
	filepath = tkFileDialog.askopenfilename()
	flexchain_path.set(filepath)

# frame for everything related to receptor input(s)
receptor_input_frame = ttk.Labelframe(inputs_frame, text="Receptor Input(s)")
receptor_input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NEWS")

# receptor
receptor_path = StringVar()
receptor_textbox_label = ttk.Label(receptor_input_frame, text="Receptor File", width=25)
receptor_textbox = ttk.Entry(receptor_input_frame, textvariable=receptor_path, width=40)
receptor_browse_button = ttk.Button(receptor_input_frame, text="Browse",command=browse_receptors, width=20)

receptor_textbox_label.grid(row=1, column=0, sticky="NEWS", padx=2.5, pady=2.5)
receptor_textbox.grid(row=1, column=1, sticky="NEWS", padx=2.5, pady=2.5)
receptor_browse_button.grid(row=1, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# flex side chains
flexchain_path = StringVar()
flexchain_textbox_label = ttk.Label(receptor_input_frame, text="Flex. File (if any)", width=25)
flexchain_textbox = ttk.Entry(receptor_input_frame, textvariable=flexchain_path, width=40)
flexchain_browse_button = ttk.Button(receptor_input_frame, text="Browse",command=browse_flexchains, width=20)

flexchain_textbox_label.grid(row=2, column=0, sticky="NEWS", padx=2.5, pady=2.5)
flexchain_textbox.grid(row=2, column=1, sticky="NEWS", padx=2.5, pady=2.5)
flexchain_browse_button.grid(row=2, column=2, sticky="NEWS", padx=2.5, pady=2.5)

def flexchain_check():
	if flexchain_check_var.get():
		flexchain_textbox.config(state=NORMAL)
		flexchain_browse_button.config(state=NORMAL)
	else:
		flexchain_path.set("")
		flexchain_textbox.config(state=DISABLED)
		flexchain_browse_button.config(state=DISABLED)
# checkbox for determining whether there is a flex file
flexchain_check_var = IntVar()
flexchain_cb = ttk.Checkbutton(receptor_input_frame, text="Flex. File?", variable=flexchain_check_var, command=flexchain_check)
flexchain_textbox.config(state=DISABLED); flexchain_browse_button.config(state=DISABLED)
flexchain_cb.grid(row=3, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# RECEPTOR SEARCH SPACE INPUTS
# ------------------------------------------------------------------------------------

# frame for everything related to receptor search space input(s)
receptor_ss_input_frame = ttk.Labelframe(inputs_frame, text="Receptor Search Grid")
receptor_ss_input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NEWS")

# search space co-ordinates
search_space_coord_frame = ttk.Frame(receptor_ss_input_frame)
search_space_coord_x_label = ttk.Label(search_space_coord_frame, text="x", anchor=CENTER, width=12)
search_space_coord_y_label = ttk.Label(search_space_coord_frame, text="y", anchor=CENTER, width=12)
search_space_coord_z_label = ttk.Label(search_space_coord_frame, text="z", anchor=CENTER, width=12)
search_space_coord_x_label.pack(side=LEFT, padx=2.5, pady=2.5)
search_space_coord_y_label.pack(side=LEFT, padx=2.5, pady=2.5)
search_space_coord_z_label.pack(side=LEFT, padx=2.5, pady=2.5)
search_space_coord_frame.grid(row=5, column=1, sticky="NEWS")

ss_center_x, ss_center_y, ss_center_z = StringVar(), StringVar(), StringVar()
search_space_center_label = ttk.Label(receptor_ss_input_frame, text="Search Space's CENTER", width=25)
ss_center_frame = ttk.Frame(receptor_ss_input_frame)
ss_center_x_textbox = ttk.Entry(ss_center_frame, textvariable=ss_center_x, width=12)
ss_center_y_textbox = ttk.Entry(ss_center_frame, textvariable=ss_center_y, width=12)
ss_center_z_textbox = ttk.Entry(ss_center_frame, textvariable=ss_center_z, width=12)
ss_center_x_textbox.pack(side=LEFT, padx=2.5, pady=2.5)
ss_center_y_textbox.pack(side=LEFT, padx=2.5, pady=2.5)
ss_center_z_textbox.pack(side=LEFT, padx=2.5, pady=2.5)
search_space_center_label.grid(row=6, column=0, sticky="NEWS", padx=2.5, pady=2.5)
ss_center_frame.grid(row=6, column=1, sticky="NEWS")
ss_center_eg_label = ttk.Label(receptor_ss_input_frame, text="Random e.g.: -2, -6, 35")
ss_center_eg_label.grid(row=6, column=2, sticky="NEWS", padx=2.5, pady=2.5)

ss_size_x, ss_size_y, ss_size_z = StringVar(), StringVar(), StringVar()
ss_size_label = ttk.Label(receptor_ss_input_frame, text="Search Space's SIZE", width=25)
ss_size_frame = ttk.Frame(receptor_ss_input_frame)
ss_size_x_textbox = ttk.Entry(ss_size_frame, textvariable=ss_size_x, width=12)
ss_size_y_textbox = ttk.Entry(ss_size_frame, textvariable=ss_size_y, width=12)
ss_size_z_textbox = ttk.Entry(ss_size_frame, textvariable=ss_size_z, width=12)
ss_size_x_textbox.pack(side=LEFT, padx=2.5, pady=2.5)
ss_size_y_textbox.pack(side=LEFT, padx=2.5, pady=2.5)
ss_size_z_textbox.pack(side=LEFT, padx=2.5, pady=2.5)
ss_size_label.grid(row=7, column=0, sticky="NEWS", padx=2.5, pady=2.5)
ss_size_frame.grid(row=7, column=1, sticky="NEWS")
ss_size_eg_label = ttk.Label(receptor_ss_input_frame, text="Random e.g.: 22, 24, 26")
ss_size_eg_label.grid(row=7, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# LIGAND INPUTS
# ------------------------------------------------------------------------------------

# helper functions for browsing ligand files, and directories
def browse_ligands():
	filepath = tkFileDialog.askopenfilename()
	ligand_path.set(filepath)
def browse_ligands_dir():
	dirpath = tkFileDialog.askdirectory()
	ligand_path.set(dirpath)

# frame for everything related to ligand input(s)
ligand_input_frame = ttk.Labelframe(inputs_frame, text="Ligand Input(s)")
ligand_input_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NEWS")

# for browsing ligand/ligands' dir.
ligand_path = StringVar()
ligand_textbox_label = ttk.Label(ligand_input_frame, text="Ligands' Directory", width=25)
ligand_textbox = ttk.Entry(ligand_input_frame, textvariable=ligand_path, width=40)
ligand_browse_button = ttk.Button(ligand_input_frame, text="Browse", command=browse_ligands_dir, width=20)

def multiple_ligands_toggle():
	if ml_var.get():
		ligand_textbox_label.config(text="Ligands' Directory")
		ligand_path.set("")
		ligand_browse_button.config(command=browse_ligands_dir)
	else:
		ligand_textbox_label.config(text="Ligand File")
		ligand_path.set("")
		ligand_browse_button.config(command=browse_ligands)
# checkbox for determining whether there is a single ligand or multiple ones to run analysis on
ml_var = IntVar()
multiple_ligands_cb = ttk.Checkbutton(ligand_input_frame, text="Multiple Ligands?", variable=ml_var, command=multiple_ligands_toggle)
ml_var.set('1')

ligand_textbox_label.grid(row=0, column=0, sticky="NEWS", padx=2.5, pady=2.5)
ligand_textbox.grid(row=0, column=1, sticky="NEWS", padx=2.5, pady=2.5)
ligand_browse_button.grid(row=0, column=2, sticky="NEWS", padx=2.5, pady=2.5)
multiple_ligands_cb.grid(row=1, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# OPTIONAL INPUTS
# ------------------------------------------------------------------------------------

# frame for everything related to optional input(s)
optional_inputs_frame = ttk.Labelframe(inputs_frame, text="Optional Input(s)")
optional_inputs_frame.grid(row=3, column=0, padx=10, pady=10, sticky="NEWS")

# following check buttons are for determining whether if the user wants to give a different input from the default one

# exhaustiveness
exhaustiveness_var = StringVar()
exhaustiveness_textbox_label = ttk.Label(optional_inputs_frame, text="Exhaustiveness", width=25)
exhaustiveness_textbox = ttk.Entry(optional_inputs_frame, textvariable=exhaustiveness_var, width=40)
def exhaustiveness_default_toggle():
	if exhaustiveness_default_var.get():
		exhaustiveness_textbox.config(state=DISABLED)
	else:
		exhaustiveness_textbox.config(state=NORMAL)
exhaustiveness_default_var = IntVar()
exhaustiveness_default_cb = ttk.Checkbutton(optional_inputs_frame, text="Default (8)", variable=exhaustiveness_default_var, command=exhaustiveness_default_toggle)
exhaustiveness_default_var.set('1'); exhaustiveness_textbox.config(state=DISABLED)

exhaustiveness_textbox_label.grid(row=0, column=0, sticky="NEWS", padx=2.5, pady=2.5)
exhaustiveness_textbox.grid(row=0, column=1, sticky="NEWS", padx=2.5, pady=2.5)
exhaustiveness_default_cb.grid(row=0, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# seed
seed_var = StringVar()
seed_textbox_label = ttk.Label(optional_inputs_frame, text="Seed", width=25)
seed_textbox = ttk.Entry(optional_inputs_frame, textvariable=seed_var, width=40)
def seed_default_toggle():
	if seed_default_var.get():
		seed_textbox.config(state=DISABLED)
	else:
		seed_textbox.config(state=NORMAL)
seed_default_var = IntVar()
seed_default_cb = ttk.Checkbutton(optional_inputs_frame, text="Default (Random)", variable=seed_default_var, command=seed_default_toggle)
seed_default_var.set('1'); seed_textbox.config(state=DISABLED)

seed_textbox_label.grid(row=1, column=0, sticky="NEWS", padx=2.5, pady=2.5)
seed_textbox.grid(row=1, column=1, sticky="NEWS", padx=2.5, pady=2.5)
seed_default_cb.grid(row=1, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# max binding modes
maxbindingmodes_var = StringVar()
maxbindingmodes_textbox_label = ttk.Label(optional_inputs_frame, text="Max. Binding Modes", width=25)
maxbindingmodes_textbox = ttk.Entry(optional_inputs_frame, textvariable=maxbindingmodes_var, width=40)
def maxbindingmodes_default_toggle():
	if maxbindingmodes_default_var.get():
		maxbindingmodes_textbox.config(state=DISABLED)
	else:
		maxbindingmodes_textbox.config(state=NORMAL)
maxbindingmodes_default_var = IntVar()
maxbindingmodes_default_cb = ttk.Checkbutton(optional_inputs_frame, text="Default (9)", variable=maxbindingmodes_default_var, command=maxbindingmodes_default_toggle)
maxbindingmodes_default_var.set('1'); maxbindingmodes_textbox.config(state=DISABLED)

maxbindingmodes_textbox_label.grid(row=2, column=0, sticky="NEWS", padx=2.5, pady=2.5)
maxbindingmodes_textbox.grid(row=2, column=1, sticky="NEWS", padx=2.5, pady=2.5)
maxbindingmodes_default_cb.grid(row=2, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# energy range
energyrange_var = StringVar()
energyrange_textbox_label = ttk.Label(optional_inputs_frame, text="Max. Energy Diff.", width=25)
energyrange_textbox = ttk.Entry(optional_inputs_frame, textvariable=energyrange_var, width=40)
def energyrange_default_toggle():
	if energyrange_default_var.get():
		energyrange_textbox.config(state=DISABLED)
	else:
		energyrange_textbox.config(state=NORMAL)
energyrange_default_var = IntVar()
energyrange_default_cb = ttk.Checkbutton(optional_inputs_frame, text="Default (3 kcal/mol)", variable=energyrange_default_var, command=energyrange_default_toggle)
energyrange_default_var.set('1'); energyrange_textbox.config(state=DISABLED)

energyrange_textbox_label.grid(row=3, column=0, sticky="NEWS", padx=2.5, pady=2.5)
energyrange_textbox.grid(row=3, column=1, sticky="NEWS", padx=2.5, pady=2.5)
energyrange_default_cb.grid(row=3, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# OUTPUT INFO.
# ------------------------------------------------------------------------------------

# frame for everything related to output
output_values_frame = ttk.Labelframe(inputs_frame, text="Output Info.")
output_values_frame.grid(row=4, column=0, padx=10, pady=10, sticky="NEWS")

# helper functions for browsing output directories
def browse_output_dir():
	dirpath = tkFileDialog.askdirectory()
	output_path.set(dirpath)
	if not diff_logdir_var.get():
		logfiles_path.set(dirpath)
def browse_logfiles_dir():
	dirpath = tkFileDialog.askdirectory()
	logfiles_path.set(dirpath)

output_path, logfiles_path = StringVar(), StringVar()
output_textbox_label = ttk.Label(output_values_frame, text="Output(s') Directory", width=25)
output_textbox = ttk.Entry(output_values_frame, textvariable=output_path, width=40)
output_browse_button = ttk.Button(output_values_frame, text="Browse", command=browse_output_dir, width=20)
logfiles_textbox_label = ttk.Label(output_values_frame, text="Logfile(s') Directory", width=25)
logfiles_textbox = ttk.Entry(output_values_frame, textvariable=logfiles_path, width=40, state=DISABLED)
logfiles_browse_button = ttk.Button(output_values_frame, text="Browse", command=browse_logfiles_dir, width=20, state=DISABLED)

def diff_logdir_toggle():
	if diff_logdir_var.get():
		logfiles_textbox.config(state=NORMAL)
		logfiles_browse_button.config(state=NORMAL)
	else:
		logfiles_textbox.config(state=DISABLED)
		logfiles_browse_button.config(state=DISABLED)
		logfiles_path.set(output_path.get())
# checkbox for determining whether the output and logfile dirs. are same
diff_logdir_var = IntVar()
diff_logdir_cb = ttk.Checkbutton(output_values_frame, text="Different Log Dir.?", variable=diff_logdir_var, command=diff_logdir_toggle)

output_textbox_label.grid(row=0, column=0, sticky="NEWS", padx=2.5, pady=2.5)
output_textbox.grid(row=0, column=1, sticky="NEWS", padx=2.5, pady=2.5)
output_browse_button.grid(row=0, column=2, sticky="NEWS", padx=2.5, pady=2.5)
logfiles_textbox_label.grid(row=1, column=0, sticky="NEWS", padx=2.5, pady=2.5)
logfiles_textbox.grid(row=1, column=1, sticky="NEWS", padx=2.5, pady=2.5)
logfiles_browse_button.grid(row=1, column=2, sticky="NEWS", padx=2.5, pady=2.5)
diff_logdir_cb.grid(row=2, column=2, sticky="NEWS", padx=2.5, pady=2.5)

# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# TEST VALUES
# ------------------------------------------------------------------------------------

# def populate_test_vals():
# 	ml_var.set('0')
# 	ligand_path.set("E:\\Dropbox\\B.I.T.S\\Academics\\PS-II\\Work\\Python\\VinaGUI\\VinaGUI_v1.0\\test\\Ligands\\PhbA.pdbqt")
# 	receptor_path.set("E:\\Dropbox\\B.I.T.S\\Academics\\PS-II\\Work\\Python\\VinaGUI\\VinaGUI_v1.0\\test\\Proteins\\1HBK.pdbqt")
# 	ss_center_x.set("-5"); ss_center_y.set("17"); ss_center_z.set("13")
# 	ss_size_x.set("18"); ss_size_y.set("16"); ss_size_z.set("16")
# 	output_path.set("E:\\Dropbox\\B.I.T.S\\Academics\\PS-II\\Work\\Python\\VinaGUI\\VinaGUI_v1.0\\test\\_Output")
# 	logfiles_path.set("E:\\Dropbox\\B.I.T.S\\Academics\\PS-II\\Work\\Python\\VinaGUI\\VinaGUI_v1.0\\test\\_Output\\Logfiles")

# test_values_button = ttk.Button(inputs_frame, text="TEST VALUES", command=populate_test_vals)
# test_values_button.grid(row=5, column=0, sticky="EW", padx=10, pady=10, ipadx=10, ipady=10)

# ------------------------------------------------------------------------------------

# ***

# ------------------------------------------------------------------------------------
# VINA FRAME
# ------------------------------------------------------------------------------------

status_frame = ttk.Labelframe(vina_frame, text="Stauts Info.")
status_frame_msg = '''
Status Info., i.e. this area, is a feature planned for a future version of VinaGUI.\n

This area would/might display information such as:

* Current receptor and ligand files, on which the docking analysis is being run.
* No of remaining ligands, in case of multiple ligands (and a progress bar).\n

In this version, once the analysis is complete for a(ll) ligand(s),\nthe 'RUN VINA' button will display the text 'DONE!'.\n
'''
status_frame_label = ttk.Label(status_frame, text=status_frame_msg)
status_frame_label.pack(expand=1)
status_frame.pack(anchor="n", fill=BOTH, expand=1, padx=10, pady=10)

def run_vina():
	# run_vina_button.config(text="VINA IS RUNNING...", state=DISABLED)
	
	lig_path, rec_path, flex_path = ligand_path.get(), receptor_path.get(), flexchain_path.get()
	center = (ss_center_x.get(), ss_center_y.get(), ss_center_z.get())
	size = (ss_size_x.get(), ss_size_y.get(), ss_size_z.get())
	output_dir, logfiles_dir = output_path.get(), logfiles_path.get()
	exhaustiveness, seed = exhaustiveness_var.get(), seed_var.get()
	max_binding_modes, energy_range = maxbindingmodes_var.get(), energyrange_var.get()

	empty_input_error = (not lig_path or not rec_path or "" in center or "" in size or not output_dir)

	if empty_input_error:
		tkMessageBox.showerror("Error!", "You have missing input(s).")
		run_vina_button.config(text="RUN VINA", state=NORMAL)
	else:
		notebook_ui.tab(0, state=DISABLED)
		if not os.path.isdir(lig_path):
			os.path.basename(ligand_path.get()) + "..."
			vina(
				lig_path, rec_path, flex_path, 
				center, size, output_dir, logfiles_dir,
				exhaustiveness, seed, max_binding_modes, energy_range
			)
		else:
			ligands = [lig_file for lig_file in os.listdir(lig_path) if lig_file.endswith(".pdbqt") or lig_file.endswith(".PDBQT")]
			for lig in ligands:
				vina(
					os.path.join(lig_path, lig), rec_path, flex_path, 
					center, size, output_dir, logfiles_dir,
					exhaustiveness, seed, max_binding_modes, energy_range
					)
		run_vina_button.config(text="DONE!", state=DISABLED)

run_vina_button = ttk.Button(vina_frame, text="RUN VINA", command=run_vina)
run_vina_button.pack(anchor="s", fill="x", expand=1, padx=10, pady=10, ipadx=10, ipady=10)

# ------------------------------------------------------------------------------------


notebook_ui.add(inputs_frame, text="Inputs")
notebook_ui.add(vina_frame, text="Vina")
notebook_ui.pack(anchor=CENTER, expand=1, padx=10, pady=10)
root.mainloop()
