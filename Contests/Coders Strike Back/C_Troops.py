class C_Troops:
    obj = {}
    def StartRound(self):
        self.obj = {}
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
        self.obj[v]["Source"] = arg2
        self.obj[v]["Destination"] = arg3
        self.obj[v]["Troops"] = arg4
        self.obj[v]["DestTime"] = arg5
        #Debug("Adding Troops: ", self.obj[v])
        return
    def GetValue(self, src, value):
        src = str(src)
        try:
            return self.obj[src][value]
        except:
            return -1
        return -1
    def TimeToOverrun(self, src):
        Level = Factories.GetValue(src, "Level")
        Owner = Factories.GetValue(src, "Owner")
        ID = Factories.GetValue(src, "ID")
        troops = (Factories.GetValue(src, "Troops"))
        ticks = 0

        objs = sorted(self.GetAllTroops(), key=lambda a: a["DestTime"])
        for obj in objs:
            if (ID == obj["Destination"]):
                d_ticks = obj["DestTime"]
                #Troops = Troops + (Elapsed Ticks * Level)
                elapsed_ticks = (d_ticks - ticks)
                production = elapsed_ticks * Level
                incomingtroops = obj["Troops"]
                troops = troops + production - incomingtroops
                ticks = d_ticks
                if troops <= 0:
                    return True, ticks, (troops * -1)

        return False, 0, 0
    def TotalIncoming(self, src):
        Level = Factories.GetValue(src, "Level")
        owner = Factories.GetValue(src, "Owner")
        troops = Factories.GetValue(src, "Troops")
        ticks = 0
        objs = sorted(self.GetAllTroops(), key=lambda a: a["DestTime"])
        for obj in objs:
            if (src == obj["Destination"]):
                if owner != obj["Owner"]:
                    troops = troops - obj["Troops"]
                else:
                    troops = troops + obj["Troops"]
        return troops
    def TotalMinTroopReq(self, src, rounds):
        Level = Factories.GetValue(src, "Level")
        owner = Factories.GetValue(src, "Owner")
        #troops = Factories.GetValue(src, "Troops")
        ticks = 0
        troops = 0
        objs = sorted(self.GetAllTroops(), key=lambda a: a["DestTime"])
        for obj in objs:
            if (src == obj["Destination"]):
                d_time = obj["DestTime"]
                elapsed_ticks = (d_time - ticks)

                if d_time > rounds:
                    return troops

                #Append or Subtract Troops
                if owner != obj["Owner"]:
                    troops = troops - obj["Troops"]
                else:
                    troops = troops + obj["Troops"]
                #Calculate Production
                troops = troops + (Level * elapsed_ticks)
        return troops

    def GetAllTroops(self):
        r = []
        for i in self.obj.items():

            r.append(i[1])
        r = sorted(r, key=lambda a: a["DestTime"])
        return r
    def GetTotal(self, owner):
        total = 0
        for i in self.obj.items():
            if i[1]["Owner"] == owner:
                total = total + i[1]["Troops"]
        return total
    def GetAllyTotal(self, src):
        v = str(src)
        count = 0
        time = -1
        troop = 0
        owner = Factories.GetFactory(src)
        owner = owner["Owner"]
        for obj in self.obj.items():
            if (owner == obj[1]["Owner"]):
                if (obj[1]["Destination"] == src):
                    count = count + obj[1]["Troops"]
                    if time == -1:
                        time = obj[1]["DestTime"]
                        troop = obj[1]["Troops"]
                    if time > obj[1]["DestTime"]:
                        time = obj[1]["DestTime"]
                        troop = obj[1]["Troops"]
            if time == -1:
                time = 0
        return [count, time, troop]
    def GetAttackerTotal(self, src):
        v = str(src)
        count = 0
        time = -1
        troop = 0

        owner = Factories.GetFactory(src)
        owner = owner["Owner"]
        #Debug("Attacker Total", owner)
        for obj in self.obj.items():
            #Debug("Attacker Total", obj)
            if (owner != obj[1]["Owner"]):
                if (obj[1]["Destination"] == src):
                    count = count + obj[1]["Troops"]
                    if time == -1:
                        time = obj[1]["DestTime"]
                        troop = obj[1]["Troops"]
                    if time > obj[1]["DestTime"]:
                        time = obj[1]["DestTime"]
                        troop = obj[1]["Troops"]
            if time == -1:
                time = 0
        return [count, time, troop]
    def Attack(self, src, dst, troop):
        v = "_Attack_" + str(src) + str(dst) + str(troop)
        self.obj[v] = {}
        self.obj[v]["ID"] = v
        self.obj[v]["Type"] = "TROOP"
        self.obj[v]["Owner"] = 1
        self.obj[v]["Source"] = src
        self.obj[v]["Destination"] = dst
        self.obj[v]["Troops"] = troop
        self.obj[v]["DestTime"] = 0
