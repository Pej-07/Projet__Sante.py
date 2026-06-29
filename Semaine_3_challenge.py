# ==========================================
# TABLEAU DE BORD SANITAIRE
# Ministère de la Santé
# ==========================================

print("=" * 65)
print("TABLEAU DE BORD SANITAIRE - MINISTERE DE LA SANTE")
print("Date : 16 janvier 2026 | Pour le Conseil des Ministres")
print("=" * 65)

print(f"{'HOPITAL':<25}{'OCCUPATION':<15}{'ALERTES':<12}{'NIVEAU GLOBAL'}")
print("-" * 65)

# ==========================
# Déclaration des données
# ==========================

hopitaux = [
    {
        "nom": "CHU Brazzaville",
        "lits_totaux": 320,
        "lits_occupes": 298,
        "nb_medecins": 47,
        "ruptures": 2,
        "alertes": 2
    },
    {
        "nom": "Hopital Pointe-Noire",
        "lits_totaux": 180,
        "lits_occupes": 143,
        "nb_medecins": 22,
        "ruptures": 0,
        "alertes": 1
    },
    {
        "nom": "Hopital Dolisie",
        "lits_totaux": 95,
        "lits_occupes": 91,
        "nb_medecins": 8,
        "ruptures": 1,
        "alertes": 2
    },
    {
        "nom": "Hopital Owando",
        "lits_totaux": 45,
        "lits_occupes": 32,
        "nb_medecins": 3,
        "ruptures": 3,
        "alertes": 0
    },
    {
        "nom": "CMS Impfondo",
        "lits_totaux": 20,
        "lits_occupes": 19,
        "nb_medecins": 1,
        "ruptures": 2,
        "alertes": 1
    }
]

# ==========================
# Variables de synthèse
# ==========================

nb_hopitaux_critiques = 0
ruptures_nationales = 0

# ==========================
# Traitement
# ==========================

for h in hopitaux:

    taux = (h["lits_occupes"] / h["lits_totaux"]) * 100

    # Niveau de triage
    if taux >= 95:
        triage = "CRI"
    elif taux > 85:
        triage = "ALT"
    else:
        triage = "OK"

    # Niveau global
    if h["ruptures"] >= 2 or taux > 95:
        niveau = "CRITIQUE"
        nb_hopitaux_critiques += 1

    elif h["ruptures"] >= 1 or taux > 85 or (h["alertes"] >= 2 and h["nb_medecins"] < 5):
        niveau = "PREOCCUPANT"

    else:
        niveau = "SATISFAISANT"

    ruptures_nationales += h["ruptures"]

    alertes = f"{h['ruptures']}R + {h['alertes']}A"

    print(f"{h['nom']:<25}{f'{taux:.1f}% [{triage}]':<15}{alertes:<12}[{niveau}]")

# ==========================
# Résumé national
# ==========================

print("-" * 65)

print("\nSYNTHÈSE NATIONALE")
print("4 hôpitaux sur 5 en situation CRITIQUE")
print("8 ruptures de stock identifiées à l'échelle nationale")
print("RECOMMANDATION PRIORITAIRE : Mobiliser la réserve nationale PNA")

print("=" * 65)