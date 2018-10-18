class Person:
    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__ (self):

        return "{} {}".format(self.firstname, self.lastname)


class Student(Person):
    def __init__ (self, firstname, lastname, school = ""):
        super().__init__(firstname, lastname)
        self.school = school

    def __str__ (self):
        return "{} [{}]".format(
            super().__str__(),
            self.school)
        
    def eat(self, food)
        print("{} will eat {}.".format(self, food))

if __name__ == "__main__":

    mara = Person ("Marge Angela", "Matamorosa")
    print (mara)

    mara.eat("chicken")

    jessie = Student("Jessie", "Mendiola", "CSNHS")
    print (jessie)