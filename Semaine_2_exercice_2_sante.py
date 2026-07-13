# ======================================================
#AKIENI ACADEMI - Projet Sante Publique
#Semaine 2 - Exercice 2 : KPis Sanitaires OMS
# ======================================================
# --- DONNEES BRUTES ---
budget_fcfa           = 87_450_000  # underscore pour lisibilite des grands nombres
nb_consultations_ext  = 4823
nb_hospitalisation    = 1247
nb_deces              = 18
nb_lits_total         = 180
nb_lits_occupes       = 143
nb_medecins           = 22
nb_infermiers         = 58
population_dept       = 128_000
taux_eur_fcfa         = 655.957
taux_usd_fcfa         = 600.0

# --- A COMPLETER ---
# 1. Conversion devises
budget_eur            = budget_fcfa / taux_eur_fcfa  
budget_usd            = budget_fcfa / taux_usd_fcfa 

# 2. INDICATEUR OMS
dnsite_medicale       = (nb_medecins / population_dept) * 1000 
taux_mortalite        = (nb_deces / nb_hospitalisation) * 100
taux_occupation       = (nb_lits_occupes / nb_lits_total) * 100

# 3. Division entiere et modulo
budget_medicaments    = int(budget_fcfa * 0.35)
cout_journalier_meds  = 450_000
jours_stock           = budget_medicaments // cout_journalier_meds     # division entiere //
jours_restants        = budget_medicaments % cout_journalier_meds      # modulo %

# 4. Puissance pour projection
budget_n_plus_2       = budget_fcfa * (1.08 ** 2)       # ** pour la puissance

# --- AFFICHAGE RAPPORT ---
print("\n=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital Genaral Pointe-Noire ===\n")
print("BUDGET")
print(f" Depenses Q4         : {budget_fcfa:,} FCFA" .replace(","," "))
print(f" En Euros           : {budget_eur:,.2f} EUR" .replace(","," "))
print(f" En dollards)       : {budget_usd:,.2f} USD" .replace(","," "))
print("INDICATEUR OMS")
print(f" Densite medicale   : {dnsite_medicale: .1f} medecins / 1000 hab [norme OMS : >= 2.3]")
print(f" Taux mortalite     : {taux_mortalite: .1f} % [Seuil alerte : > 2%]")
print(f" Taux occupation    : {taux_occupation: .1f} % [Optimal : 70-85%]")
print("ANALYSE PFARMACIE")
print(f" Budget medicaments : {budget_medicaments: ,} FCFA" .replace(",", " "))
print(f" Jours de stock     : {jours_stock} Jours")
print(f" Jours depassement  : 0 Jours")
print("PROJECTION")
print(f" Budget N+2 (8%/an) : {budget_n_plus_2:,.1f} FCFA" .replace(",", " "))
print(f"ALERTE            : Densite mdicale CRITIQUE "  f"({dnsite_medicale: .1f} pour 1000 hab - norme OMS : 2.3)")