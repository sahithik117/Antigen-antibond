from Bio.PDB import PDBParser
import numpy as np

# PDB file
pdb_file = "data/abag_split.csv"

# Load PDB
parser = PDBParser(QUIET=True)
structure = parser.get_structure("abag_split", pdb_file)

print("PDB loaded successfully!")

# Get first model
models = list(structure.get_models())

if len(models) == 0:
    print("No model found!")
    exit()

model = models[0]

# Get chains
chains = list(model.get_chains())

print("Chains found:")

for chain in chains:
    print("Chain:", chain.id)

# ------------------------------------------------
# IMPORTANT:
# Change these two chain IDs according to your PDB
# ------------------------------------------------

antibody_chain = model["A"]
antigen_chain = model["B"]

# Contact distance
DISTANCE_THRESHOLD = 5.0

contacts = []

# Go through antibody residues
for antibody_residue in antibody_chain:

    # Skip water
    if antibody_residue.id[0] != " ":
        continue

    # Go through antigen residues
    for antigen_residue in antigen_chain:

        # Skip water
        if antigen_residue.id[0] != " ":
            continue

        # Compare atoms
        contact_found = False

        for antibody_atom in antibody_residue:
            for antigen_atom in antigen_residue:

                distance = np.linalg.norm(
                    antibody_atom.coord - antigen_atom.coord
                )

                if distance <= DISTANCE_THRESHOLD:
                    contact_found = True
                    break

            if contact_found:
                break

        # Store contact
        if contact_found:

            contacts.append(
                (
                    antibody_residue.get_resname(),
                    antigen_residue.get_resname()
                )
            )


# ------------------------------------------------
# Print results
# ------------------------------------------------

print()
print("Total contacts:", len(contacts))

print()
print("First 20 contacts:")

for antibody, antigen in contacts[:20]:

    print(
        "Antibody:",
        antibody,
        "→ Antigen:",
        antigen
    )