from random import randint

class Game(object):
    def __init__(self):
        self.turn = 1
    def end_turn(self):
        self.turn += 1

class Dice(object):
    def __init__(self):
        self.total = 0
    def roll(self, number=2):
        self.total = 0
        number_of_dice = number
        while(number_of_dice > 0):
            die = randint(1, 6)
            self.total += die
            number_of_dice -= 1
        return self.total
    def attribute_roll(self, attribute):
        self.roll()
        return self.total <= attribute
    def skill_roll(self, skill, target):
        self.roll()
        try:
            return self.total + skills[skill] >= target
        except:
            return self.total >= target

class Character(object):
    def __init__(self):
        self.name = ""
        self.brains = 0
        self.bravery = 0
        self.brawn = 0
        self.health = 0
        self.health_max = 0
        self.skills = {}
    def setvar(self, var, value):
        self.__dict__[var] = value
    def do_damage(self, enemy):
        damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0:
            print "%s evades %s's attack." % (enemy.name, self.name)
        else:
            print "%s hurts %s!" % (self.name, enemy.name)
        return enemy.health <= 0

class Villain(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = ''
        self.plan = ''
        self.dm = 0

class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = 'a Dalek'
        self.health = randint(1, player.health)

class Ally(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = 'Rose Tyler'
        self.health = 10
        
class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "The Doctor"
        self.brains = 10
        self.brawn = 4
        self.bravery = 7
        self.state = 'normal'
        self.health = 10
        self.health_max = 10
        self.dm = 0
        self.luck = 4
    def addto(self, var, value):
        try:
            self.__dict__[var] += value
            print "\n%s is now %s." % (var, self.__dict__[var])
            return value
        except:
            print "\n%s cannot be added to %s." % (value, var)
    def addskill(self, skill, val = 1):
        if skill in allskills:
            if skill in p.skills:
                self.skills[skill] += val
                print "\n%s now at level %i." % (skill, p.skills[skill])
                return 0
            else:
                self.skills[skill] = val
                print "\n%s added to your skills." % skill
                return 1
        else:
            print "%s is not a valid skill." % skill.capitalize()
            return 0
    def quit(self):
        self.health = 0
        input("\n\nPress the enter key to exit.")
    def help(self):
        print "\n"
        for a in actions.keys():
            print a
    def status(self):
        print "%s's health: %d/%d" % (self.name, self.health, self.health_max)
        
    def defeat(self):
        if v.name == '':
            print "You don't know who the villain is."
        elif v.plan == '':
            print "You don't know the villain's plan."
        else:
            d.roll()
            d.total += self.dm
            if g.turn in range(1,5):
                d.total -= 2
            if g.turn in range(5,9):
                d.total -= 1
            if d.total in range(2,4):
                print "You are killed in your attempt to defeat the enemy. The game is over."
                p.quit()
            if d.total == 4:
                if self.companion:
                    print "Your Companion has been killed."
                    self.companion = None
                    self.luck -= 2
                else:
                    print "You are killed in your attempt to defeat the enemy. The game is over."
                    self.quit()
            if d.total == 5:
                print "You have failed to defeat the Enemy and have been captured"
                self.state = 'captured'
                self.escape()
            if d.total == 6:
                print "You have failed to defeat the Enemy."
                self.luck -= 1
            if d.total == 7:
                print "You have failed to defeat the Enemy."
                self.dm -= 1
                #roll for enemy event.
            if d.total in range(8,10):
                print "You have failed to defeat the Enemy."
    def escape(self):
        print "you escape"
    def explore(self):
        print "\nYou decide to explore the area and see what you can discover."
        total = d.roll()
        if 'tracking' in p.skills:
            total += p.skills['tracking']
        if total == 2:
            pass
            #roll for enemy event.
        elif total in range(3,5):
            e.e078()
        elif total == 5:
            e.e002()
        elif total in range(6,8):
            print "\nYou discover nothing unusual."
        elif total == 8:
            pass
            #roll for character even.
        elif total in range(9,11):
            pass
            #you have a choice.
        elif total == 11:
            pass
            #roll for plot event.
        else:
            e.e082()
    def investigate(self):
        print "you investigate"
    def move(self):
        print "you move"
    def plan(self):
        print "you plan"
    def relax(self):
        print "you relax"
    def research(self):
        print "you research"
    def rescue(self):
        print "you rescue someone"
    def rest(self):
        print "you rest"
    def info(self):
        print "you seek info"
    def wait(self):
        print "you wait"
    def enemy_attacks(self):
        if self.enemy.do_damage(self):
            print "%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name)
    
allskills = [
    'aware',
    'charisma',
    'computers',
    'demolitions',
    'domination',
    'engineering',
    'gloating',
    'history',
    'marksman',
    'medicine',
    'music',
    'pilot',
    'poison',
    'running',
    'science',
    'tardis',
    'thief',
    'tracking',
    'unit'
    ]

actions = {
    'quit': Player.quit,
    'help': Player.help,
    'status': Player.status,
    'defeat': Player.defeat,
    'escape': Player.escape,
    'explore': Player.explore,
    'investigate': Player.investigate,
    'move': Player.move,
    'plan': Player.plan,
    'relax': Player.relax,
    'research': Player.research,
    'rescue': Player.rescue,
    'rest': Player.rest,
    'info': Player.info,
    'wait': Player.wait
    }

g = Game()
d = Dice()
v = Villain()
p = Player()
print "Evil events have overtaken the Universe! The Timelords and your home planet of Gallifrey have been destroyed in the last, great Time War. You managed to escape just in time and now, in a new regeneration, are standing next to the central console of your TARDIS as it flies through the twisting miasma of the Time Vortex."
print "\nYou have brains 10, brawn 4, and bravery 7."
print "You may also allocate 5 extra points between these attributes, but no more than 3 to any one."

#allocate attributes.
extra = 5
allowed = {'brains': 3,'brawn': 3, 'bravery': 3}

while(extra > 0):
    print "\nYou have %i points to allocate." % extra
    attribute = raw_input("Which attribute would you like to increase? ").lower()
    if attribute in allowed:
        if allowed[attribute] == 0:
            print "\nYou can't add anymore to %s.\n" % attribute
        else:
            maxval = min(extra, allowed[attribute])
            print "\nYou can add up to %i to %s." % (maxval, attribute)
            newval = int(raw_input("What do you want to add to %s?\n(Type '0' if you changed your mind.) " % attribute))
            addval = min(maxval, newval)
            p.addto(attribute, addval)
            extra -= addval
            allowed[attribute] -= addval
    else:
        print "\n%s is not a valid attribute." % attribute.capitalize()

#add skills.
print "\nYou also choose 8 skills from the list below."
print "You may not choose a skill twice.\nYou will be able to increase your skills later in the game.\n"

for s in allskills:
    print s

new = 8
while(new > 0):
    print "\nYou have %i skills to add." % new
    skill = raw_input("which skill would you like to add? ").lower()
    if skill in p.skills:
        print "\nYou have already added %s." % skill
    else:
        new -= p.addskill(skill)

print "\nYou watch as a loud wheezing, groaning sound suddenly fills the air as the TARDIS starts to materialize. As the sound dies away, you check the controls of the TARDIS to see where you are."
print "\nYou have landed on Earth during the glorious second Roman Empire where technology mixes with antiquity. Roman centurians armed with blasters fly in hover-chariots over the city whilst the population watches robotic gladiatorial games in enormous coliseums."
print "\nNow you straighten your new clothes (much better than your last incarnation anyway) and step outside the TARDIS to begin your adventure."
print "\nChoose your first action. Type 'help' to see a list of possible actions."

#Turn sequence:
while(p.health > 0 and g.turn <= 12):
    actionFound = False
    while(actionFound == False):
        try:
            action = raw_input("\nWhat would you like to do? ").lower()
            actions[action](p)
            actionFound = True
        except:
            print "%s doesn't understand the suggestion." % p.name.capitalize()

    #Code for random encounters goes here, after action resolution and before turn ends.
    
    g.end_turn
    
