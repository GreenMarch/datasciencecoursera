# definition of superclass "Triangles"
class Triangles(object):
    count = 0

    # Calling Constructor
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        Triangles.count += 1

    def setName(self, name):
        self.name = name

    def setdim(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def getcount(self):
        return Triangles.count

    def __str__(self):
        return \
            'Name: ' + self.name + \
            '\nDimensions: ' + str(self.s1) + ',' + str(self.s2) + ',' + str(self.s3) + \
            '\nCount: ' + str(self.getcount())


    # describing a subclass


# inherits from Triangles
class Peri(Triangles):

    # function to calculate the area
    def calculate(self):
        self.pm = 0
        self.pm = self.s1 + self.s2 + self.s3

    # function to display just the area
    # because it is not extended
    def display(self):
        return self.pm


def main():
    # instance of the subclass
    p = Peri('PQR', 2, 3, 4)
    # call to calculate()
    p.calculate()
    # explicit call to __str__()
    print(p.__str__())
    # call to display()
    print("pm:", p.display())


main()
