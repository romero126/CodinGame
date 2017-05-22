import sys
import math


#Stateful Thoughts
# Player.AI stages

#AI BreakPoints
#
# LandGrab (Resource Gathering)
    # Phase 1

        #When to start?
            #self.total < 10 per object
            #Total /10 / 5
        #Go Straight to MoleculesTable
            #Grab an average of 10/size
            #
        #
# Grab Average


MovementMatrix = {
    'SET': ['START_POS', 'SAMPLES', 'DIAGNOSIS', 'MOLECULES', 'LABRATORY'],
    'START_POS':    [2, 2, 2, 2],
    'SAMPLES':      [0, 3, 3, 3],
    'DIAGNOSIS':    [3, 0, 3, 4],
    'MOLECULES':    [3, 3, 0, 3],
    'LABRATORY':    [3, 4, 3, 0]
}
MovementMatrix = {
    'SET': ['START_POS', 'SAMPLES', 'DIAGNOSIS', 'MOLECULES', 'LABRATORY'],
    'START_POS':    [2, 2, 2, 2],
    'SAMPLES':      [0, 3, 3, 3],
    'DIAGNOSIS':    [3, 0, 3, 4],
    'MOLECULES':    [3, 3, 0, 3],
    'LABRATORY':    [3, 4, 3, 0]
}

class PLAYER:
    '''
    index = PlayerIndex
    target = ''
    eta = ''
    score = ''
    storage = []
    expertise = []

    '''
    def __init__(self, index):
        self.index = index
        self.target = ''
        self.eta = ''
        self.score = ''
        self.storage = []
        self.expertise = []

    def LoadData(self, data):
        '''
            Load Data from the following Format
            string target
            int eta
            list score = (int), (int), (int), (int), (int)

        '''
        self.target = data[0]
        self.eta = int(data[1])
        self.score = int(data[2])
        self.storage = [int(j) for j in data[3:7]]
        self.expertise = [int(j) for j in data[8:12]]
    def TotalExpertise(self):
        total = 0
        for i in self.expertise:
            total += i
        return total
    def TotalStorage(self):
        total = 0
        for i in self.storage:
            total += i
        return i
    def isLocation(self):
        '''
            Determine if my player is still moving
        '''
        if self.eta > 0:
            return False, self.target
        return True, self.target


class AI_CLASS:
    def AI(self, playerClass):
        pass
    def START_POS():
        pass
    def DIAGNOSIS():
        pass
    def
    pass


#class AI_CLASS_BLOCKING



def Debug(*args):
    r = ""
    for i in args:
        if r == "":
            r = str(i)
        else:
            r = r + "   " + str(i)
    print(r, file=sys.stderr)
class lab_class:
    samples = []
    def LoadData(self, data):
        #data = [int(i) for i in data]



        sample = {
            'ID': int(data[0]),
            'carrier': int(data[1]),
            'rank': data[2],
            'expgain': data[3],
            'health': int(data[4]),
            'storage': [int(data[5]), int(data[6]), int(data[7]), int(data[8]), int(data[9])]
        }
        '''
        #Get Median Storage Points
        median_storagepoints
        #Calculate Points (Highest points win)

        storage = sample['STORAGE']
        #Bad Thing
        storage_points = storage[0] + storage[1] + storage[2] + storage[3] + storage[4]

        expgain = sample['EXPGAIN'] #Good thing #Ignore for League
        health = sample['HEALTH']   #Good thing

        sample['COST'] = storage_points / health
        '''

        #health = undiscovered -1
        #sample['COST'] = sample['HEALTH']
        storage = sample['storage']
        sample['cost'] = storage[0] + storage[1] + storage[2] + storage[3] + storage[4]
        self.samples.append(sample)
    def MoleculeTable(self, data):
        self.available = data

    def Identify(self):
        for i in self.samples:
            if i['health'] == -1 and i['carrier'] == 0:
                return -1, i['ID']
        return 1, -1


    def StartData(self):
        self.samples = []
        self.available = []
    def Sample_Costs(self):
        return sorted(self.samples, key=lambda sample: sample['cost'])

class output:
    move_command = -1
    def Move(self, *args):
        if self.move_command == -1:
            r = ""
            for i in args:
                if r == "":
                    r = str(i)
                else:
                    r = r + "   " + str(i)
            self.move_command = r
    def EndOfRound(self):
        if self.move_command == -1:
            return
        print(self.move_command)
        self.move_command = -1


out = output()
# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!
class player:
    '''
        Three Stages
            START_POS
        target

        eta
        score
        storage = []
        expertise = []
    '''

    def LoadData(self,data):
        '''
        target, eta, score, storage_a, storage_b, storage_c, storage_d, storage_e, expertise_a, expertise_b, expertise_c, expertise_d, expertise_e = input().split()
        '''


        self.target = data[0]
        data.pop(0)
        data = [int(j) for j in data]
        self.eta = data[0]
        data.pop(0) #ETA
        self.score = data[0]
        data.pop(0) #Score

        self.storage = data[0:5]
        for i in range(5): data.pop(0)
        self.expertise = data[0:5]
        for i in range(5): data.pop(0)
        #Debug(self.storage, self.expertise, data)

    def SAMPLES(self):
        Debug("SAMPLES", len(self.cards))

        for i in self.cards:
            Debug(i)
        if len(self.cards) == 2:
            self.NextStation()
            return
        out.Move("CONNECT", 1)

    def DIAGNOSIS(self):
        v = lab.Identify()
        if v[0] == -1:
            out.Move("CONNECT", v[1])
            return

        self.NextStation()

    def MOLECULES(self):
        #Debug(self.cards_count)

        #First grab only needed
        count = 0
        for i in self.storage:
            count += i
        if count >= 10:
            self.NextStation()
            return

        Debug('Show Expertise', self.expertise)
        Debug('Show Counts', self.cards_count)
        Debug('Show available', lab.available)

        for i in self.cards:
            Debug(i)
        outval = 'ABCDE'
        for i in range(len(self.cards)):
            s_storage = self.cards[i]['storage']
            for x in range(len(s_storage)):
                required, inventory = s_storage[x], self.storage[x]

                #Debug("self.storage", self.storage)

                if required > inventory:
                    out.Move("CONNECT", outval[x])
                    break
        self.NextStation()
    def LABORATORY(self):
        Debug("Labratory Finally!!")
        for i in range(len(self.cards)):
            s_storage = self.cards[i]['storage']
            v = True
            for x in range(len(s_storage)):
                a, b = s_storage[x], self.storage[x]
                if a > b:
                    v = False
                    break
            if v == True:
                out.Move("CONNECT", self.cards[i]['ID'])
                return

        self.NextStation()


    def AI(self):
        Debug("AI, load values")
        v = lab.Sample_Costs()


        #Get Count Data
        count = 0
        cards_count = [0,0,0,0,0]
        self.cards = []

        for i in v:
            Debug(i['ID'], i['carrier'])
            if i['carrier'] == 0:
                self.cards.append(i)
                Debug("Adding Cards!", i)
                cards_count[0] += i['storage'][0]
                cards_count[1] += i['storage'][1]
                cards_count[2] += i['storage'][2]
                cards_count[3] += i['storage'][3]
                cards_count[4] += i['storage'][4]
                count += 1


        if self.target == 'SAMPLES':
            self.SAMPLES()

        elif self.target == 'DIAGNOSIS':
            self.DIAGNOSIS()

        elif self.target == 'MOLECULES':
            self.MOLECULES()

        elif self.target == 'LABORATORY':
            self.LABORATORY()
            pass
        else:
            self.NextStation()


    def NextStation(self):
        path = ['SAMPLES','DIAGNOSIS','MOLECULES','LABORATORY']
        if not self.target in path:
            self.target = path[-1]
        v = path.index(self.target)
        if v == len(path) - 1:
            v = 0
        else:
            v += 1
        out.Move('GOTO', path[v])

    def __init__(self):
        self.target = ''
        self.storage = []
        self.cards = []
        self.cards_count = [0,0,0,0,0]

p1 = player()
lab = lab_class()

project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]
    Debug("Project Count", a,b,c,d,e)
Debug(project_count)
# game loop
while True:
    lab.StartData()
    #p1.StartData()
    for i in range(2):

        data = input().split()
        if i == 0:
            p1.LoadData(data)

    available = [int(i) for i in input().split()]
    lab.MoleculeTable(available)
    #available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]
    Debug(available)
    #Debug(available_a, available_b, available_c, available_d, available_e)

    sample_count = int(input())
    Debug("Sample Values", sample_count)

    for i in range(sample_count):
        data = input().split()
        Debug('DATA', data)
        lab.LoadData(data)



    #lab.CalculateCosts()
    #(AVG SampleCosts / currentsamplecost) health
    p1.AI()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    out.EndOfRound()
    #print("GOTO DIAGNOSIS")
