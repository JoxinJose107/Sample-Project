#***********Multilevel Inheritence*************

class MusicalInstruments:
    numberOfMajorKeys=12

class StringInstruments(MusicalInstruments):
    typeWood="ToneWood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings=6
        print("This guitar consists of {} strings. It is made up of {}  and it can paly {} keys".format(self.numberOfStrings,self.typeWood,self.numberOfMajorKeys))

guitar=Guitar()