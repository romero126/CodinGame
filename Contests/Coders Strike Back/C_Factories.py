class C_Factories:
    obj = {}
    def init(self, src, dst, time):
        a = str(src)
        b = str(dst)
        try:
            self.obj[a]
        except:
            self.obj[a] = {}
        try:
            self.obj[b]
        except:
            self.obj[b] = {}
        self.obj[a]["ID"] = src
        self.obj[b]["ID"] = dst
        self.MAP(src, dst, time)
        self.MAP(dst, src, time)
    def Add(self, entity_id, entity_type, arg1, arg2, arg3, arg4, arg5):
        #Add Troops to List
        v = str(entity_id)
        try:
            self.obj[v]
        except:
            self.obj[v] = {}
        self.obj[v]["ID"] = entity_id
        self.obj[v]["Type"] = entity_type
        self.obj[v]["Owner"] = arg1
        self.obj[v]["Troops"] = arg2
        self.obj[v]["Level"] = arg3
        self.obj[v]["Production"] = arg4

        try:
            self.obj[v]["BOMB"]
        except:
            self.obj[v]["BOMB"] = 0
        try:
            self.obj[v]["MAP"]
        except:
            self.obj[v]["MAP"] = {}
    def Attack(self, src, dst, troop):
        src = str(src)
        troop = int(troop)

        self.obj[src]["Troops"] = self.obj[src]["Troops"] - troop

        Troops.Attack(src, dst, troop)
        Action.Attack(src, dst, troop)
        #Factories.Attack(factory["ID"], enemy["ID"], e_cost)
    def GetValue(self, src, value):
        src = str(src)
        try:
            return self.obj[src][value]
        except:
            return -1
        return -1
    def Level(self, src):
        src = str(src)
        self.obj[src]["Troops"] = self.obj[src]["Troops"] - 10
        Action.Level(src)

        #Factories.Attack(factory["ID"], enemy["ID"], e_cost)

    def GetTotal(self, owner, obj):
        a_factories = self.GetFactories(owner)
        count = 0
        sumval = 0
        for factory in a_factories:
            if factory["Owner"] == owner:
                count = count + 1
                try:
                    sumval = sumval + factory[obj]
                    #value = factory[obj]
                except:
                    sumval = sumval
                    #value = 0
                
        return count, sumval
    def GetAverage(self, owner, obj):
        count,sumval = self.GetTotal(owner, obj)
        if sumval == 0 or count == 0:
            return 0
        return int(round(sumval / count))
    def CalculateCosts(self, src):
        a_factories = self.GetFactoriesNotOwner(-2) #Grab Everyone
        for factory in a_factories:
            #Calculate Costs for all and dump into the asset
            threat = Troops.GetAttackerTotal(factory["ID"])
            allies = Troops.GetAllyTotal(factory["ID"])

            Level = factory["Level"]

            if factory["ID"] != src:
                Distance = factory["MAP"][str(src)]
            else:
                Distance = 1


            #Calculate Costs
            if factory["Owner"] == 0:
                Level = 1

            TroopCount = factory["Troops"]


            LevelWeight = (Level * 2.5)
            cost = (Distance * Level) + TroopCount - allies[0] + threat[0] - LevelWeight

            min_strength = (Level * Distance) + TroopCount + allies[0] - threat[0] + 3
            #min_strength = TroopCount
            factory["Cost"] = cost
            factory["Min_Strength"] = min_strength

            if factory["ID"] == src:
                cost = (TroopCount + allies[0] - threat[0])
                min_strength = (Level * Distance) + TroopCount + allies[0] - threat[0] + 2
                #min_strength = TroopCount
                factory["Cost"] = cost
                factory["Min_Strength"] = min_strength

    def GetCost(self, src, dst):
        src = str(src)
        dst = str(dst)
        Level = self.obj[dst]["Level"]
        TroopCount = self.obj[dst]["Troops"]
        IncomingTroops = 0
        Cost = (Level * Distance) + (TroopCount - IncomingTroops)
        return Cost
    def GetFactory(self, src):
        return self.obj[str(src)]
    def GetAverageCost(self):
        return

    def GetFactoriesNotOwner(self, owner):
        r = []
        for i in self.obj.items():
            if (i[1]["Owner"] != owner):
                r.append(i[1])
        r = sorted(r, key=lambda a: a["Troops"])
        return r

    def GetFactories(self, owner):
        r = []
        for i in self.obj.items():
            if (i[1]["Owner"] == owner):
                    r.append(i[1])
        r = sorted(r, key=lambda a: a["Troops"])
        return r
    def GetStrongestFactoral(self, owner, value1, value2):
            entity = 0
            for i in self.obj.items():
                if (i[1]["Owner"] == owner):
                    if (entity == 0):
                        entity = i[1]
                    e_fact = i[1][value1] * i[1][value2]
                    f_fact = entity[value1] * entity[value2]
                    if (e_fact > f_fact):
                        entity = i[1]
            return entity
    def GetStrongest(self, owner, value):
        entity = 0
        for i in self.obj.items():
            if (i[1]["Owner"] == owner):
                if (entity == 0):
                    entity = i[1]
                if (i[1][value] > entity[value]):
                    entity = i[1]
        return entity

    def GetWeakest(self, owner):
        entity = 0
        for i in self.obj.items():
            if (i[1]["Owner"] == owner):
                if (entity == 0):
                    entity = i[1]
                if (i[1]["Troops"] < entity["Troops"]):
                    entity = i[1]
        return entity
    def GetNearest(self, src, owner):
        entity = 0
        edist = 0
        ospf = self.obj[str(src)]["MAP"].items()
        ospf = sorted(ospf, key=lambda a: a[1])
        for i in ospf:
            if self.obj[str(i[0])]["Owner"] == owner:
                if entity == 0:
                    entity = self.obj[str(i[0])]
                    edist = i[1]
                if edist > i[1]:
                    entity = self.obj[str(i[0])]
                    edist = i[1]
        return entity, edist
    def MAP(self, src, dst, time):
        try:
            self.obj[str(src)]["MAP"]
        except:
            self.obj[str(src)]["MAP"] = {}
        try:
            self.obj[str(src)]["MAP"][str(dst)]
        except:
            self.obj[str(src)]["MAP"][str(dst)] = 0
#        if (time > self.obj[str(src)]["MAP"][str(dst)]):
        self.obj[str(src)]["MAP"][str(dst)] = time
