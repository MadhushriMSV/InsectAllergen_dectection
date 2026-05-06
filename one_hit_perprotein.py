import pandas as pd

# Load Perseus + BLAST merged data
df = pd.read_csv("merged_allergen_hits_clean.csv")# used to create allergens 454 list

# Convert BLAST score fields
for col in ["pident", "evalue", "bitscore"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# OPTION 1️⃣: Keep only the **best hit per protein**
best_hit = (
    df.sort_values(["pident", "bitscore"], ascending=[False, False])
      .drop_duplicates(subset="qseqid", keep="first")
)

best_hit.to_csv("merged_best_hit.csv", index=False)
print(f"✅ Reduced from {len(df)} → {len(best_hit)} unique proteins (best match kept).")


merged_hits.to_csv("merged_all_hits_combined.csv", index=False)
print(f"✅ Collapsed to {len(merged_hits)} proteins with all allergen hits summarized.")
