class Auto:
    def __init__(self, model, jahr, farbe, handelbar):
        self.model = model
        self.jahr = jahr
        self.farbe = farbe
        self.handelbar = handelbar

    def fahren(self):
        print("Du fährst das Auto")

    def stoppen(self):
        print("Du fährst das nicht Auto")