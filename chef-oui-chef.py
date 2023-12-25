# chef-oui-chef.py
from aviron import Course, Bateau

# Test de la compétition d'aviron
cadets = Course("2X")
boat_1_2x = Bateau("mickey", 62, "2X")
boat_2_2x = Bateau("minnie", 70, "2X")
boat_3_skiff = Bateau("picsou", 120, "Skiff")

cadets.ajout_bateau_ligne_depart(boat_1_2x)
cadets.ajout_bateau_ligne_depart(boat_2_2x)
cadets.ajout_bateau_ligne_depart(boat_3_skiff)

cadets.depart()

while cadets.en_cours():
    cadets.next_loop()
    positions = cadets.affiche_position()
    print(positions)
    if all(distance >= 2.0 for distance in positions.values()):
        break
