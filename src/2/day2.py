import functools

linee = open("input.txt").readlines()

FIRSTP = ["C","B","A"]
SECONDP = ["X","Y","Z"]  


def takeNValueFromIterator(iterator, value):
        return (value != 0 and (next(iterator) or True) and takeNValueFromIterator(iterator, value-1)) or (value == 0 and next(iterator))

def pointsCycle(): 
    while True: yield 6; yield 0; yield 3

def sumRowToTot(tot, row):
    tupla = row.replace("\n","").split(" ")
    firstShift = FIRSTP.index(tupla[0])
    secondShift = SECONDP.index(tupla[1])
    return tot+ takeNValueFromIterator(pointsCycle(), firstShift+secondShift) + secondShift+1

def otherMoveCycle(): 
    while True: yield "Z"; yield "X"; yield "Y"

def adjustLine(linea):
    opponent = linea.split(" ")[0][0]
    result = linea.split(" ")[1][0]         
    firstShift = ["A", "B", "C"].index(opponent)
    secondShift = SECONDP.index(result)
    return opponent+" "+takeNValueFromIterator(otherMoveCycle(),firstShift+secondShift)


print(functools.reduce(sumRowToTot,linee, 0))

print(functools.reduce(sumRowToTot,[adjustLine(linea) for linea in linee], 0))