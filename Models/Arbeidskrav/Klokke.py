#oppgavesett 1 oppgave 3

class Klokkeklasse:

    def __init__(self, timer=0, minutter=0, sekunder=0):
        self.timer = timer
        self.minutter = minutter
        self.sekunder = sekunder

    def tik(self):
        self.sekunder += 1
        if self.sekunder >= 60:
            self.sekunder = 0
            self.minutter += 1
        if self.minutter >= 60:
            self.minutter = 0
            self.timer += 1
        if self.timer >= 24:
            self.timer = 0

    def juster_tid(self, timer=None, minutter=None, sekunder=None):
        if sekunder is not None:
            self.sekunder += sekunder
        if minutter is not None:
            self.minutter += minutter
        if timer is not None:
            self.timer += timer

        if self.sekunder >= 60:
            ekstra_minutter = self.sekunder // 60
            self.sekunder = self.sekunder % 60
            self.minutter += ekstra_minutter

        if self.minutter >= 60:
            ekstra_timer = self.minutter // 60
            self.minutter = self.minutter % 60
            self.timer += ekstra_timer

        if self.timer >= 24:
            self.timer = self.timer % 24

    def vis_tid(self):
        print(f"{self.timer:02d}:{self.minutter:02d}:{self.sekunder:02d}")

    def sett_tid(self, timer, minutter, sekunder):
        self.timer = timer % 24
        self.minutter = minutter % 60
        self.sekunder = sekunder % 60

    def legg_til_sekunder(self, sekunder):
        self.sekunder += sekunder
        if self.sekunder >= 60:
            ekstra_minutter = self.sekunder // 60
            self.sekunder = self.sekunder % 60
            self.minutter += ekstra_minutter

        if self.minutter >= 60:
            ekstra_timer = self.minutter // 60
            self.minutter = self.minutter % 60
            self.timer += ekstra_timer

        if self.timer >= 24:
            self.timer = self.timer % 24

tid = Klokkeklasse()
tid.vis_tid()

for _ in range(5):
    tid.tik()
    tid.vis_tid()

tid.juster_tid(timer=1, minutter=30, sekunder=90)
tid.vis_tid()

bruker_timer = int(input("Skriv inn timer: "))
bruker_minutter = int(input("Skriv inn minutter: "))
bruker_sekunder = int(input("Skriv inn sekunder: "))
tid.sett_tid(bruker_timer, bruker_minutter, bruker_sekunder)
tid.vis_tid()

sekunder_å_legge_til = int(input("Skriv inn antall sekunder som skal legges til: "))
tid.legg_til_sekunder(sekunder_å_legge_til)
tid.vis_tid()
