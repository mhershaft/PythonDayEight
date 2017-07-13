class Animal(object):
    def __init__(self,texture,predator,prey,number_of_legs):
        self.texture=texture
        self.predator=predator
        self.prey=prey
        self.number_of_legs=number_of_legs
    def prey2(self):
        print ("I hunt for " + self.prey + ".")
    def drink_prey(self):
        print ("I drink " + self.prey + "'s juice.")
    def texture2(self):
        print (self.texture + " is my texture.")
    def predator2(self):
        print ("My main predator is " + self.predator + ".")
    def number_of_legs2(self):
        print ("I have " + self.number_of_legs + " legs.")
animal_name=raw_input("Animal Name\n")
name=Animal(raw_input("Texture\n"),raw_input("Predator\n"),raw_input("Prey\n"),raw_input("Leg Count\n"))
print "\nMy name is " + animal_name + "."
name.prey2()
name.drink_prey()
name.texture2()
name.predator2()
name.number_of_legs2()