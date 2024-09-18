from collections import defaultdict 

n = list(input())

freq = defaultdict(int) 

for c in n:
    freq[c] += 1

odd = False
no_solution = False

for k,v in freq.items():
    if v % 2 == 1:
        if odd:
            no_solution = True
        else:
            odd = True

if odd and len(n) % 2 == 0:
    no_solution = True
if not odd and len(n) % 2 == 1:
    no_solution = True

out = [''] * len(n) 

i, j = 0, len(n) - 1

if not no_solution:
    for k, v in freq.items():
        for l in range(v // 2):
            out[i] = k
            out[j] = k
            i += 1
            j -= 1 
        if v % 2 == 1:
            out[len(n) // 2] = k
    print(''.join(out))
else:
    print('NO SOLUTION')

