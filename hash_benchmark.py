import os
import time
import multiprocessing
from blake3 import blake3
from datetime import datetime

# Konfig aus ENV
CONCURRENT_WORKERS = int(os.getenv("CONCURRENT_WORKERS", "4"))
SECONDS_TO_RUN = int(os.getenv("SECONDS_TO_RUN", "10"))
FIXED_STRING = os.getenv("FIXED_STRING", "HelloWorld").encode()
RESULT_DIR = "/results"
ALGORITHM = "blake3"

# Worker-Funktion
def hash_worker(seconds, return_dict, worker_id):
    start_time = time.time()
    count = 0
    while time.time() - start_time < seconds:
        _ = blake3(FIXED_STRING).digest()
        count += 1
    return_dict[worker_id] = count

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    processes = []
    for i in range(CONCURRENT_WORKERS):
        p = multiprocessing.Process(target=hash_worker, args=(SECONDS_TO_RUN, return_dict, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    total_hashes = sum(return_dict.values())
    hashes_per_sec = total_hashes / SECONDS_TO_RUN

    timestamp = datetime.now().strftime("%Y_%m_%d_%H-%M-%S")
    os.makedirs(RESULT_DIR, exist_ok=True)
    result_path = os.path.join(RESULT_DIR, f"{timestamp}.txt")

    with open(result_path, "w") as f:
        f.write(f"Algorithm: {ALGORITHM}\n")
        f.write(f"Concurrent Workers: {CONCURRENT_WORKERS}\n")
        f.write(f"Seconds Run: {SECONDS_TO_RUN}\n")
        f.write(f"Total Hashes: {total_hashes}\n")
        f.write(f"Hashes/sec: {hashes_per_sec:.2f}\n")

    print(f"[✔] Ergebnis gespeichert unter: {result_path}")
