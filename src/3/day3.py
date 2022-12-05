import functools

linee = open("input.txt").readlines()

LOWER = 96
UPPER = 38

def valoreCarattere(carattere):
    return ord(carattere) - (((carattere == carattere.lower()) and LOWER ) or UPPER ) 

def addCarattere(tot, line):
    carattere = list(set((tuple:=(line[len(line)//2:],line[:len(line)//2] ))[0]).intersection(tuple[1]))[0]
    return tot+valoreCarattere(carattere)

def getCommon(lines):
    return list(functools.reduce(lambda finalSet, line: finalSet.intersection(set(line)), lines[1:], set(lines[0])))[0]

def split(my_list, n):
    return [[elemento.replace("\n","") for elemento in my_list[i*n:i*n+n] ] for i in range(len(my_list)//3)]


print(functools.reduce(addCarattere, linee, 0))
print((sum([valoreCarattere(getCommon(gruppo)) for gruppo in split(linee,3)])))
