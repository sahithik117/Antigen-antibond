from Bio.PDB import PDBParser

pdb_file = "data/abag_split.csv"

parser = PDBParser(QUIET=True)

structure = parser.get_structure("abag_split", pdb_file)

print("PDB loaded successfully!")
print()

for model in structure:

    print("Model:", model.id)

    for chain in model:

        print()
        print("Chain:", chain.id)

        count = 0

        for residue in chain:

            print(
                "Residue:",
                residue.get_resname(),
                "Number:",
                residue.id[1]
            )

            count += 1

            if count == 10:
                break