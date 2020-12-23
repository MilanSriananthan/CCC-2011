lines = int(input())
all = []
for i in range(lines):
    hold = input()
    hold = list(hold)
    all.append(hold)

allt = 0
for seq in all:
    allt = allt + seq.count('t')
    allt = allt + seq.count('T')

alls = 0
for seq in all:
    alls = alls + seq.count('s')
    alls = alls + seq.count('S')

if allt > alls:
    print('English')
else:
    print('French')