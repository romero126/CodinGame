class C_Bomb:
    obj = {}
    old = {}
    def StartRound(self):
        self.old = self.obj
        self.obj = {}
        return
    def StartRound_After(self):
        for i in self.old.items():
            try:
                self.obj[ str(i[1]["ID"]) ]
            except:
                Debug("Clear Bomb Threat!?")
                self.ClearBombThreat(i[1]["ID"])
    def Add(self, entity_id, entity_type, arg1, arg2, arg3, arg4, arg5):
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
        self.obj[v]["DestTime"] = arg4
        self.obj[v]["Unused"] = arg5

        owner = arg1
        e_src = arg2
        if (owner == -1):
            #Start Flagging potential hits!
            e_factory = Factories.GetFactory(e_src)
            p_factories = Factories.GetFactories(1)

            for p_factory in p_factories:
                if (p_factory["BOMB"] == 0):
                    #                    threat, total, current
                    try:
                        time = p_factory["MAP"][str(e_src)]
                    except:
                        time = 0

                    p_factory["BOMB"] = [entity_id , time, time ]
                else:
                    bomb = p_factory["BOMB"]
                    bomb[2] = bomb[2] - 1
    def ClearBombThreat(self, src):
        p_factories = Factories.GetFactories(1)
        for i in p_factories:
            if (i["BOMB"] != 0):
                if i["BOMB"][0] == src:
                    i["BOMB"] = 0
    def CanExplode(self, src):
        f_objs = Factories.GetFactories(1)
        for obj in f_objs:
            bomb = obj["BOMB"]
            if len(self.obj.items()) == 0:
                bomb = 0
            if obj["ID"] == src:
                if bomb != 0:
                    if bomb[2] == 2:
                        obj["BOMB"] = 0
                        return True
        return False
    def GetBombs(self, owner):
        bombs = []
        for obj in self.obj.items():
            if (obj[1]["Owner"] == owner):
                bombs.append(obj[1]["DestTime"])
        return bombs
