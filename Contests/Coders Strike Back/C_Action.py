class C_Action:

    def StartRound(self):
        self.ActionSTR = ""
    def MSG(self, text):
        if (self.ActionSTR != ""):
            self.ActionSTR = self.ActionSTR + ";"
        self.ActionSTR = self.ActionSTR + "MSG " + str(text)
    def Attack(self, factory, enemy, troop):
        if (self.ActionSTR != ""):
            self.ActionSTR = self.ActionSTR + ";"
        if troop < 0:
            Debug("Error", factory, enemy, troop)
            raise("TroopCount wrong")
        self.ActionSTR = self.ActionSTR + "MOVE " + str(factory) + " " + str(enemy) + " " + str(troop)
    def Level(self, factory):
        if (self.ActionSTR != ""):
            self.ActionSTR = self.ActionSTR + ";"
        Debug("Leveling up ", factory)
        self.ActionSTR = self.ActionSTR + ("INC " + str(factory) )
    def Bomb(self, src, dst):
        if (self.ActionSTR != ""):
            self.ActionSTR = self.ActionSTR + ";"
        #Debug("Blowing it up ", factory)
        self.ActionSTR = self.ActionSTR + ("BOMB " + str(src) + " " + str(dst) )
    def Wait(self):
        if (self.ActionSTR != ""):
            self.ActionSTR = self.ActionSTR + ";"
        self.ActionSTR = self.ActionSTR + "WAIT"
    def HasAttacked(self):
        if "MOVE" in self.ActionSTR:
            return True
        return False
    def EndRound(self):
        print(self.ActionSTR)
