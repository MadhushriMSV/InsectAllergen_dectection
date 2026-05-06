# Insect_Allergen_dectection
MaxQuant was run and blastoutput were merged for identified proteins 
## Load MaxQuant proteinGroups
in the 1st part of the analyses 'proteinGroups.txt'were merged with blastp output using script "blast_hit_MQid"
## Clean up merged hits
Merged hits were cleaned up using script "one_hit_per_protein"
## List of top 40 proteins LFQ
using the new list top 40 allergens based on LFQ were selected using script "select_top40_allergens" 

