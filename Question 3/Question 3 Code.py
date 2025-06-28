import random
import threading
import time

# =============================================================================
#               TO GENERATE 100 RANDOM NUMBERS FROM 0 TO 100
# =============================================================================

""" Return: 100 numbers (list)"""
def generate_random_numbers():
    rand_list = []      # List to store random numbers
    # Loop for 100 times
    # Write every round's random number (1 - 10000) into rand_list
    for _ in range(100):
        rand_list.append(random.randrange(1, 10001))    # 1 inclusive, 10001 exclusive
    return rand_list

# =============================================================================
#                TO RUN MULTI-THREADS FOR PRE-DEFINED ROUNDS
# =============================================================================

""" Parameter 1: Pre-defined rounds (int) """
""" Parameter 2: Pre-defined thread count (int) """
""" Return: Recorded time for every rounds (list) """
def run_multi_thread(rounds, thread_count):
    multi_thread_t = []     # List to store time taken for every multi-threading round
    # Loop for 'rounds' times
    for i in range(1, rounds + 1):
        thread_ls = []      # Thread list to store all created threads (easier operation)
        # Loop to create threads (amount according to thread_count)
        # Let every threads targets the generate_random_numbers function to run
        for _ in range (thread_count):
            thread = threading.Thread(target=generate_random_numbers)
            thread_ls.append(thread)    # Store into thread list
        
        # Record the start time in nanoseconds before starting all threads
        start_time = time.time_ns()
        # Start all threads
        for thread in thread_ls:
            thread.start()

        # Wait for all threads to complete before proceed
        for thread in thread_ls:
            thread.join()
        
        # Record the time interval in nanoseconds (end_time - start time)
        multi_thread_t.append(time.time_ns() - start_time)

    return multi_thread_t

# =============================================================================
#              TO RUN ONLY SINGLE THREAD FOR PRE-DEFINED ROUNDS
# =============================================================================

""" Parameter: pre-defined rounds (int) """
""" Return: Recorded time for every rounds (list) """
def run_single_thread(rounds):
    single_thread_t = []    # List to store time taken for every single-threading round
    # Loop for 'rounds' times
    for i in range(1, rounds + 1):
        # Record the start time in nanoseconds
        start_time = time.time_ns()
        # Generate three sets of random numbers one after the other
        for _ in range(3):
            generate_random_numbers()
        # Record the time interval in nanoseconds
        interval = time.time_ns() - start_time
        single_thread_t.append(interval)

    return single_thread_t

# =============================================================================
#             TO PRINT THE ROUND-BY-ROUND PERFORMANCE COMPARISON
#                      TO PRINT THE SUMMARY OF RESULTS
# =============================================================================

""" Parameter 1: Recorded time for every multi-threading rounds (list) """
""" Parameter 2: Recorded time for every single-threading rounds (list) """
def print_performance_table(multi_thread_t, single_thread_t):
    print("\nRound-by-Round Performance Comparison:")
    print("+---------+--------------------------+------------------------------+------------------+")
    print("|  Round  | Multithreading Time (ns) | Non-Multithreading Time (ns) |  Difference (ns) |")
    print("+---------+--------------------------+------------------------------+------------------+")
    for i in range(1, 11):
        # Column 1, 2, 3, 4
        print(f"|{str(i).center(9)}|", end = "")
        print(f"{str(multi_thread_t[i - 1]).center(26)}|", end = "")
        print(f"{str(single_thread_t[i - 1]).center(30)}|", end = "")
        print(f"{str(multi_thread_t[i - 1] - single_thread_t[i - 1]).center(18)}|")
    print("+---------+--------------------------+------------------------------+------------------+")

    total_multi = sum(multi_thread_t)                   # Total time taken of all rounds (multi-threading)
    total_single = sum(single_thread_t)                 # Total time taken of all rounds (single-threading)
    total_diff = total_multi - total_single             # Total time difference between multi and single
    avg_multi= total_multi / len(multi_thread_t)        # Average time taken of all rounds (multi-threading)
    avg_single = total_single / len(single_thread_t)    # Average time taken of all rounds (single-threading)
    avg_diff = avg_multi - avg_single                   # Average time difference between multi and single

    print("\nSummary of Results:")
    print("+--------------+------------------------+-----------------------------+--------------------+")
    print("|    Metric    |   Multithreading (ns)  |   Non-Multithreading (ns)   |   Difference (ns)  |")
    print("+--------------+------------------------+-----------------------------+--------------------+")
    # Row 1 (Column 1, 2, 3, 4)
    print("|  Total Time  |", end = "")
    print(f"{str(total_multi).center(24)}|", end = "")
    print(f"{str(total_single).center(29)}|", end = "")
    print(f"{str(total_diff).center(20)}|")
    # Row 2 (Column 1, 2, 3, 4)
    print(f"| Average Time |", end = "")
    print(f"{str(int(avg_multi)).center(24)}|", end = "")
    print(f"{str(int(avg_single)).center(29)}|", end = "")
    print(f"{str(int(avg_diff)).center(20)}|")
    print("+--------------+------------------------+-----------------------------+--------------------+")

# =============================================================================
#                        MAIN PROGRAM EXECUTION FLOW
# =============================================================================

def main():
    multi_thread_t = run_multi_thread(10, 3)
    single_thread_t = run_single_thread(10)
    print_performance_table(multi_thread_t, single_thread_t)

# =============================================================================
#                           PROGRAM LAUNCHES HERE
# =============================================================================

if __name__ == "__main__":
    main()