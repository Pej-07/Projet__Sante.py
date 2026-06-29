# ============================================
# RAPPORT DSS - 3 HOPITAUX DU POOL
# ============================================

# --------------------------------------------
# 1. Hopital District Kinkala
# # ------------------------------------------

budget_kin              = 12_500_000
consultation_kin        = 1_847
Hospitalisations_kin    = 312
deces_hospitalier_kin   = 8
lits_totaux_kin         = 45
lits_occupes_kin        = 41
medecins_permanants_kin = 3
population_dservie_kin  = 85_000
# --- A COMPLETEER ---
nb_total_patients_kin   = consultation_kin + Hospitalisations_kin
cout_moyen_kin          = budget_kin / nb_total_patients_kin
taux_occupation_kin     = (lits_occupes_kin / lits_totaux_kin) * 100
densite_meedicale_kin   = medecins_permanants_kin / population_dservie_kin
taux_mortalite_kin      = (deces_hospitalier_kin / Hospitalisations_kin) * 100

if taux_mortalite_kin > 2 or densite_meedicale_kin < 0.05:
    statut_kin          = "CRITIQUE"
else:
     statut_kin         = "STABLE"

# --------------------------------------------
# 2. CMS de Vindza
# # ------------------------------------------

Budget_trim_vin         = 6_800_000
consultation_vin        = 923
Hospitalisations_vin    = 87
deces_hospitalier_vin   = 2
lits_totaux_vin         = 20
lits_occupes_vin        = 14
medecins_permanants_vin = 1
population_dservie_vin  = 42_000
# --- A COMPLETEER ---
nb_total_patients_vin   = consultation_vin + Hospitalisations_vin
cout_moyen_par_patient_vin = Budget_trim_vin / nb_total_patients_vin
taux_occupation_vin     = (lits_occupes_vin / lits_totaux_vin ) * 100
densite_meedicale_vin   = medecins_permanants_vin / population_dservie_vin
taux_mortalite_vin      = (deces_hospitalier_vin / Hospitalisations_vin) * 100

if taux_mortalite_vin > 2 or densite_meedicale_vin < 0.05:
    statut_vin          = "CRITIQUE"
else:
     statut_vin         = "STABLE"

# ----------------------------------------------
# 3. Hopital de Kindamba
# ----------------------------------------------
Budget_trim_kid         = 9_200_000
consultation_kid        = 1_234
Hospitalisations_kid    = 201
deces_hospitalier_kid   = 11
lits_totaux_kid         = 35
lits_occupes_kid        = 33
medecins_permanants_kid = 2
population_dservie_kid  = 67_000
# --- A COMPLETEER ---
nb_total_patients_kid   = consultation_kid + Hospitalisations_kid
cout_moyen_par_patient_kid = Budget_trim_kid / nb_total_patients_kid
taux_occupation_kid     = (lits_occupes_kid / lits_totaux_kid) * 100
densite_meedicale_kid   = medecins_permanants_kid / population_dservie_kid
taux_mortalite_kid      = (deces_hospitalier_kid / Hospitalisations_kid) * 100

if taux_mortalite_kid > 2 or densite_meedicale_kid < 0.05:
    statut_kid          = "CRITIQUE"
else:
     statut_kid         = "STABLE"

# --- AFFICHAGE RESULTAT ---
print("=" * 60)
print("RAPPORT DSS - 3 HOPITAUX DU POOL")
print("=" * 60)
print("\n1. Hopital District Kinkala")
print(f" cout moyen/patients KIN : {cout_moyen_kin:,.2f} FCFA" .replace(","," "))
print(f" Taux d'occupations KIN  : {taux_occupation_kin: .2f}%")
print(f" Densite medicale KIN    : {densite_meedicale_kin: .5f}")
print(f" Taux de mortalite KIN   : {taux_mortalite_kin: .2f}%")
print(f" STATUT KIN              : {statut_kin }")

print("\n2. CMS de Vindza")
print(f" cout moyen/patients VIN : {cout_moyen_par_patient_vin:,.2f} FCFA" .replace(","," "))
print(f" Taux d'occupations VIN  : {taux_occupation_vin: .2f}%")
print(f" Densite medicale VIN    : {densite_meedicale_vin: .5}")
print(f" Taux de mortalite VIN   : {taux_mortalite_vin: .2f}%")
print(f" STATUT VIN              : {statut_vin}")

print("\n3. Hopital de Kindamba")
print(f" cout moyen/patients     : {cout_moyen_par_patient_kid:,.2f} FCFA" .replace(","," "))
print(f" Taux d'occupations      : {taux_occupation_kid: .2f}%")
print(f" Densite medicale        : {densite_meedicale_kid: .5}")
print(f" Taux de mortalite VID   : {taux_mortalite_kid: .2f}%")
print(f" STATUT VID              : {statut_kid}")

# ============================================
#RAPPPORT
# ============================================

medecins_manquants = ((5 - medecins_permanants_kin) + (5 - medecins_permanants_vin) + (5 - medecins_permanants_kid) )
cout_recrutement   = medecins_manquants * 1200000
budget_total       = (budget_kin + Budget_trim_vin + Budget_trim_kid)

print("\n" + "=" * 60)
print("RAPPORT")
print("=" * 60)

print(f" Budget total disponible : {budget_total:,.0f} FCFA" .replace(","," "))
print(f" cout de recrutment      : {cout_recrutement:,.0f} FCFA" .replace(","," "))

if budget_total >= cout_recrutement:
     print("le budget est suffisant pour atteindre: 5 medecins par hopital.")
else:
     print("le budgt eest insuffisant.")