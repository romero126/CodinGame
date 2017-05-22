arg = [6,6,6,6,6]

def Normalize(args, minimum, maximum):
    result = 0
    #Sum of all values
    for val in args:
        result += val - minimum
    result = (result / len(args)) / maximum
    return result


#v = Normalize(arg, 0, 10)
#print(v)



class AI:
    def CALL(self):
        AI_GENERAL().CALL()



class AI_GENERAL:
    def CALL(self):
        print("Value")


AI().CALL()
