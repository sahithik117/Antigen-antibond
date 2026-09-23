from Bio.PDB import PDBParser

# Location of PDB file
pdb_file = "data/abag_split.csv"

# Create parser
parser = PDBParser(QUIET=True)

# Read PDB
structure = parser.get_structure("abag_split", pdb_file)

print("PDB file loaded successfully!\n")

# Display models and chains
for model in structure:
    print("Model:", model.id)

    for chain in model:
        print("Chain:", chain.id)