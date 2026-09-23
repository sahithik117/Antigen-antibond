from Bio.PDB import PDBParser

# PDB file location
pdb_file = "data/abag_split.csv"

# Create parser
parser = PDBParser(QUIET=True)

# Load PDB file
structure = parser.get_structure("abag_split", pdb_file)

print("PDB loaded successfully!")

# Get all models
models = list(structure.get_models())

print("Number of models:", len(models))

# Check if model exists
if len(models) == 0:
    print("ERROR: No models found in the PDB file.")
    exit()

# Get first model
model = models[0]

print("First model found!")

# Show chains
for chain in model:
    print("Chain:", chain.id)

    # Show residues
    for residue in chain:
        print(
            "Residue:",
            residue.get_resname(),
            "Number:",
            residue.id[1]
        )