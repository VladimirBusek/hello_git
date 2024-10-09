class Zprava:
    def __init__(self, jmeno, text):
        self.jmeno = jmeno
        self.zprava = text
    
    def pozdrav(self):
        print(f"Ahoj, jmenuji se {self.jmeno} a chci říct: {self.zprava}")