class Arbeiter:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
        

    @staticmethod
    def is_gültig_position(position):
        gültig_position = ["Manager", "Kassierer", "Koch", "Putzkraft"]
        return position in gültig_position
    

print(Arbeiter.is_gültig_position("Koch"))