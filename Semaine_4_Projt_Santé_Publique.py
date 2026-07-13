total_suspects = 0
total_confirmes = 0
total_deces = 0
total_actifs = 0
zones_vertes = 0
zones_jaunes = 0
zones_oranges = 0
zones_rouges = 0
nb_districts = 9

print(f'=== SURVEILLANCE EPIDEMIQUE MPOX - CONGO 2025 ===')
for i in range(1, nb_districts + 1):
    print('--- Districts', i, '---')
    nom_district = input('Nom du district :')
    suspects = int(input('cas suspects :'))
    confirmes = int(input('Cas confirmes :'))
    deces = int(input('Deces :'))

    cas_actifs = confirmes - deces
    letalite = (deces / confirmes) * 100
    total_confirmes = nb_districts

    if confirmes > 0:
        letalite = 0
    else:
        letalite = 0

    if confirmes >= 10:
        alerte = 'ROUGE'
        zones_rouges = zones_rouges+ 1
    elif confirmes >= 5:
        alrte = 'ORANGE'
        zones_oranges = zones_oranges + 1
    elif confirmes >= 2:
        alerte = 'JAUNE'
        zones_jaunes = zones_jaunes + 1
    else:
        alerte = 'VERT'
        zones_vertes = zones_vertes + 1

    total_suspects = total_suspects + suspects
    total_confirmes = total_confirmes + confirmes
    total_deces = total_deces + deces
    total_actifs = total_actifs + cas_actifs

    print(' Alerte :', alerte)
    print(' Actifs :', cas_actifs)
    print(' Letalite :', round(letalite, 1), '%')
    print()

print('=' * 60)
print('    RAPPORT NATIONAL MPOX 2025   ')
print('=' * 60)
print('Districts analyses :', nb_districts)
print('Total suspects :', total_suspects)
print('Total confirmes :', total_confirmes)
print('Total deces :', total_deces)
print('Total cas actifs :', total_actifs)
print('Zones VERTES :', zones_vertes)
print('ZONES JAUNE :', zones_jaunes)
print('ZONES ORANGES :', zones_oranges)
print('ZONES ROUGES :', zones_rouges)
print('=' * 60)