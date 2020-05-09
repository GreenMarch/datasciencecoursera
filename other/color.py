class Color:

    def __init__(self, color):
        self.color = color

    def getcolor(self):
        return self.color

    def getcolor_red(self):
        return "red"


class ShowColor(Color):
    def printcolor(self):
        print(self.getcolor() + " extended!")
        print(self.getcolor_red() + " extended!")


ShowColor("blue").printcolor()
