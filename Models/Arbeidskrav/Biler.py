#oppgavesett 1 oppgave 1

class Bil:
    def __init__(self, merke: str, modell: str, aar: int, hastighet: int):
        self.merke = merke
        self.modell = modell
        self.aar = aar
        self.hastighet = hastighet

    def __str__(self):
        return f'Dette er en {self.merke} {self.modell}, produsert i {self.aar} og kan kjøre i {self.hastighet}'
    def akselerer(self, okning):
        self.hastighet += okning
        print(f"Hastigheten er nå {self.hastighet} km/t.")

    def brems(self, reduksjon):
        self.hastighet -= reduksjon
        if self.hastighet < 0:
            self.hastighet = 0
        print(f"Hastigheten er nå {self.hastighet} km/t.")

    def vis_info(self):
        print(self.__str__())


bil = Bil("Pegani", "ACT III", 2025, hastighet=500)
bil.vis_info()
bil.akselerer(50)
bil.brems(20)
bil.vis_info()
