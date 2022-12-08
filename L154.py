class Fabric:
    """Represents Fabric

    attributes: countryOfOrigin, color"""

    def __init__(self,countryOfOrigin, color):
        self.countryOfOrigin=countryOfOrigin
        self.color=color

    def __str__(self):
        return self.countryOfOrigin+"("+str(self.color)+")"

F1=Fabric("USA", "Blue")

print(F1)
