import os
import math
import time

PRIME_FILE = "primes.txt"
STEP_SIZE = 100000  # How many new numbers to test each run

def log(msg):
    print(f"[prime-generator] {msg}")

def is_prime(n, known_primes):
    """Check if n is prime using existing primes up to sqrt(n)."""
    limit = int(math.sqrt(n)) + 1
    for p in known_primes:
        if p > limit:
            break
        if n % p == 0:
            return False
    return True

def read_primes(file_path=PRIME_FILE):
    """Read existing primes from file."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return [int(line.strip()) for line in f if line.strip().isdigit()]

def append_primes(primes, file_path=PRIME_FILE):
    """Append new primes to the file."""
    with open(file_path, "a") as f:
        for p in primes:
            f.write(f"{p}\n")

def generate_new_primes(existing_primes, step_size=STEP_SIZE):
    """Generate new primes beyond the largest known prime."""
    new_primes = []
    start = existing_primes[-1] + 1 if existing_primes else 2
    end = start + step_size - 1

    log(f"Checking numbers {start} to {end}")

    for n in range(start, end + 1):
        if is_prime(n, existing_primes + new_primes):
            new_primes.append(n)

    return new_primes

if __name__ == "__main__":
    start_time = time.time()

    log("Starting prime generation…")

    existing_primes = read_primes()

    if existing_primes:
        log(f"Loaded {len(existing_primes)} existing primes. Largest = {existing_primes[-1]}")
    else:
        log("No existing primes found. Starting fresh.")

    new_primes = generate_new_primes(existing_primes)

    if new_primes:
        append_primes(new_primes)
        log(f"Found {len(new_primes)} new primes.")
        log(f"Largest new prime = {new_primes[-1]}")
    else:
        log("No new primes found during this run.")

    elapsed = round(time.time() - start_time, 3)
    log(f"Prime generation complete in {elapsed} seconds.")
