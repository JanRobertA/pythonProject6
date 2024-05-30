#oppgave sett 1 Oppgave 2

class Bok:
    def __init__(self, tittel: str, forfatter: str, utgivelsesår: int, pris: int):
        self.tittel = tittel
        self.forfatter = forfatter
        self.utgivelsesår = utgivelsesår
        self.pris = pris

    def vis_bokinfo(self):
        print(f"Tittel: {self.tittel}, Forfatter: {self.forfatter}, Utgivelsesår: {self.utgivelsesår}, Pris: {self.pris} kr")

    def endre_pris(self, ny_pris):
        self.pris = ny_pris
        print(f"Ny pris for boken '{self.tittel}' er nå {self.pris} kr.")


bok = Bok("Mysterier", "Knut Hamsun", 1892, 199)
bok.vis_bokinfo()
bok.endre_pris(149)
bok.vis_bokinfo()
