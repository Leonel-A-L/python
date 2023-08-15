class Prodacer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = 'repaired'

class AnakinsPod(Prodacer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Prodacer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        self.condition = 'trashed'

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply).
# Answer - 
# Encapsulation because we are putting multiple related code into one class.
# Inheritance- because we are getting a class and adding it to another class.
# Polymorphism because we are calling another class into another and using it differently.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# Answer - Based on the codes i know this one is easier.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# Answer - Made it easier to understand and use the codes in a similar but different method.
