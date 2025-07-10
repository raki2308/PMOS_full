import csv
import os

def compare_csv_files(file1, file2):
    # Helper function to read and skip rows
    def read_csv_skipping_rows(file_path, skip_rows):
        with open(file_path, 'r', newline='') as f:
            reader = csv.reader(f)
            # Skip specified number of rows
            for _ in range(skip_rows):
                next(reader)
            return list(reader)
    
    # Read files with skipped rows
    data1 = read_csv_skipping_rows(file1, skip_rows=3)
    data2 = read_csv_skipping_rows(file2, skip_rows=1)
    
    # Initialize differences list
    differences = []
    
    # Compare row counts
    if len(data1) != len(data2):
        differences.append(f"Row count difference: File1 has {len(data1)} rows (after skip), File2 has {len(data2)} rows (after skip)")
    
    # Compare each row
    for i in range(min(len(data1), len(data2))):
        row1 = data1[i]
        row2 = data2[i]
        
        # Compare column counts in current row
        if len(row1) != len(row2):
            differences.append(f"Row {i+1} (after skip): Column count mismatch ({len(row1)} vs {len(row2)})")
            continue
        
        # Compare each cell in the row
        for j in range(len(row1)):
            if row1[j] != row2[j]:
                differences.append(
                    f"Row {i+1} (after skip), Column {j+1}: "
                    f"File1='{row1[j]}', File2='{row2[j]}'"
                )
    
    # Output results
    if differences:
        print("Differences found:")
        for diff in differences:
            print(f"• {diff}")
        print(f"\nTotal differences: {len(differences)}")
    else:
        print("Files are identical in the compared sections")

# Example usage:
# Hardcoded directory for file2
file2_dir = 'New Folder/'  # <-- Change this to your actual directory path

# Get file1 (in current directory) and file2 filename from user
file1 = input("Enter the filename for file1 (in current directory): ")
#file2_filename = input("Enter the filename for file2 (in directory x): ")
file2_filename = file1

# Build the full path for file2
file2 = os.path.join(file2_dir, file2_filename)

compare_csv_files(file1, file2)

