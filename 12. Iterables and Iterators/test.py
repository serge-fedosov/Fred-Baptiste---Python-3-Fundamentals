from time import perf_counter

start = perf_counter()
l = list(range(100_000_000))
end = perf_counter()
print(f'elapsed {end - start}')
