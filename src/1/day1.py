import functools

linee = open("input.txt").readlines()

allElvesCal = functools.reduce(lambda tot, line : (line == "\n" and tot+[0]) or (tot[:-1]+[tot[-1]+int(line.replace("\n",""))]), linee, [0])

print(max(allElvesCal))
print(sum(sorted(allElvesCal)[-3:]))