from itertools import product
import os

import joblib

Args = []

for p in range(0, 5):
    for _ in range(5 // (p+1)):
        Args.append((10 ** p, -1, 10 ** 5, -1))

for p in range(3):
    Args.append((1, -1, 10 ** 5, p))


print(len(Args))
print(Args)

def call(id, args):
    cmd = f"python3 tools/gen-call.py { id } { ' '.join(map(str, args)) }"
    # print(cmd)
    os.popen(cmd)

joblib.Parallel(n_jobs=1)(
    joblib.delayed(call)(id, args) for id, args in enumerate(Args)
)
