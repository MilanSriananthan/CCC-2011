givers = input().split(" ")
required = input().split(" ")

def makeNum(seq):
    hold = []
    for i in seq:
        hold.append(int(i))
    return hold

required = makeNum(required)
givers = makeNum(givers)
total = 0
def check(seq1, val):
    count = 0
    for i in range(len(seq1)):
        if val == 0:
            break
        elif val > seq1[-i-1]:
            count += seq1[-i-1]
            val -= seq1[-i-1]
            seq1[-i-1] = 0
        else:
            count += val
            seq1[-i-1] -= val
            val = 0

    return [seq1, count]


start = [givers[0]]
result = check(start, required[0])
total += result[1]
givers[0] = result[0][0]


start = givers[:2]
result = check(start, required[1])
total += result[1]
givers[:2] = result[0]


start = [givers[0], givers[2]]
result = check(start, required[2])
total += result[1]
givers[0] = result[0][0]
givers[2] = result[0][1]


start = givers[:4]
result = check(start, required[3])
total += result[1]
givers[:4] = result[0]


start = [givers[0], givers[4]]
result = check(start, required[4])
total += result[1]
givers[0] = result[0][0]
givers[4] = result[0][1]


start = [givers[0], givers[1], givers[4],  givers[5]]
result = check(start, required[5])
total += result[1]
givers[0] = result[0][0]
givers[1] = result[0][1]
givers[4] = result[0][2]
givers[5] = result[0][3]


start = [givers[0], givers[2], givers[4], givers[6]]
result = check(start, required[6])
total += result[1]
givers[0] = result[0][0]
givers[2] = result[0][1]
givers[4] = result[0][2]
givers[6] = result[0][3]


start = givers
result = check(start, required[7])
total += result[1]
givers = result[0]


print(total)
'''
o-, o+, a-, a+, b-, b+, AB-, AB+
'''