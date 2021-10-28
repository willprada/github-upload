class A:
    def __init__(self, name):
        self.name = name


    def getDescription(self):
        return 'Just a normal object called ' + str(self.name) + ', instance of class ' + self.__class__
