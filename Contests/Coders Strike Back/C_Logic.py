class C_Logic:
    def IsDuress(self):
        return
    def GetTotalPoints(self):
        p_troops = Factories.GetTotal(1, "Troops")[1] + Troops.GetTotal(1)
        e_troops = Factories.GetTotal(-1, "Troops")[1] + Troops.GetTotal(-1)

        #Debug("Player:", Factories.GetTotal(1, "Troops")[1], Troops.GetTotal(1), p_troops)
        #Debug("Enemy :", Factories.GetTotal(-1, "Troops")[1], Troops.GetTotal(-1), e_troops)
        return p_troops, e_troops
    def GetProduction(self):
        p_val = Factories.GetTotal(1, "Level")[1]
        e_val = Factories.GetTotal(-1, "Level")[1]
        if p_val == 0:
            p_val = 1
        if e_val == 0:
            e_val = 1
        return p_val, e_val
    def TimeToOverrun(self):
        count = 0
        rounds = 0

        return rounds, count
