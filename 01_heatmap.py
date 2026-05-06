import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("top40_allergens_for_heatmap_no_log_transform.csv")
meta = pd.read_csv("sample_metadata.csv", dtype=str)

# Extract intensity columns
intensity_cols = [c for c in df.columns if c.startswith("LFQ intensity")]

# Set protein names as index
heatmap_data = df.set_index("stitle_clean")[intensity_cols]

# Map sample IDs to species
meta = meta.set_index("Species")
sample_ids = [c.replace("LFQ intensity", "").strip() for c in intensity_cols]
species_labels = [meta.loc[s, "Species"] if s in meta.index else "Unknown" for s in sample_ids]

# Sort columns by species
order = sorted(range(len(intensity_cols)), key=lambda i: species_labels[i])
heatmap_sorted = heatmap_data.iloc[:, order]
sorted_cols = [intensity_cols[i] for i in order]
#plot heatmap
plt.figure(figsize=(14, 10))
plt.imshow(heatmap_sorted.values, aspect='auto')
plt.yticks(range(len(heatmap_sorted.index)), heatmap_sorted.index)
plt.xticks(range(len(sorted_cols)), sorted_cols, rotation=90)
plt.title("Allergen Heatmap (stitle_clean vs LFQ intensity, grouped by species)")
plt.colorbar(label="Intensity (Z-score)")
plt.tight_layout()
plt.show()

sns.clustermap(
    heatmap_data,
    figsize=(12, 12),
    cmap="viridis",
    yticklabels=True
)
plt.show()
