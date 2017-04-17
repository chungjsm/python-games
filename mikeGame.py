import random

def leftRoom(hero):
    myHero = hero
    print "You've entered the left room."
    print "There is a treasure chest on the ground."
    print "There is also an enemy bat flying around."
    print "Do you fight the bat (fight bat), open the chest (open chest), or leave the room (leave)?"

    batMonster = bat(50, False)
    chest_opened = False

    while True:
        choice = raw_input("> ")

        if choice == "open chest" and not chest_opened:
            if not batMonster.batDead:
                print "The bat attacks you while you open the chest"
                for i in range(1,3):
                    myHero.takeDamage(batMonster.attack())
                    print "You have %d HP left!" % myHero.HP
            print "You open the chest."
            if myHero.has_shield == False:
                print "There was a shield inside!"
            else:
                print "Looks like someone looted this chest already!"
            chest_opened = True
            myHero.has_shield = True
        elif choice == "fight bat" and not batMonster.batDead:
            while True:
                if batMonster.batDead == True:
                    print "The bat dropped a small health potion."
                    potion = random.randint(5,20)
                    myHero.HP += potion
                    print "Your HP increased %d points to %d!" % (potion, myHero.HP)
                    break
                else:
                    print "The bat attacks you for %d damage." % myHero.takeDamage(batMonster.attack())
                    print "You have %d HP left!" % hero.HP
                    print "You take a swing at the bat!"
                    batMonster.takeDamage(myHero.attack())
                    if batMonster.batDead == False:
                        print "The bat has %d HP left!" % batMonster.HP
        elif choice == "leave":
            mainRoom(myHero)
        else:
            print "Not a valid choice."

def frontRoom(hero):
    myHero = hero

    print "You've entered the front room."
    print "There is a large, locked door at the end of the room."
    print "You also spot pots to the left and right of the door."
    print "Do you inspect either the left pots (left pots) or the right pots (right pots)?"
    print "Do you unlock the door (unlock door) or leave the room (leave)?"

    while True:
        choice = raw_input("> ")

        if choice == "unlock door":
            print "You walk up to the large door."
            if myHero.has_key:
                print "You unlock the door with the key and enter the room."
                bossRoom(myHero)
            else:
                print "The door is locked!"
        elif choice == "left pots":
            print "You walk towards the left pots."
            print "You have a sudden urge to break them."
            print "Do you break the pots? Yes or no?"
            decision = raw_input("> ")
            while True:
                if decision == "yes":
                    print "You smash the pots!"
                    if myHero.has_key == False:
                        print "There was a key inside!"
                        myHero.has_key = True
                        break
                    else:
                        print "There was nothing in them!"
                        break
                elif decision == "no":
                    print "You return to the center of the room."
                    break
                else:
                    print "Not a valid choice."
                    break
        elif choice == "right pots":
            print "You walk towards the right pots."
            print "You have a sudden urge to break them."
            print "Do you break the pots? Yes or no?"
            decision = raw_input("> ")
            while True:
                if decision == "yes":
                    print "You smash the pots!"
                    if myHero.potions == False:
                        print "There were health potions inside!"
                        myHero.HP += 25
                        print "Your HP increased by %d points to %d!" % (25, myHero.HP)
                        myHero.potions = True
                        break
                    else:
                        print "There was nothing in them!"
                        break
                elif decision == "no":
                    print "You return to the center of the room."
                    break
                else:
                    print "Not a valid choice."
                    break
        elif choice == "leave":
            print "You head back to the main room."
            mainRoom(myHero)
        else:
            print "Not a valid choice."

def rightRoom(hero):
    myHero = hero
    print "You've entered the room on the right."
    print "There is a chest in the middle of the room."
    print "Do you open the chest (open chest) or leave the room (leave)?"

    chest_opened = False

    while True:
        choice = raw_input("> ")

        if choice == "open chest" and not chest_opened:
            print "You've opened the chest!"
            if myHero.has_sword == False:
                print "There was a sword inside!"
            else:
                print "Looks like someone looted this chest already!"
            chest_opened = True
            myHero.has_sword = True
        elif choice == "leave":
            print "You leave the room."
            mainRoom(myHero)
        else:
            print "Not a valid choice."

def bossRoom(hero):
    myHero = hero
    bossMonster = boss(150, False)

    print "You've entered the boss room."
    print "There is a giant armored caterpillar in the room."
    print "Do you fight (fight) or flee (flee)?"

    while True:
        choice = raw_input("> ")

        if choice == "fight":
            while True:
                if bossMonster.bossDead == True:
                    endGame()
                else:
                    print "The boss attacks you for %d damage!" % myHero.takeDamage(bossMonster.attack())
                    print "You have %d HP left!" % hero.HP
                    print "You take a swing at the monster!"
                    bossMonster.takeDamage(myHero.attack())
                    if bossMonster.bossDead == False:
                        print "The boss has %d HP left!" % bossMonster.HP
        elif choice == "flee":
            print "The door is locked! You can't escape!"
            for i in range(1,3):
                myHero.takeDamage(bossMonster.attack())
                print "You have %d HP left!" % myHero.HP
        else:
            print "Not a valid choice."

def endGame():
    print ""
    print "Congratulations! You've defeated the boss!"
    print "You've received a prize!"
    exit(0)

def dead(why):
    print why, "Good job buddy!"
    exit(0)

def mainRoom(hero):
    myHero = hero
    print "There is a door to the left, directly in front, and to the right."
    print "Which one do you take? The (left), (front), or (right)?"

    choice = raw_input("> ")

    if choice == "left":
        leftRoom(myHero)
    elif choice == "front":
        frontRoom(myHero)
    elif choice == "right":
        rightRoom(myHero)
    else:
        dead("You stumble around the room until you starve to death.")

class hero(object):
    name = ""
    HP = 100
    has_sword = False
    has_shield = False
    has_key = False
    potions = False

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, HP, has_sword, has_shield, has_key, potions):
        self.name = name
        self.HP = HP
        self.has_sword = has_sword
        self.has_shield = has_shield
        self.has_key = has_key

    def attack(self):
        if self.has_sword == False:
            damage = random.randint(1,10)
        elif self.has_sword == True:
            damage = random.randint(11,30)
        return damage

    def takeDamage(self, damage):
        if self.has_shield == False:
            takenDamage = damage
        elif self.has_shield == True:
            takenDamage = damage/2
        self.HP -= takenDamage
        if self.HP <= 0:
            print dead("You died!")
        else:
            return takenDamage

class bat(object):
    HP = 50
    batDead = False

    # The class "constructor" - It's actually an initializer
    def __init__(self, HP, batDead):
        self.HP = HP
        self.batDead = batDead

    def attack(self):
        damage = random.randint(1,15)
        return damage

    def takeDamage(self, damage):
        self.HP -= damage
        if self.HP <= 0:
            print "You've killed the bat!"
            self.batDead = True
        return damage

class boss(object):
    HP = 150
    bossDead = False

    # The class "constructor" - It's actually an initializer
    def __init__(self, HP, bossDead):
        self.HP = HP
        self.bossDead = bossDead

    def attack(self):
        damage = random.randint(11,25)
        return damage

    def takeDamage(self, damage):
        self.HP -= damage
        if self.HP <= 0:
            print "You've killed the boss!"
            self.bossDead = True
        return damage

def start():
    print "Hello, friend. What's your name?"
    name = raw_input("> ")
    myHero = hero(name, 100, False, False, False, False)
    print "Hi, %s! \nYour story begins now...\n" % (name)
    print "You wake up in the middle of a dark temple."
    mainRoom(myHero)

start()
