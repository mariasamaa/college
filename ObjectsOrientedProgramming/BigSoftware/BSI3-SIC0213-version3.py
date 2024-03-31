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

# MODIFICATION: now class GuitarSpec has the atribute numSpring (number of strings)
class GuitarSpec():
    def __init__(self, builder, model, typeg, back_wood, top_wood, strings):
        self._builder = builder
        self._model = model.lower() 
        self._guitarType = typeg
        self._backWood = back_wood
        self._topWood = top_wood
        self._numStrings = strings

    # methods to return guitars specifications 
    def _getBuilder(self):
        return self._builder
  
    def _getModel(self):
        return self._model
  
    def _getGuitarType(self):
        return self._guitarType
  
    def _getBackWood(self):
        return self._backWood
  
    def _getTopWood(self):
        return self._topWood

    def _getNumStrings(self):
        return self._numStrings

    # MODIFICATION: query method to search and match guitars now is into GuitarSpec class
    # this method is called into Inventory class
    def matches (self, guitar): #guitar is a GuitarSpec object
        if self._builder != guitar._getGuitarSpec()._getBuilder():
            return False
        if self._model != "" and self._model != guitar._getGuitarSpec()._getModel():
            return False
        if self._guitarType != guitar._getGuitarSpec()._getGuitarType():
            return False
        if self._backWood != guitar._getGuitarSpec()._getBackWood():
            return False
        if self._topWood != guitar._getGuitarSpec()._getTopWood():
            return False
        if self._numStrings != guitar._getGuitarSpec()._getNumStrings():
            return False
        return True

    # method to return guitar's specifications as a string
    def __str__(self):
        return f"\033[31mBUILDER:\033[0m{self._builder}\n\033[31mMODEL:\033[0m{self._model}\n\033[31mTYPE:\033[0m{self._guitarType}\n\033[31mBACK WOOD:\033[0m{self._backWood}\n\033[31mTOP WOOD:\033[0m{self._topWood}\n\033[31mSTRINGS:\033[0m{self._numStrings}"

# create the class for objects guitar
class Guitar():
    def __init__(self, serial_number, price, specs):
        self._serialNum = serial_number
        self._priceTag = price
        # MODIFICARION: specs is a guitarSpec object, specified as a variable out of the class
        self._guitarSpec = specs 

    # methods to return guitars specifications
    def _getSerialNum(self):
        return self._serialNum

    def _getPriceTag(self):
        return self._priceTag
  
    def _getGuitarSpec(self):
        return self._guitarSpec
  
    # method to return guitar's specifications as a strin
    def __str__(self):
        return  f"\033[34mSERIAL NUMBER:\033[0m{self._serialNum}\n\033[31mPRICE:\033[0m R${self._priceTag}\n{self._guitarSpec}\n"
  
# create class inventory to store objects guitar
class Inventory():
    def __init__(self):
        self.guitars = []
    
     # method to include new objects 'Guitar' at the inventory
    def _addGuitar(self, serial_number, price, specs):
        guitar = Guitar(serial_number, price, specs)
        self.guitars.append(guitar)
  
    # search guitar by its serial number
    def _getGuitar(self, serial_number):
        for guitar in self.guitars:
            if guitar._getSerialNum() == serial_number:
                return guitar
        return None
  
    # MODIFICATION: Query method now calls for a method into GuitarSpec class
    def _searchGuitars(self, searchingGuitar):
        # searchingGuitar is also a object 'guitar'
        matching_guitars = []
        for guitar in self.guitars:
            if guitar._getGuitarSpec().matches(searchingGuitar):
                matching_guitars.append(guitar)
        return matching_guitars if len(matching_guitars) != 0 else None     

# THIRD VERSION TESTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Rick has a Guitar Store, and needs a system to consult your inventory
# Each guitar has a serial number, a price, a builder, a model, a type, a back wood, and a top wood

# create an inventory object
rick_inventory = Inventory()

# add objects guitar in rick's inventory
spec1 = GuitarSpec (Builder.FENDER.value, "Stratocastor", GuitarType.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value, 5)
rick_inventory._addGuitar('0000', 1499.99, spec1)
rick_inventory._addGuitar('0001', 1499.99, spec1)

spec2 = GuitarSpec(Builder.GIBSON.value, "Ibanez", GuitarType.ACOUSTIC.value, Wood.SITKA.value, Wood.MAPLE.value, 12)
rick_inventory._addGuitar('0003', 999.90, spec2)

# a client (named Erin) wants a specific guitar
# create an object guitar with erin's specifications
erin_specs= GuitarSpec (Builder.FENDER.value, "Stratocastor", GuitarType.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value,5)
erin_guitar = Guitar (' ', 0, erin_specs)

# search for erin's guitar at rick's inventory
guitar = rick_inventory._searchGuitars(erin_guitar)
if guitar != None:
    for g in guitar:
        print (f"{g}")
else:
    print ("\033[31mNothing Found\033[0m")