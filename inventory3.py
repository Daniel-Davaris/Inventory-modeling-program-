class Pack():

    def __init__(self, cap, contents=None):
        self.cap = cap

        if contents is None:
            self.contents = []
        else:
            self.contents = contents
        
    def add_item(self, obj):
        if len(self.contents) > self.cap - 1:
            print("Your pack is full")
        else:
            self.contents.append(obj)
            print("success")

        
    
    def drop_item(self, obj):
        if len(self.contents) == 0:
            print("You pack is empty")
        else:
            self.contents.remove(obj)
            print("success")
           

    def display_contents(self):
        for obj in self.contents:
            return obj

    def display_size(self):
        return self.cap

    def display_current(self):
        return len(self.contents)

class Item():

    def __init__(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def __str__(self):
        return str(self.size)

    

item_1 = Item(1)
pack_1 = Pack(3, [])

print("Your pack can hold",pack_1.display_size(),"items")
while True:
    inp = input("Command Line: ")
    if inp == "":
        break
    if inp == "add":
        print("attempting to add item")
        pack_1.add_item(item_1)
        continue 
    if inp == "drop":
        print("attempting to drop item")
        pack_1.drop_item(item_1)
        continue
    if inp == "display":
        print(pack_1.display_contents())
        continue
    if inp == "current":
        print(pack_1.display_current())
        continue
    



"""
class Potion(Item):

    def __init__(self, potency, size):
        Item.__init__(self, potency)
        self.potency = potency
        self.size = size

    def use(self):
        return self.potency

    def __str__(self):
        return "You have used your %s" % (self)


    
class Weapon(Item):

    def __init__(self, power, range):
        Item.__init__(self, power, range)
        self.power = power
        self.range = range
    
    def getPower(self):
        return self.power

    def getRange(self):
        return self.range
    

class Axe(Weapon):

    def __init__(self):
        Weapon.__init__(self, chop, swing, size)
        self.chop = chop
        self.swing = swing
        self.size = size

    def chop(self):
        return self.chop
    
    def swing(self):
        return self.swing

class Sword(Weapon):

    def __init__(self):
        Weapon.__init__(self, swing, thrust, size)
        self.swing = swing
        self.thrust = thrust
        self.size = size
    def swing(self):
        return self.swing

    def thrust(self):
        return self.thrust


#items
    #axes
battle_axe = Axe(2,7,2)
war_axe = Axe(9,9,2)
empire_axe = Axe(3,4,2)
    #swords
short_sword = Sword(3,7,2)
long_sword = Sword(6,6,2)
double_sword = Sword(4,8,2)
    #potions
dragon_potion = Potion(7,1)
magic_potion = Potion(5,1)
evil_potion = Potion(9,1)
    #packs

list1 = [
    pack1 = Pack(4, 0)
    pack2 = Pack(8, 0)
    pack3 = Pack(16, 0)
    pack4 = Pack(20, 0)
]
    


cap = 0

print("PRESS ENTER TO START")
inp1 = input("")
if inp1 == "":
    print("How big do you want your inventory to be?")
    print(list1)
    inp2 = int(input("Enter Number: "))
    print("Pack -",inp2, "selected")
    if inp2 == 1:
        cap = 4
    if inp2 == 2:
        cap = 8
    if inp2 == 3:
        cap = 16
    if inp2 == 4:
        cap = 20
print("Inventory-size: "cap)
print("Inventoru-usage: "

"""


   


    
