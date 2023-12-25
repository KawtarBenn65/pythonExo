class Course:
    def __init__(self, boat_type):
        self.boat_type = boat_type
        self.boats = []
        self.is_running = False

    def ajout_bateau_ligne_depart(self, boat):
        if isinstance(boat, Bateau):
            if boat.boat_type == self.boat_type:
                self.boats.append(boat)
                print(f"{boat.name} ajouté à la ligne de départ.")
            else:
                print("Le type de bateau ne correspond pas au type de la course.")
        else:
            print("Type de bateau invalide.")

    def depart(self):
        print("La course a commencé !")
        self.is_running = True

    def en_cours(self):
        return self.is_running

    def next_loop(self):
        for boat in self.boats:
            boat.move()

    def affiche_position(self):
        positions = {boat.name: round(boat.distance, 2) for boat in self.boats}
        return positions

class Bateau:
    def __init__(self, name, average_speed, boat_type):
        self.name = name
        self.average_speed = average_speed
        self.distance = 0
        self.boat_type = boat_type

    def move(self):
        self.distance += self.average_speed / 60 
