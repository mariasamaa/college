# import enum method to avoid possible comparisons with strings later
from enum import Enum 

# 'enumerated' class to store brands that produce instruments
class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

# 'enumerated' class to store instrument types
class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "eletric"

# 'enumerated' class to store kinds of wood used to produce instruments
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
    
# 'enumerated' class to store types of mandolin
class Style(Enum):
    A = "a"
    F = "f"

# MODIFICATION: New class Instrument, with all instruments common specifications
class InstrumentSpec():
    def __init__(self, builder, model, type, back_wood, top_wood):
        self._builder = builder
        self._model = model.lower()
        self._type = type
        self._backWood = back_wood
        self._topWood = top_wood

    # methods to return instruments' specifications 
    def _getBuilder(self):
        return self._builder
  
    def _getModel(self):
        return self._model
  
    def _getType(self):
        return self._type
  
    def _getBackWood(self):
        return self._backWood
  
    def _getTopWood(self):
        return self._topWood

    # method to match instruments, used at the inventory
    def _matches (self, searched_instrument): 
        if self._builder != searched_instrument._getBuilder():
            return False
        if self._model != "" and self._model != searched_instrument._getModel():
            return False
        if self._type != searched_instrument._getType():
            return False
        if self._backWood != searched_instrument._getBackWood():
            return False
        if self._topWood != searched_instrument._getTopWood():
            return False
        return True

    # method to return instruments's specifications as a string
    def __str__(self):
        return f"\033[31mBUILDER:\033[0m{self._builder}\n\033[31mMODEL:\033[0m{self._model}\n\033[31mTYPE:\033[0m{self._type}\n\033[31mBACK WOOD:\033[0m{self._backWood}\n\033[31mTOP WOOD:\033[0m{self._topWood}\n"

# create the class for "guitar" objects' specifications
class GuitarSpec(InstrumentSpec):
    def __init__(self, builder, model, typeg, back_wood, top_wood, strings):
        super().__init__( builder, model, typeg, back_wood, top_wood)
        self._numStrings = strings

    # method that will return guitars specifications
    def _getNumStrings(self):
        return self._numStrings
    
    # method to match searched guitars with inventory guitars.
    def _matches(self, searched_instrument):
        if not super()._matches(searched_instrument):
            return False
        if self._numStrings != searched_instrument._numStrings:
            return False
        return True
    
    # return a string with all specficiations
    def __str__(self):
        return f"\033[31mBUILDER:\033[0m{self._builder}\n\033[31mMODEL:\033[0m{self._model}\n\033[31mTYPE:\033[0m{self._type}\n\033[31mBACK WOOD:\033[0m{self._backWood}\n\033[31mTOP WOOD:\033[0m{self._topWood}\n\033[31mSTRINGS:\033[0m{self._numStrings}\n"

# MODIFICATION: New class MandolinSpec added to store mandolin's specifications
class MandolinSpec(InstrumentSpec):
    def __init__(self, builder, model, typeg, back_wood, top_wood, style):
        super().__init__( builder, model, typeg, back_wood, top_wood)
        self._style = style

    # method that will return guitars specifications
    def _getStyle(self):
        return self._style
    
    # method to match searched guitars with inventory guitars.
    def _matches(self, searched_instrument):
        if not super()._matches(searched_instrument):
            return False
        if self._style != searched_instrument._style:
            return False
        return True
    
    # return a string with all specficiations
    def __str__(self):
        return f"\033[34mBUILDER:\033[0m{self._builder}\n\033[34mMODEL:\033[0m{self._model}\n\033[34mTYPE:\033[0m{self._type}\n\033[34mBACK WOOD:\033[0m{self._backWood}\n\033[34mTOP WOOD:\033[0m{self._topWood}\n\033[34mSTYLE:\033[0m{self._style}"

# MODIFICATION: New class instrument, a father class to be a base for specif instruments classes
# Note: when create new classes for new intruments, they will 'be part of' Instruments.
class Instrument():
    def __init__ (self, serial_num, price, spec): #spec will be a instrument spec object
        self._serialNum = serial_num
        self._price = price
        self._spec = spec
        
    def __str__ (self):
        return f"{self._spec}"

# MODIFICATION
# create a class for Guitar objects
class Guitar (Instrument):
    def __init__ (self, serial_num, price, spec):
        super().__init__(serial_num, price, spec)
    
    def __str__ (self):
        return f"{self._spec}"

# MODIFICATION   
# create a class for Mandolin objects 
class Mandolin (Instrument):
    def __init__ (self, serial_num, price, spec):
        super().__init__(serial_num, price, spec)
    
    def __str__ (self):
        return f"{self._spec}"

# create class inventory to store all objects 
class Inventory():
    def __init__(self):
        self._inventory = []
    
    # include new guitar or mandolin at the inventory
    def _addInstrument(self, serial_number, price, spec): #spec is a instrument spec, might be guitar or mandolin
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serial_number, price, spec)
        if isinstance(spec, MandolinSpec):
            instrument = Mandolin(serial_number, price, spec)
        self._inventory.append(instrument)
  
    # search guitars or mandolins by its serial number
    def _getInstrument(self, serial_number):
        for instrument in self._inventory:
            if instrument._serialNum == serial_number:
                return instrument
        return None
  
  # MODIFICATION
  # search guitars or mandolins  by its specifications
  # 'searched_instrument' is also a object GuitarSpec or MandolinSpec 
    def _searchInstruments(self, searched_instrument):  
        if isinstance(searched_instrument, GuitarSpec):
            return [guitar for guitar in self._inventory if isinstance(guitar, Guitar) and guitar._spec._matches(searched_instrument)]
        if isinstance(searched_instrument, MandolinSpec):
            return [mandolin for mandolin in self._inventory if isinstance(mandolin, Mandolin) and mandolin._spec._matches(searched_instrument)]
        return None

# FOURTH VERSION TESTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Rick has a Guitar Store, and needs a system to consult your inventory
# Each guitar or mandolin has a serial number, a price, a builder, a model, a type, a back wood, and a top wood
# More recently, it has number of strings for guitars and style for mandolins

# create an inventory object
rick_inventory = Inventory()

# add objects guitar and mandolin in rick's inventory
spec1 = GuitarSpec(Builder.FENDER, "stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
rick_inventory._addInstrument("V95693", 1499.95, spec1)
rick_inventory._addInstrument("V99999", 1599.95, spec1)
spec2 = MandolinSpec(Builder.FENDER, "stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, Style.A)
rick_inventory._addInstrument("M12345", 1000.00, spec2)

# a client (named ERIN) wants a specific guitar
# create an object guitar with erin's specifications
erin_specs = GuitarSpec(Builder.FENDER, "stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)

# search for erin's guitar at rick's inventory
guitar = rick_inventory._searchInstruments(erin_specs)
if guitar != None:
    for g in guitar:
        print (f"{g}")
else:
    print ("\033[31mNothing Found\033[0m")

# a client (named BOB) wants a specific mandolin
# create an object mandolin with bob's specifications
bob_specs = MandolinSpec(Builder.FENDER, "stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, Style.A)

# search for bob's mandolin at rick's inventory
mandolin = rick_inventory._searchInstruments(bob_specs)
if mandolin != None:
    for m in mandolin:
        print (f"{m}")
else:
    print ("\033[31mNothing Found\033[0m")