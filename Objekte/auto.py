class Auto:
    def __init__(self, model, jahr, farbe, handelbar):
        self.model = model
        self.jahr = jahr
        self.farbe = farbe
        self.handelbar = handelbar

    def fahren(self):
        print(f"Du fährst den {self.model}")

    def stoppen(self):
        print(f"Du stopst den {self.model}")