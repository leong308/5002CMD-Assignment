import random

# =============================================================================
#                             HASH TABLE CLASS
# =============================================================================

class HashTable:
    # =============================================================================
    #                        HASH TABLE CLASS CONSTRUCTOR
    # =============================================================================
    def __init__(self, tb_size):
        self.tb_size = tb_size                      # Indicates the hash table's size
        self.table = [[] for _ in range(tb_size)]   # For separate chaining using list of lists
        self.collisions = 0                         # Used to store the amount of collision events

    # =============================================================================
    #         FOLDING TECHNIQUE HASH FUNCTION (RETURN BACK HASHED VALUE)
    # =============================================================================
    def hash_function(self, key_str):
        parts = []  # Initialize an empty list
        for i in range(0, len(key_str), 4):         # Increment 4 after every loop
            part = key_str[i:i + 4]                 # Cut the substring to the size of 4 on the base of current index
            parts.append(part)                      # Append the substring ino the parts list
        total = sum(int(part) for part in parts)    # Convert all substrings in the list back to integer and sum up all
        return total % self.tb_size                 # mod the value with table size to prevent overflow

    # =============================================================================
    #                 FUNCTION TO INSERT A VALUE INTO HASH TABLE
    # =============================================================================
    def insert_value(self, key_str):
        index = self.hash_function(key_str)
        if self.table[index]:                       # If the index is already occupied with any value or child
            self.collisions += 1                    # Increment collision count by 1
        self.table[index].append(key_str)           # Append the key into the table's index

# =============================================================================
#                     USED TO GENERATE RANDOM IC NUMBER
# =============================================================================

def gen_random_ic(table1, table2):
    keys = set()    # Create Empty Set

    """ Keep Generating IC Numbers Until 1000 Entries Reached """
    while len(keys) < 1000:
        """ Generate Year  **---------- """
        year = random.randint(0, 99)

        """ Generate Month --**-------- """
        month = random.randint(1, 12)

        """ Generate Day   ----**------ """
        if month in {1, 3, 5, 7, 8, 10, 12}:
            max_days = 31
        elif month in {4, 6, 9, 11}:
            max_days = 30
        else:
            if year % 4 == 0:   # When it is leap year (every 4 years)
                max_days = 29
            else:
                max_days = 28
        day = random.randint(1, max_days)

        """ Generate State Code    ------**---- """
        region = random.randint(0, 99)
        while region in {17, 18, 19, 20, 94, 95, 96, 97}:
            region = random.randint(0, 99)

        """ Generate Last 4 Digits --------**** """
        serial = random.randint(0, 9999)

        """ Combine Together """
        ic_number = f"{year:02d}{month:02d}{day:02d}{region:02d}{serial:04d}"

        """ Escape if IC Number Repeated """
        if ic_number in keys:
            continue

        """ Add Valid IC Number to Keys """
        keys.add(ic_number)

    """ Insert Key Data Into Tables + Hashing Process """
    for key in keys:
        table1.insert_value(key)
        table2.insert_value(key)

    return table1, table2

# =============================================================================
#                           CONSTANTS DECLARATION
# =============================================================================

TABLE1_SIZE = 1009
TABLE2_SIZE = 2003
TEST_ROUNDS = 10

# =============================================================================
#                        MAIN PROGRAM EXECUTION FLOW
# =============================================================================

def main():
    # Initialize two hash tables of sizes 1009 and 2003
    table1 = HashTable(TABLE1_SIZE)
    table2 = HashTable(TABLE2_SIZE)

    # Perform 10 rounds of insertion and record collisions for each round
    collisions_table1 = []
    collisions_table2 = []
    for r in range(1, TEST_ROUNDS + 1):
        # reset tables for each round
        table1 = HashTable(TABLE1_SIZE)
        table2 = HashTable(TABLE2_SIZE)
        table1, table2 = gen_random_ic(table1, table2)
        collisions_table1.append(table1.collisions)
        collisions_table2.append(table2.collisions)
        # (Optionally print collisions in each round here)

    # After 10 rounds, calculate total and average collisions
    total_coll1 = sum(collisions_table1)
    avg_coll1 = total_coll1 / len(collisions_table1)
    total_coll2 = sum(collisions_table2)
    avg_coll2 = total_coll2 / len(collisions_table2)

    """ Header """
    print("\n" + "=" * 40)
    print(f"{'Collisions / Size':<20} | {TABLE1_SIZE:>7} | {TABLE2_SIZE:>7}")
    print("=" * 40)

    """ Print For Every Round's Collisions Summary """
    for round_num in range(TEST_ROUNDS):
        # Get collision counts for this round
        coll1 = collisions_table1[round_num]
        coll2 = collisions_table2[round_num]

        # Print row with proper alignment
        print(f"Round {round_num + 1:<14} | {coll1:>7} | {coll2:>7}")

    """ Print For Total Collisions & Average """
    print("=" * 40)
    print(f"{'Total Collisions':<20} | {total_coll1:>7} | {total_coll2:>7}")
    print(f"{'Average Collisions':<20} | {avg_coll1:>7.1f} | {avg_coll2:>7.1f}")
    print("=" * 40)

# =============================================================================
#                           PROGRAM LAUNCHES HERE
# =============================================================================

if __name__ == "__main__":
    main()