AI = C_AI()
Action = C_Action()
Factories = C_Factories()
Troops = C_Troops()
Bomb = C_Bomb()
Logic = C_Logic()
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    #Debug2(["Links", factory_1, factory_2, distance])
    Factories.init(factory_1, factory_2, distance)

roundcount = 0
# game loop
while True:
    Action.StartRound()
    Troops.StartRound()
    Bomb.StartRound()
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        entity_id = int(entity_id)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        arg_5 = int(arg_5)
        # Entities.Add(entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5)

        if (entity_type == "FACTORY"):
            Factories.Add(entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5)
        if (entity_type == "TROOP"):
            Troops.Add(entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5)
            #Factories.MAP(arg_2, arg_3, arg_5)
            #Factories.MAP(arg_3, arg_2, arg_5)
        if (entity_type == "BOMB"):
            Bomb.Add(entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5)
            Action.MSG("WARNING BOMB " + str(arg_2))
    Bomb.StartRound_After()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    Debug("Round Count", roundcount)
    roundcount = roundcount + 1
    AI.Call()

    Action.EndRound()
    # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
    # print("WAIT")
