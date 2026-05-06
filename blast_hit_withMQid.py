import pandas as pd

# Load MaxQuant proteinGroups
mq = pd.read_csv('proteinGroups.txt', sep='\t')

# Load BLAST results
blast = pd.read_csv('blast_results.tsv', sep='\t', header=None)
blast.columns = ['Protein IDs', 'Allergen_hit', 'pident', 'length', 'evalue', 'bitscore', 'Allergen_description']

# Merge based on Protein IDs
merged = mq.merge(blast, on='Protein IDs', how='left')

# Optional: mark allergen hits
merged['Allergen_match'] = merged['Allergen_hit'].notna()

# Save merged output
merged.to_csv('proteins_with_allergen_annotations.tsv', sep='\t', index=False)
