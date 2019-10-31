class Pet:
    def __init__(self, fur, breed, call):
        self.f = fur
        self.b = breed
        self.c = call
    def eat(self):
        if self.c == 'meow':
            print("The pet is eating fish,", self.c)
        elif self.c == 'woof':
            print("The pet is chewing bone,", self.c)
class cat(Pet):
    def __init__(self, fur, breed):
        Pet.__init__(self, fur, breed, 'meow')
        print('The ')
class dog(Pet):
    def __init__(self,fur,breed):
        Pet.__init__(self,fur,breed,'woof')
mykitty = cat('white', 'siam')
mykitty.eat()
mylassie = dog('White','Collar')
mylassie.eat()