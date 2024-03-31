# import Enum method (to avoid possible comparisons)
from enum import Enum

# class to store brands that produce guitars
class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

# class to store guitar types
class GuitarType(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"

# class to store kinds of wood used to produce guitars
class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"
  
# class for the "guitar" objects
class Guitar():
    def __init__(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        self.serialNum = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.backWood = back_wood
        self.topWood = top_wood

    # methods to return guitars specifications
    def getSerialNum(self):
        return self.serialNum

    def getBuilder(self):
        return self.builder

    def getGuitarType(self):
        return self.typeg

    def getModel(self):
        return self.model.lower() # lower() was included to avoid comparisons

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood

    def getPrice(self):
        return self.price

    # method used to change guitar's price
    def setPrice(self, new_price):
        self.price = new_price
    
    # method to return the guitar object as a string
    def __str__ (self):
        return f"SERIAL NUM:{self.serialNum}\nBUILDER:{self.builder}\nTYPE:{self.typeg}\nMODEL:{self.model}\nBack Wood:{self.backWood}\nTop Wood:{self.topWood}\nPROCE: R${self.price}"

# create class inventory to store objects guitar
class Inventory():
    def __init__ (self):
        self.guitars = []
    
    # method to include new objects 'Guitar' at the inventory
    def addGuitar (self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, typeg, back_wood, top_wood)
        self.guitars.append(guitar)

    # query method to find a guitar by your serial number
    def getGuitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None 
    
    # QUERY METHOD BY SPECIFICATIONS
    def searchGuitar(self, searchingGuitar):
        results = []
        for guitar in self.guitars:
            if searchingGuitar.getBuilder() != guitar.getBuilder():
                continue
            if searchingGuitar.getModel() and searchingGuitar.getModel() != "" and searchingGuitar.getModel() != guitar.getModel():
                continue
            if searchingGuitar.getGuitarType() != guitar.getGuitarType():
                continue
            if searchingGuitar.getBackWood() != guitar.getBackWood():
                continue
            if searchingGuitar.getTopWood() != guitar.getTopWood():
                
                continue
            print (f'\033[31m{guitar}\0330m\n')
    
    # method to return the inventory as a string
    def __str__ (self):
        return f"Inventory List:\n{[i for i in self.guitars]}"

# FISRT VERSION TESTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Rick has a Guitar Store, and needs a system to consult your inventory
# Each guitar has a serial number, a price, a builder, a model, a type, a back wood, and a top wood

# create an inventory object
rick_inventory = Inventory()

# add objects guitar in rick's inventory
rick_inventory.addGuitar('0000', 1499.99, Builder.FENDER, "Stratocastor", GuitarType.ELETRIC, Wood.ALDER, Wood.ALDER)
rick_inventory.addGuitar('0001', 1499.99, Builder.FENDER, "Stratocastor", GuitarType.ELETRIC, Wood.ALDER, Wood.ALDER)

# a client (named Erin) wants a specific guitar
# create an object guitar with erin's specifications
erin_guitar = Guitar (' ', 0, Builder.FENDER, "Stratocastor", GuitarType.ELETRIC, Wood.ALDER, Wood.ALDER)

# search for erin's guitar at rick's inventory
guitar = rick_inventory.searchGuitar(erin_guitar)
find_text = f"Results:\n{guitar}"
out_text = "Nothing found"
print (find_text) if guitar is not None else (out_text)
    