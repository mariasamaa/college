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

# create a new class with guitar specifications
class GuitarSpec():
    def __init__(self, builder, model, typeg, back_wood, top_wood):
        self._builder = builder
        self._model = model.lower()
        self._guitarType = typeg
        self._backWood = back_wood
        self._topWood = top_wood

    # methods to return guitar's specifications 
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
  
    # method to return guitar's specifications as a string
    def __str__(self):
        return f"\033[31mBUILDER:\033[0m{self._builder}\n\033[31mMODEL:\033[0m{self._model}\n\033[31mTYPE:\033[0m{self._guitarType}\n\033[31mBACK WOOD:\033[0m{self._backWood}\n\033[31mTOP WOOD:\033[0m{self._topWood}\n"

# create the class for objects guitar
class Guitar():
    def __init__(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        self._serialNum = serial_number
        self._priceTag = price
        # specifications is a GuitatSpec object as an atribute
        self._guitarSpec = GuitarSpec(builder, model, typeg, back_wood, top_wood)

    # methods to return guitars specifications
    def _getSerialNum(self):
        return self._serialNum

    def _getPriceTag(self):
        return self._priceTag
  
    def _getGuitarSpec(self):
        return self._guitarSpec
  
    # method to return guitar's specifications as a string
    def __str__(self):
        return  f"\033[34mSERIAL NUMBER:\033[0m{self._serialNum}\n\033[31mPRICE:\033[0m R${self._priceTag}\n{self._guitarSpec}"
  
# create class inventory to store objects guitar
class Inventory():
    def __init__(self):
        self.guitars = []
    
    # method to include new objects 'Guitar' at the inventory
    def _addGuitar(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, typeg, back_wood, top_wood)
        self.guitars.append(guitar)
  
    # query method to find a guitar by your serial number
    def _getGuitar(self, serial_number):
        for guitar in self.guitars:
            if guitar._getSerialNum() == serial_number:
                return guitar
        return None
  
    # QUERY METHOD BY SPECIFICATIONS
    def _searchGuitars(self, searchingGuitar):
        # 'searchingGuitar' is also a Guitar object
        results = []
        for guitar in self.guitars:
            if searchingGuitar._getGuitarSpec()._getBuilder() != guitar._getGuitarSpec()._getBuilder():
                continue
            if searchingGuitar._getGuitarSpec()._getModel() and searchingGuitar._getGuitarSpec()._getModel() != "" and searchingGuitar._getGuitarSpec()._getModel() != guitar._getGuitarSpec()._getModel():
                continue
            if searchingGuitar._getGuitarSpec()._getGuitarType() != guitar._getGuitarSpec()._getGuitarType():
                continue
            if searchingGuitar._getGuitarSpec()._getBackWood() != guitar._getGuitarSpec()._getBackWood():
                continue
            if searchingGuitar._getGuitarSpec()._getTopWood() != guitar._getGuitarSpec()._getTopWood():
                continue
            # print (f"\033[34m{guitar}\033[0m\n")
            results.append(f"{guitar}")
        return results if len(results) != 0 else None
     

# SECOND VERSION TESTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Rick has a Guitar Store, and needs a system to consult your inventory
# Each guitar has a serial number, a price, a builder, a model, a type, a back wood, and a top wood

# create an inventory object
rick_inventory = Inventory()

# add objects guitar in rick's inventory
rick_inventory._addGuitar('0000', 1499.99, Builder.FENDER.value, "Stratocastor", GuitarType.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
rick_inventory._addGuitar('0001', 1499.99, Builder.FENDER.value, "Stratocastor", GuitarType.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)

# a client (named Erin) wants a specific guitar
# create an object guitar with erin's specifications
erin_guitar = Guitar (' ', 0, Builder.FENDER.value, "Stratocastor", GuitarType.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)

# search for erin's guitar at rick's inventory
guitar = rick_inventory._searchGuitars(erin_guitar)
if guitar is not None:
    for g in guitar:
        print (f"{g}")
else:
    print ("Nothing Found")