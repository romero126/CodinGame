def Debug3(obj):
    r = ""
    for i in obj:
        if r == "":
            r = str(i)
        else:
            r = r + ",  "+ str(i)
    print(r, file=sys.stderr)

def Debug(*args):
    r = ""
    for i in args:
        if r == "":
            r = str(i)
        else:
            r = r + "   " + str(i)
    print(r, file=sys.stderr)


Debug("abcd", "efg", "hijk", "lmnop")
