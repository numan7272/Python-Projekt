#
#from abc import ABC, abstractmethod
#
#class Form:
#    
#    @abstractmethod
#    def Fläche(self):
#        pass
#
#
#class Kreis(Form):
#    def __init__(self, radius):
#        self.radius = radius
#    def Fläche(self):
#        return 3.14 * self.radius
#
#
#
#class Viereck(Form):
#    def __init__(self, seite):
#        self.seite = seite
#
#    def Fläche(self):
#        return self.seite ** 2
#
#class Dreieck(Form):
#    def __init__(self, höhe, base):
#        self.base = base
#        self.höhe = höhe
#
#    def Fläche(self):
#        return 0.5 * self.base * self.höhe
#
#
#
#class Pizza(Kreis):
#    def __init__(self, Belag, radius):
#        self.Belag = Belag
#        self.radius = radius
#
#
#formen = [Kreis(2), Viereck(3), Dreieck(4, 4), Pizza("salami",14)]
#
#for form in formen:
#    print(f"{form.Fläche()} cm²")
#
#
#



#class Tier:
#    leben = True
#
#
#class Hund(Tier):
#    def sprechen(self):
#        print("WUFF!")
#
#
#class Katze(Tier):
#    def sprechen(self):
#        print("MIAU!")
#
#Tiere = [Hund(), Katze()]
#
#for tier in Tiere:
#    tier.sprechen()
#    print(tier.leben)

