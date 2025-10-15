# metrik.py

import time
# We now import ONLY the core logic function we need from main.py
from main import encrypt_core 

def run_performance_test():
    """
    Tests the performance of the core encryption algorithm.
    """
   
    with open('sample_test_file_10k.txt', 'r', encoding='utf-8') as file:
        message = file.read()

    file_size_kb = len(message.encode('utf-8')) / 1024
    key = "a_strong_key_123"

    print("Starting performance test...")

    # Time the encryption by calling the clean core function
    start_time = time.time()
    encrypted_message = encrypt_core(message, key) 
    end_time = time.time()

    duration = end_time - start_time
    speed_kbs = file_size_kb / duration

    print(f"\nEncrypted {file_size_kb:.2f} KB in {duration:.4f} seconds.")
    print(f"Encryption Speed: {speed_kbs:.2f} KB/s")

if __name__ == "__main__":
    run_performance_test()