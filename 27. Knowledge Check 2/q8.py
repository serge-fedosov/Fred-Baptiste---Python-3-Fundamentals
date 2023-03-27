import random
import statistics


random.seed(-1) 
s = statistics.NormalDist(mu=3.0, sigma=5.0)
print(round(s.mean, 2))
