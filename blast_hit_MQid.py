import pandas as pd
import matplotlib.pyplot as plt

# 1. Load MaxQuant proteinGroups matrix
mq = pd.read_csv('protein_filter_processed.txt', sep='\t')

# 2. Load BLAST results
blast = pd.read_csv('blastp_hits_named_with_header.txt', sep='\t')

# 3. Clean protein IDs if needed (e.g., keep only accession part)
# Example for IDs like 'tr|A0A8J6LE66|A0A8J6LE66_TENMO'
blast['qseqid'] = blast['qseqid'].str.split('|').str[1]

# 4. Merge MaxQuant with BLAST hits
merged = pd.merge(mq, blast, left_on='Cleaned_ID', right_on='qseqid', how='inner')

# 5. Filter strong hits (optional)
merged_filtered = merged[(merged['pident'] >= 35) & (merged['evalue'] <= 1e-5)]

# 6. Count detected allergens
allergen_counts = merged_filtered['stitle'].value_counts()

# 7. Plot a bar graph
plt.figure(figsize=(10,6))
allergen_counts.plot(kind='bar')
plt.ylabel('Number of detected proteins')
plt.xlabel('Allergen name')
plt.title('Detected allergens in insect proteomics dataset')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print(merged_filtered.head())
print(type(merged_filtered))
