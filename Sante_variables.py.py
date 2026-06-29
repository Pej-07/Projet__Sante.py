# ===================================================================
# MODULE FONDATEUR - Projrt Sante publique / Akini Academy
# Ce fichier ceentralise toutes les constantes eet variables metier
# Il sera enrichi chaque semaine jusqu'a s24
# ===================================================================

# ========= SECTION A : CONSTANTES NATIONALES ET NORMES OMS =========
TAUX_EUR = 655.957
TAUX_USD = 600.0
SEUIL_OMS_DENSITE_MDICALE = 2.3  # 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0
SEUIL_MORTALITE_ALRTE = 2.0
SEUIL_RUPTURE_STOCK_JOURS = 30
DEEPARTEMENTS_CONGO = ["Brazzaville", "Pointe-Noire", "Bouenza", "Cuvette", "Cuvette-Ouest", "Kouilou", "Lekoumou", "Likouala", "Niari", "Plateaux", "Pool", "Sangha"]

# ==== SECTION B : VARIABLES DES 5 HOPITAUX ========================
# Hopital 1 - CHU de Brazzaville
h1_nom = 'CHU de Brazzavillee'
h1_ville = 'Brazzaville'
h1_departeement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_populations_zone = 1_800_000
# Hopital 2 - Hopital General de Pointe-Noire
h2_nom = 'Hopital General de Pointe-Noire'
h2_ville = 'Pointe-Noir'
h2_departement = 'Pointe-Noire'
h2_type = 'Hopital General'
h2_nb_lits = 295
h2_nb_lits_occupes = 184
h2_nb_medecins = 39
h2_nb_infirmiers = 102
h2_populations_zone = 1_525_000
# Hopital 3 - Hopital de Dolisie
h3_nom = 'Hopital de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = 'Hopital'
h3_nb_lits = 95
h3_nb_lits_occupes =79 
h3_nb_infirmiers = 85
h3_nb_medeecins = 27
h3_populations_zone = 825_000
# Hopital 4 - Hopital de District Owando
h4_nom = 'Hopital de District Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = 'Hopital de District'
h4_nb_lits = 54
h4_nb_lits_occupes = 37 
h4_nb_infirmiers = 47
h4_nb_medecins = 18
h4_populations_zone = 212_000
# Hopital 5 - Centre de Sante Impfondo
h5_ville = 'Impfondo' 
h5_departement = 'Likouala'
h5_type = 'Centre de Sante'
h5_nb_lits = 33
h5_nb_lits_occupes = 11 
h5_nb_infirmires = 17
h5_nb_medecins = 8
h5_populations_zone = 102_000
# ==== SECTION C : VARIABLES DES 5 MEDICAMENTS ======================
# Medicamnt 1 - Artemether-Lumefantrine
m1_nom = 'Artemether-Lumefantrine'
m1_quantite = 850
m1_seuil_rupture = 100
m1_prix = 2500.0
# Medicamnt 2 - Amoxicilline
m2_nom = 'Amoxicilline'
m2_quantite = 92
m2_seuil_rupture = 123
m2_prix = 1100.0
# Medicamnt 3 - Paracetamol
m3_nom = 'Paracetamol'
m3_quantite = 1358
m3_seuil_rupture = 250
m3_prix = 500.0
# Medicamnt 4 - SRO
m4_nom = 'SRO'
m4_quantite = 57
m4_seuil_rupture = 35
m4_prix = 3000.0
# Medicamnt 5 - Vaccin Anti-Paludeen
m5_nom = 'SRO'
m5_quantite = 10000
m5_seuil_rupture = 2000
m5_prix = 500.0
# ==== SECTION D : CALCULS D'INITIALISATION ======================
# Total Medecins
total_medecins = (h1_nb_medecins + h2_nb_medecins +h3_nb_medeecins +h4_nb_medecins +h5_nb_medecins)
# Total infirmiers
total_infirmiers = (h1_nb_infirmiers +h2_nb_infirmiers + h3_nb_infirmiers + h4_nb_infirmiers + h5_nb_infirmires)
# Total des Lits
total_lits = (h1_nb_lits +h2_nb_lits + h3_nb_lits +h4_nb_lits + h5_nb_lits)
# Total des Lits Occupes
total_lits_occupes = (h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes +h5_nb_lits_occupes)
# Population Totale Deservie
Population_totale = (h1_populations_zone + h2_populations_zone + h3_populations_zone + h4_populations_zone +h4_populations_zone)
# Taux d'Occupation Moyen
taux_occupation_moyen = (total_lits_occupes / total_lits) * 100
# Dnsite medicale (medecins pour 1000 habitants)
densite_medicale = (total_medecins / Population_totale) * 100
# Valeur totale du Stock des Medicaments
valeur_stock = (m1_quantite * m1_prix + m2_quantite * m2_prix + m3_quantite * m3_prix + m4_quantite * m4_prix + m5_quantite * m5_prix)

# === SECTION 6 - AFFICHAGE RESULTAT ===============================
print("=" * 60)
print("RAPPORT INITIAL DU SYSTEME DE SANTE")
print("=" * 60)

print(f"Nombre total de meedeecins : {total_medecins: .2f}")
print(f"Nombre total infirmiers    : {total_infirmiers: .2f}")
print(f"Nombre total de lits       : {total_lits: .2f}")
print(f"Nombre total lits occupes  : {total_lits_occupes: .2f}")
print(f"Taux d'occupation          : {taux_occupation_moyen: .2f}%")
print(f"Densite medicale           : {densite_medicale: .2f} medecins/1000 habitants")
print(f"Valeur totale du stock     : {valeur_stock:,.2f} FCFA" .replace(","," "))