import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your merged file
df = pd.read_csv('merged_allergen_hits_clean.csv')

#  Filter high-confidence BLAST matches
df_confident = df[(df['pident'] >= 40) & (df['evalue'] <= 1e-5)]

#  Find LFQ intensity columns (they usually start with 'LFQ intensity')
lfq_cols = [c for c in df_confident.columns if 'LFQ intensity' in c]

#  Compute mean LFQ intensity across all samples (log-transform optional)
df_confident['mean_LFQ'] = df_confident[lfq_cols].replace(0, np.nan).mean(axis=1)

# Sort by intensity (descending) and take top 40
df_top40 = df_confident.sort_values('mean_LFQ', ascending=False).head(40)

plt.figure(figsize=(10,8))
plt.barh(df_top40['stitle_clean'], df_top40['mean_LFQ'])
plt.gca().invert_yaxis()  # highest at top
plt.xlabel('Mean LFQ intensity (a.u.)')
plt.ylabel('Allergen')
plt.title('Top 40 highly expressed insect allergens (high-confidence hits)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,8))
plt.barh(df_top40['stitle_clean'], np.log10(df_top40['mean_LFQ'] + 1))
plt.gca().invert_yaxis()
plt.xlabel('log₁₀(LFQ intensity)')
plt.ylabel('Allergen')
plt.title('Top 40 high-confidence, highly expressed insect allergens')
plt.tight_layout()
plt.show()
