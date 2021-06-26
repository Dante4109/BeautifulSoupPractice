import concurrent.futures
import time

numList = []

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    numList.append(seconds)


# context manager
with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
    secs = range(0, 100000)
    results = executor.map(do_something, secs)
    # for result in results:
    #     print(result)

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()
print(numList)
print(f'Finished in {round(finish-start, 2)} second(s)')
