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

# MODIFICATION: new class
# 'enumerated' class to store types of intruments   
class InstrumentType(Enum):
    GUITAR = "Guitar"
    BANJO = "Banjo"
    DOBRO = "Dobro"
    FIDDLE = "Fiddle"
    BASS = "Bass"
    MANDOLIN = "Mandolin"
    SAX = "Sax"
    UNSPECIFIED = "Unspecified"

# MODIFICATION: new class instrument 
# Now all instruments are objects of this class, without any subclass
class Instrument():
    def __init__(self, serial_number, price, spec):
        self.serialNum = serial_number
        self.price = price
        self.spec = spec #spec is an InstrumentSpec object

    # methods to return intruments specifications
    def getSerial_number(self):
        return self.serialNum

    def getPrice(self):
        return self.price

    def setPrice(self, new_price):
        self.price = new_price

    def getSpec(self):
        return self.spec
    
    def __str__ (self):
        return f"SERIAL NUMBER: {self.serialNum}\nPRICE: R${self.price}\n{self.spec}"

# MODIFICATION: new class InstrumentSpec
# Now all instruments' specifications are objects of this class, without any subclass
class InstrumentSpec():
    def __init__(self, properties=None):
        if properties is None:
            self.properties = {}
        else:
            self.properties = properties.copy()

    # MODIFICATION
    # method to retrun instruments' specific property
    def getProperty(self, property_name):
        return self.properties.get(property_name)

    # MODIFICATION
    # new method to return instruments's properties
    def getProperties(self):
        return self.properties

    # MODIFICATION
    # new query method to match intruments during the searhcing
    def matches(self, other_spec):
        for property_name in other_spec.getProperties():
            if self.properties.get(property_name) != other_spec.getProperty(property_name):
                return False
        return True

# class Inventory, to store intruments objects
class Inventory():
    def __init__(self):
        self.inventory = []

    # method to include new instruments objects into the inventory list object
    def addInstrument(self, serial_number, price, spec):
        instrument = Instrument(serial_number, price, spec)
        self.inventory.append(instrument)

     # search guitars or mandolins by its serial number
    def getInstrument(self, serial_number):
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    # MODIFICATION: new query method
    def search(self, search_spec):
        # search_spec is a InstrumentSpec object
        matching_instruments = []
        for instrument in self.inventory:
            if instrument.getSpec().matches(search_spec):
                matching_instruments.append(instrument)
        return matching_instruments
    
# MODIFICATION: new method with ready dictionaries to use as Specifications
def initialize_inventory(inventory):
    properties = {
        "Instrument Type": InstrumentType.GUITAR.value,
        "Builder": Builder.COLLINGS.value,
        "Model": "CJ",
        "Type": Type.ACOUSTIC.value,
        "Num Strings": 6,
        "Top Wood": Wood.INDIAN_ROSEWOOD.value,
        "Back Wood": Wood.SITKA.value
    }
    inventory.addInstrument("11277", 3999.95, InstrumentSpec(properties))

    properties = {
        "Instrument Type": InstrumentType.GUITAR.value,
        "Builder": Builder.GIBSON.value,
        "Model": "Les Paul",
        "Type": Type.ELECTRIC.value,
        "Num Strings": 6,
        "Top Wood": Wood.MAPLE.value,
        "Back Wood": Wood.MAPLE.value
    }
    inventory.addInstrument("70108276", 2295.95, InstrumentSpec(properties))

    properties = {
        "Instrument Type": InstrumentType.MANDOLIN.value,
        "Builder": Builder.GIBSON.value,
        "Model": "F5-G",
        "Type": Type.ACOUSTIC.value,
        "Top Wood": Wood.MAPLE.value,
        "Back Wood": Wood.MAPLE.value,
        "Style": Style.A.value
    }
    inventory.addInstrument("9019920", 5495.99, InstrumentSpec(properties))

    properties = {
        "Instrument Type": InstrumentType.BANJO.value,
        "Builder": Builder.GIBSON.value,
        "Model": "RB-3",
        "Type": Type.ACOUSTIC.value,
        "Num Strings": 5,
        "Back Wood": Wood.MAPLE.value
    }
    inventory.addInstrument("8900231", 2945.95, InstrumentSpec(properties))

# FIFTH VERSION TESTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
inventory = Inventory()
initialize_inventory(inventory)

properties = {
    "Builder": Builder.GIBSON.value,
    "Back Wood": Wood.MAPLE.value
}
    
client_spec = InstrumentSpec(properties)
matching_instruments = inventory.search(client_spec)
    
if matching_instruments:
    for instrument in matching_instruments:
        spec = instrument.getSpec()
        print(f"\033[36m{spec.getProperty('Instrument Type')}\033[0m")
        for property_name, property_value in spec.getProperties().items():
            if property_name == "Instrument Type":
                continue
            print (f"\033[31m{property_name}:\033[0m {property_value}")
        print (f"It can be yours for just $\033[32m{instrument.getPrice()}\033[0m")
        print()
else:
    print("\033[34m\nNothing Found\033[0m\n")
