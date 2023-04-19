"""
https://stackoverflow.com/questions/69995292/algorithm-question-finding-the-cheapest-flight
"""

D = [10, 7, 15, 12, 4]
R = [5, 12, 9, 10, 12]

monoQ = [0] * len(R)
monoQ[-1] = R[-1]

for i in range(len(R) - 2, -1, -1):
    monoQ[i] = min(monoQ[i + 1], R[i])

best = R[0] + D[0]
for i, el in enumerate(D):
    best = min(best, D[i] + monoQ[i])
print(best)
