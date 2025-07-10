import csv

def generate_new_entries(existing_length):
    """Generate new entries to extend the CSV to 32660 values per row"""
    distinct_values = 180  # 0.01 to 1.80
    repetitions = 181      # Each value repeats 181 times
    total_required = distinct_values * repetitions  # 180 * 181 = 32660
    remaining = total_required - existing_length
    
    if remaining <= 0:
        return [], []  # No new entries needed

    # Generate new data for first row (181 repetitions per value)
    current_block = existing_length // repetitions
    position_in_block = existing_length % repetitions
    new_row1 = []
    
    # Complete current block
    if position_in_block > 0:
        current_value = (current_block + 1) * 0.01
        remaining_in_block = repetitions - position_in_block
        new_row1.extend([round(current_value, 2)] * min(remaining_in_block, remaining))
    
    # Generate full blocks
    full_blocks_needed = (remaining - len(new_row1)) // repetitions
    for block_index in range(current_block + 1, current_block + 1 + full_blocks_needed):
        value = block_index * 0.01
        new_row1.extend([round(value, 2)] * repetitions)
    
    # Generate any remaining partial block
    remaining_values = remaining - len(new_row1)
    if remaining_values > 0:
        last_value = (current_block + 1 + full_blocks_needed) * 0.01
        new_row1.extend([round(last_value, 2)] * remaining_values)

    # Generate new data for second row (1.80 to 3.60)
    new_row2 = []
    start_value = 1.80
    end_value = 3.60
    step = 0.01
    sequence_length = int((end_value - start_value) / step) + 1  # 181 values
    
    for i in range(remaining):
        # Calculate position in sequence (0-180)
        seq_index = (existing_length + i) % sequence_length
        value = start_value + seq_index * step
        new_row2.append(round(value, 2))

    return new_row1, new_row2

# Load existing data
filename = 'header.csv'  # Replace with your CSV filename
existing_row1 = []
existing_row2 = []

try:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        if rows:
            existing_row1 = [float(val) for val in rows[0]]
            if len(rows) > 1:
                existing_row2 = [float(val) for val in rows[1]]
except FileNotFoundError:
    print("Creating new file...")

# Generate new entries
new_row1, new_row2 = generate_new_entries(len(existing_row1))

# Combine existing and new data
combined_row1 = existing_row1 + new_row1
combined_row2 = existing_row2 + new_row2

# Write updated data back to CSV
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([f"{x:.2f}" for x in combined_row1])
    if combined_row2:  # Only write second row if it has data
        writer.writerow([f"{x:.2f}" for x in combined_row2])

print(f"Added {len(new_row1)} new entries to each row")
print(f"Total entries per row: {len(combined_row1)}")

