def removeRef(ls, obj):
    length = len(ls)
    for i in range(length):
        if ls[i] is obj:
            ls.pop(i)
            break
def inRef(ls, obj):
    length = len(ls)
    for i in range(length):
        if ls[i] is obj:
            return True
def allExcept(ls, obj):
    lsf = []
    for it in ls:
        if not (it is obj):
            lsf.append(it)
    return lsf
