import csv
import re

def txt_to_csv(input_file, output_file):
    # Open the text file for reading and the CSV file for writing
    with open(input_file, 'r') as txtfile, open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header for the CSV
        csv_writer.writerow(["Simulation", "Round", "Informed"])
        
        simulation_count = 0  # Counter to track each simulation block
        for line in txtfile:
            # Check if the line indicates a new simulation
            if line.startswith("Simulating pushpull;"):
                simulation_count += 1  # New simulation, increment counter
            else:
                # Look for lines with "Round:x Informed:y"
                match = re.match(r"Round:(\d+) Informed:(\d+)", line)
                if match:
                    round_num = int(match.group(1))
                    informed_count = int(match.group(2))
                    # Write the data to the CSV file
                    csv_writer.writerow([simulation_count, round_num, informed_count])

# Convert the provided file
txt_to_csv('pushpull100.txt', 'pushpull100.csv')
