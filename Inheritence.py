
#************Inheritence******************8

# In inheritace a class can inherit all the attributes of another class
class Chef:
    def make_butter(self):
        print("Chef making butter")

    def make_chicken(self):
        print("Chef making chicken")

    def make_rice(self):
        print("Chef making rice")

# myChef=Chef() 
# myChef.make_butter()

class ChineesChef(Chef):
    def make_fried(self):
        print("Chef making fried rice")

mychef=ChineesChef()
mychef.make_butter()
mychef.make_chicken()
mychef.make_fried()
mychef.make_rice()