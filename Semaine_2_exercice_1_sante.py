# ========================================================
#    AKIENI ACADEMY - Projet Santé Publique
# ========================================================
# SECTION 1 : VARIABLES PATIENT
nom_patient = "MAVOUNGOU Celestine"
age_patient = 42
sexe_patient = "F"
departement_patient = "Brazzaville"
coverture_sociale = "CNSS"
# ---------------------------------------------------------
# SECTION 2 : VARIABLES CONSULTATION
type_consultation = "urgences"
cout_consultation_fcfa = 15000
nb_consultation = 1
remise_cnss_pct = 30
diagnostic_pricipal = "paludisme"
# -----------------------------------------------------------
# SECTION 3: VARIABLES HOPITAL
nom_hopital = "CHU de Brazzaville"
ville_hopital = "Brazzaville"
nb_lits_total = 320
nb_lits_occupés = 284
nb_médecins_actifs = 47
# ========================================================
# SECTION 4 : CALCULS
cout_total_fcfa = cout_consultation_fcfa*nb_consultation*(1-remise_cnss_pct / 100)
taux_occupation_pct = round(nb_lits_occupés / nb_lits_total*100, 1)
nb_consultations_hopital = 120
ratio_consultations_médecin = round(nb_consultations_hopital / nb_médecins_actifs, 1)
# SECTION 5 : AFFICHAGE
print("=" * 60)
print(f"FICHE PATIENT - {nom_patient}")
print("=" * 60)
print(f"Age                          : {age_patient} ANS")
print(f"sexe                         : {sexe_patient}")
print(f"Département                  : {departement_patient}")
print(f"Couvrture                    : {coverture_sociale}")
print("-" * 60)
print("CONSULTATION")
print(f"Type                         : {type_consultation}")
print(f"DIAGNOSTIC                   : {diagnostic_pricipal}")
print(f"Cout unitaire                : {cout_consultation_fcfa} FCFA")
print(f"Remise CNSS                  : {remise_cnss_pct }%")
print(f"COUT TOTAL                   : {cout_total_fcfa} FCFA")
print("-" * 60)
print(f"HOPITAL                      : {nom_hopital}")
print(f"VILLE                        : {ville_hopital}")
print(f"Lits occupés                 : {nb_lits_occupés} / {nb_lits_total}({taux_occupation_pct}%)")
print(f"Médecin actifs               : {nb_médecins_actifs}")
print("=" * 60)
print(f"Ratio consultations/médcecin : {ratio_consultations_médecin}")
print("=" * 60)




