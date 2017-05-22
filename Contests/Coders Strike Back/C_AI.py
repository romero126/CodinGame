class C_AI:
    def Call(self):
        self.CallSupport()
        self.CallGenAI()
        self.CallReinforce()
        #self.SendFeelers()
        Action.Wait()
    def SendFeelers(self):
        if not Action.HasAttacked():
            Debug("Send Feelers")
            factories = Factories.GetFactories(1)
            factories = sorted(factories, key=lambda a: a["Troops"], reverse=True)
            for factory in factories:
                f_id = factory["ID"]
                enemies = Factories.GetFactoriesNotOwner(1)
                enemies = sorted(enemies, key=lambda a: a["Cost"])
                for enemy in enemies:
                    if enemy["Owner"] == 0:
                        isoverrun, time, troops = Troops.TimeToOverrun(f_id)
                        if not isoverrun:
                            Factories.Attack(f_id, enemy["ID"], 1)

    def CallSupport(self):
        factories = Factories.GetFactories(1)
        factories = sorted(factories, key=lambda a: a["Troops"], reverse=True)
        for factory in factories:
            f_id = factory["ID"]
            isoverrun, time, troops = Troops.TimeToOverrun(f_id)

            if isoverrun == True:
                Debug("Halp I am getting overrun", f_id, time, troops)
                IsReinforced = self.CallSupport_Reinforce(f_id, troops, time)
                if IsReinforced != True:
                    if time <= 2:
                        self.CallSupport_Evacuate(f_id)

    def CallSupport_Reinforce(self, src, troop, time):
        factories = Factories.GetFactories(1)
        factories = sorted(factories, key=lambda a: a["Troops"], reverse=True)
        for factory in factories:
            f_id = factory["ID"]
            isoverrun, time, troops = Troops.TimeToOverrun(f_id)
            if isoverrun != True:
                dist = factory["MAP"][str(src)]
                min_str = Troops.TotalMinTroopReq(f_id, dist)
                if time > dist and min_str > troop:
                    Factories.Attack(f_id, src, min_str)
                    return True
        return False

    def CallSupport_Evacuate(self, src):
        fact, dist = Factories.GetNearest(src, 1)
        troops = Factories.GetValue(src, "Troops")
        if fact != 0:
            Factories.Attack(src, fact["ID"], troops)

    def CallBombAI(self):
        enemies = Factories.GetFactoriesNotOwner(1)
        factories = Factories.GetFactories(1)
        factories = sorted(factories, key=lambda a: a["Troops"], reverse=True)
        a = Factories.GetTotal(1, "Level")
        b = Factories.GetTotal(-1, "Level")

        #Bomb AI
        if a < b:
            e = Factories.GetStrongestFactoral(-1, "Troops", "Level")
            f = Factories.GetNearest(e["ID"], 1)
            if e != 0 and f != 0:
                totals = Troops.GetAttackerTotal(e["ID"])
                if totals[0] <= 0:
                    if len(Bomb.GetBombs(1)) == 0:
                        Action.Bomb(f["ID"], e["ID"])
    def CallGenAI(self):
        enemies = Factories.GetFactoriesNotOwner(1)
        factories = Factories.GetFactories(1)


        factories = sorted(factories, key=lambda a: a["Troops"], reverse=True)
        for factory in factories:
            if Bomb.CanExplode(factory["ID"]):
                self.Evacuate(factory["ID"])
            Factories.CalculateCosts(factory["ID"])
            f_cost = factory["Cost"]
            f_str = factory["Min_Strength"]


            Factories.CalculateCosts(factory["ID"])
            f_cost = factory["Cost"]
            f_str = factory["Min_Strength"]
            enemies = Factories.GetFactoriesNotOwner(1)
            enemies = sorted(enemies, key=lambda a: a["Cost"])
            for enemy in enemies:
                # Calculate Production Weights
                if factory["Level"] < 3:
                    f_points, e_points = Logic.GetTotalPoints()
                    f_prod, e_prod = Logic.GetProduction()
                    if (f_points / e_points) > .90 or e_prod > f_prod:
                        if (factory["Troops"] > 13):
                            Factories.Level(factory["ID"])

                Factories.CalculateCosts(factory["ID"])

                f_str = factory["Min_Strength"]
                f_troops = factory["Troops"]
                e_str = enemy["Min_Strength"]


                # Logic.GenAI_CheckAttack()
                if e_str > 0 and f_str > 0 and f_troops > 0:
                    f_avg = Factories.GetAverage(1, "Troops")
                    e_avg = Factories.GetAverage(-1, "Troops")

                    # Logic.GenAI_CareAboutStrength()
                    '''
                    if f_avg > (e_avg * 1.5):
                        eTroopTotal = Troops.GetTotal(-1)
                        fTroopTotal = Troops.GetTotal(1)
                        if (eTroopTotal * 1.25) < fTroopTotal:
                            #Stop Caring about strength.
                            Factories.Attack(factory["ID"], enemy["ID"], (factory["Troops"] / 2))

                    '''




                    f_points, e_points = Logic.GetTotalPoints()



                    if (f_points / e_points) > 1.18:
                        Factories.Attack(factory["ID"], enemy["ID"], (factory["Troops"] / 2))
                        Debug("Go On Offense", f_points, e_points)
                    #Logic.GenAI_GetStrength


                    elif f_str > e_str:
                        f_points, e_points = Logic.GetTotalPoints()
                        if (f_points / e_points) > 1.1 and f_str > 15:
                        #if (f_avg * .8) > e_avg and f_str > 15:
                            #Attack 0 Bases
                            Factories.Attack(factory["ID"], enemy["ID"], e_str+10)
                            Debug("Attack 0 Bases")
                        elif (enemy["Level"] != 0):
                            _near, _dist = Factories.GetNearest(factory["ID"], 1)
                            MinTroops = Troops.TotalMinTroopReq(factory["ID"], _dist+2)
                            _troops = factory["Troops"] - int(MinTroops / 2)

                            #Troops Greater than 1
                            if _troops > 1:
                                #Factories.Attack(factory["ID"], enemy["ID"], e_str + 3)
                                Factories.Attack(factory["ID"], enemy["ID"], _troops)
                            else:
                                mt = Troops.TotalMinTroopReq(factory["ID"], 2)
                                if mt < 0:
                                    _near, _dist = Factories.GetNearest(factory["ID"], 1)
                                    Factories.Attack(factory["ID"], enemy["ID"], factory["Troops"])





    def CallDistress(self):

        return
    def CallReinforce(self):
        #Call Reinforce
        factories = Factories.GetFactories(1)
        if len(Bomb.GetBombs(-1)) == 0:

            f_avg = Factories.GetAverage(1, "Troops")
            e_avg = Factories.GetAverage(-1, "Troops")
            if (f_avg * 1.15) > e_avg:

                factories = sorted(factories, key=lambda a: a["Cost"])
                for factory in factories:
                    Factories.CalculateCosts(factory["ID"])
                    avg = Factories.GetAverage(1, "Troops")
                    for target in factories:
                        if factory["ID"] != target["ID"]:
                            if factory["Troops"] > (avg * 1.2):
                                if target["Troops"] < avg:
                                    value = avg - target["Troops"]
                                    Factories.Attack(factory["ID"], target["ID"], value)
    def Evacuate(self, src):
        factory = Factories.GetFactory(src)
        friendlies = Factories.GetFactories(1)
        enemies = Factories.GetFactoriesNotOwner(1)
        evacuated = False
        Factories.CalculateCosts( factory["ID"])
        for i in friendlies:
            if i["ID"] != factory["ID"]:
                evacuated = True
                #Debug("Reinforce")
                Factories.Attack(factory["ID"], i["ID"], factory["Troops"])
        if evacuated:
            return
        for enemy in enemies:
            e_cost = enemy["Cost"]
            f_cost = factory["Cost"]
            if (e_cost < f_cost):
                if (not e_cost > factory["Troops"]):
                    if (e_cost > 0):
                        if (enemy["Level"] != 0):
                            Factories.Attack(factory["ID"], enemy["ID"], factory["Troops"])
                            evacuated = True
        if evacuated:
            return
        for enemy in enemies:
            e_cost = enemy["Cost"]
            f_cost = factory["Cost"]
            Debug("Ignore Costs")
            Factories.Attack(factory["ID"], enemy["ID"], factory["Troops"])
            evacuated = True
