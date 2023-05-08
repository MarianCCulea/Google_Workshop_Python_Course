class Catalog:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def afisare_absente(self):
        return f"{self.nume} {self.prenume} are {self.absente} absente."

    def incrementare_absente(self):
        self.absente += 1

    def stergere_absente(self, nr):
        if self.absente >= nr:
            self.absente -= nr
        else:
            print("Nu se poate sterge acest numar de absente.")


class Extensie1(Catalog):
    def adaugare_materie(self, materia, note):
        self.materii[materia] = note

    def afisare_materii(self):
        return list(self.materii.keys())

    def afisare_note_mediate(self):
        for materia, note in self.materii.items():
            filtered_note = list(filter(lambda x: isinstance(x, int), note))
            if filtered_note:
                medie = sum(filtered_note) / len(filtered_note)
                print(f"{materia}: {medie}")


# Exemplu de utilizare
student1 = Extensie1("Ion", "Roata")
student1.incrementare_absente()
student1.incrementare_absente()
student1.incrementare_absente()
student1.stergere_absente(2)

student2 = Extensie1("George", "Cerc")
student2.incrementare_absente()
student2.incrementare_absente()
student2.incrementare_absente()
student2.incrementare_absente()

print(student1.afisare_absente())
print(student2.afisare_absente())

student1.adaugare_materie("Python", [7, 8, "absent"])
student2.adaugare_materie("Matematica", [9, 10, 8])
student1.adaugare_materie("Romana", [6, 7, 8])

print(student1.afisare_materii())
print(student2.afisare_materii())

student1.afisare_note_mediate()
student2.afisare_note_mediate()
