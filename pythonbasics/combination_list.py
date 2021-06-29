import imaplib
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

# Sequential

""" numList = []


for i in range(0, 5):
    numList.append(i)

print(numList) """

# Multi-Threaded

""" numList = []

ids = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13]


def append_to_list(ids):
    for i in ids:
        print(f'Adding number: {i}')
    print(f'Completed adding {len(ids)} numbers')
    return i


start = time.perf_counter()

number_of_chunks = 10
chunk_size = 10

with concurrent.futures.ThreadPoolExecutor() as executor:

    tasks = []

    for i in range(number_of_chunks):
        chunk = ids[i*chunk_size:(i+1)*chunk_size]
        tasks.append(executor.submit(append_to_list, chunk))
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
print(numList) """

# Multi Threaded but returns in same order executed

numList = []

ids = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13]


def append_to_list(ids):
    for i in ids:
        print(f'Adding number: {i}')
        numList.append(i)
    print(f'Completed adding {len(ids)} numbers')
    return i


start = time.perf_counter()

number_of_chunks = 10
chunk_size = 10

with concurrent.futures.ThreadPoolExecutor() as executor:

    results = executor.map(append_to_list, iterables)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
print(numList)
