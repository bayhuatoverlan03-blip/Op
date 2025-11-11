class Artist:
    def skill(self):
        print("Creates artwork.")

class Musician:
    def skill(self):
        print("Plays musical instruments.")

class Performer(Artist, Musician):
    def skill(self):
        super().skill()
        print("Also performs on stage.")

p = Performer()
p.skill()
