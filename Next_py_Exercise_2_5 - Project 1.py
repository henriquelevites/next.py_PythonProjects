class Animal:
    """
    A class used to represent an animal
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger = 0):
        """Sets the initial values for the attributes of animal
        :param name: name of animal
        :param hunger: degree of hunger (default value = 0)
        :type name: string
        :type hunger: int
        :return: None
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """Gets the name of the animal
        :return: The name of animal
        :rtype: string
        """
        return self._name

    def is_hungry(self):
        """Indicates if the animal is hungry or not.
        :return: True or False
        :rtype: boolean
        """
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        """Subtracts one "point" from the degree of hunger of the animal
        :return: None
        """
        self._hunger -= self._hunger

    def talk(self):
        pass

class Dog(Animal):
    """
    A subclass used to represent an animal of type dog.
    """
    def talk(self):
        """Prints to screen the words the animal dog knows to talk.
        :return: None
        """
        super().talk()
        print("woof woof")

    def fetch_stick(self):
        """Unique method to animal dog that prints a specific caption to screen.
        :return: None
        """
        print("There you go, sir!\n")

class Cat(Animal):
    """
    A subclass to represent an animal of type cat
    """
    def talk(self):
        """Prints to screen the words the animal cat knows to talk.
        :return: None
        """
        super().talk()
        print("meow")

    def chase_laser(self):
        """Unique method to animal cat that prints a specific caption to screen.
        :return: None
        """
        print("Meeeeow\n")

class Skunk(Animal):
    """
    A subclass to represent an animal of type skunk
    """
    def __init__(self, name, hunger, stink_count=6):
        """Initiates an instance of skunk with another attribute (in addition to name and degree of hunger)
        :param name: name of animal
        :param hunger: degree of hunger
        :param stink_count: degree of stink (default degree is 6)
        :type name: string
        :type hunger: int
        :type stink_count: int
        :return: None
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """Prints to screen the words the animal skunk knows to talk.
        :return: None
        """
        super().talk()
        print("tsssss")

    def stink(self):
        """Unique method to animal skunk that prints a specific caption to screen.
        :return: None
        """
        print("Dear lord!\n")

class Unicorn(Animal):
    """
    A subclass to represent an animal of type unicorn
    """
    def talk(self):
        """Prints to screen the words the animal unicorn knows to talk.
        :return: None
        """
        super().talk()
        print("Good day, darling")

    def sing(self):
        """Unique method to animal unicorn that prints a specific caption to screen.
        :return: None
        """
        print("I'm not your toy...\n")

class Dragon(Animal):
    """
    A subclass to represent an animal of type dragon
    """
    def __init__(self, name, hunger, color="Green"):
        """Initiates an instance of dragon with another attribute (in addition to name and degree of hunger)
        :param name: name of animal
        :param hunger: degree of hunger
        :param color: color of dragon. Default color is green.
        :type name: string
        :type hunger: int
        :type color: string
        :return: None
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """Prints to screen the words the animal dragon knows to talk.
        :return: None
        """
        super().talk()
        print("Raaaawr")

    def breath_fire(self):
        """Unique method to animal dragon that prints a specific caption to screen.
        :return: None
        """
        print("$@#$#@$\n")


def main():
    """Executes the following tasks:
    · Creates one animal of each type (Dog, Cat, Skunk, Unicorn and Dragon), and initiates it with attributes values '_name' and '_hunger'.
    · The function saves the instances of the animals in a list named 'zoo_lst'.
    · The function creates new animals of each type, and updates the 'zoo_lst' list to also include the instances of these new animals as elements.
    · The function goes over all animals in 'zoo_lst' in a for loop. For each hungry animal, it prints the animal's type (type, name of the subclass)
      and its name, and after then the function feeds the animal till it is not more hungry (i.e., till degree of hunger is 0).
    · After the stage of feed, the method 'talk' is called for all the animals.
    · After calling the method 'talk' for each animal, the function calls the method that is unique to animal, according to its type.    
    """
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky", 0), Unicorn("Keith", 7), Dragon("Lizzi", 1450)]
    new_animals_lst = [Dog("Doggo", 80), Cat("Kitty", 80), Skunk("Stinky Jr.", 80), Unicorn("Clair", 80), Dragon("McFly", 80)]
    for new_animal in new_animals_lst:
        zoo_lst.append(new_animal)
    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__, animal.get_name()) # Adding '__name__' returns a readable string representation of a class name.
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        else:
            animal.breath_fire()

    print(Animal.zoo_name)  # call the class attribute via class name.

main()