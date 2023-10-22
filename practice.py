import time
import numpy as np

a = np.arange(10)
b = np.arange(10)

start = time.time()
c=a*b
end = time.time()

print(c)

d=np.where(c>5,5,0)
print(d)
print("\n\n elapsed time =", end - start)

