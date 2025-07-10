import csv
from collections import defaultdict

def verify_csv(file_path):
    # Read CSV file
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    if len(rows) < 2:
        print("Error: CSV must contain at least 2 rows")
        return
    
    # Convert to floats with rounding
    row1 = [round(float(val), 2) for val in rows[0]]
    row2 = [round(float(val), 2) for val in rows[1]]
    
    # Generate expected values for both rows
    expected_values_row1 = [round(i * 0.01, 2) for i in range(1, 181)]  # 0.01 to 1.80
    expected_values_row2 = [round(i * 0.01, 2) for i in range(180, 361)]  # 1.80 to 3.60
    
    # Count occurrences in both rows
    count_row1 = defaultdict(int)
    count_row2 = defaultdict(int)
    
    for val in row1:
        count_row1[val] += 1
    
    for val in row2:
        count_row2[val] += 1
    
    # Print verification report for Row 1
    print("============ ROW 1 VERIFICATION ============")
    print("Value\tActual Count\tExpected Count\tStatus")
    print("--------------------------------------------")
    row1_correct = True
    for val in expected_values_row1:
        count = count_row1[val]
        expected = 181
        status = "OK" if count == expected else f"ERROR: Expected {expected}, got {count}"
        
        if count != expected:
            row1_correct = False
        
        print(f"{val:.2f}\t{count}\t\t{expected}\t\t{status}")
    
    # Print verification report for Row 2
    print("\n============ ROW 2 VERIFICATION ============")
    print("Value\tActual Count\tExpected Count\tStatus")
    print("--------------------------------------------")
    row2_correct = True
    for val in expected_values_row2:
        count = count_row2[val]
        expected = 180
        status = "OK" if count == expected else f"ERROR: Expected {expected}, got {count}"
        
        if count != expected:
            row2_correct = False
        
        print(f"{val:.2f}\t{count}\t\t{expected}\t\t{status}")
    
    # Summary report
    total_expected = 32580  # 180 distinct values × 181 repetitions
    total1 = len(row1)
    total2 = len(row2)
    
    print("\n================ SUMMARY ================")
    print(f"Total entries in Row1: {total1} (Expected: {total_expected})")
    print(f"Total entries in Row2: {total2} (Expected: {total_expected})")
    print(f"Row1 pattern verification: {'PASSED' if row1_correct else 'FAILED'}")
    print(f"Row2 pattern verification: {'PASSED' if row2_correct else 'FAILED'}")
    
    # Check for unexpected values
    unexpected_row1 = set(count_row1.keys()) - set(expected_values_row1)
    unexpected_row2 = set(count_row2.keys()) - set(expected_values_row2)
    
    if unexpected_row1:
        print("\nUNEXPECTED VALUES IN ROW1:")
        for val in sorted(unexpected_row1):
            print(f"{val:.2f}: {count_row1[val]} occurrences")
    
    if unexpected_row2:
        print("\nUNEXPECTED VALUES IN ROW2:")
        for val in sorted(unexpected_row2):
            print(f"{val:.2f}: {count_row2[val]} occurrences")

# Usage example
verify_csv('header.csv')

