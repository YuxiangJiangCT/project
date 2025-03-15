import csv
import re

def parse_csv(file_path, file_name, pump1_choice, pump2_choice):
    """
    Parse CSV file and return client name, run ID, and time series data list
    """
    client_name = None
    run_id = None
    data_records = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        first_row = next(reader, None)
        if first_row and len(first_row) > 1:
            header_info = first_row[1]
            match = re.match(r'([A-Za-z]+)_([A-Za-z0-9]+)', header_info)
            if match:
                client_name = match.group(1)
                run_id = match.group(2)
            else:
                match = re.match(r'([A-Za-z]+)_([A-Za-z0-9]+)', file_name)
                if match:
                    client_name = match.group(1)
                    run_id = match.group(2)
        
        next(reader, None)

        headers = next(reader, None)
        
        for row in reader:
            if len(row) >= 7: 
                try:
                    time_stamp = float(row[0])
                    parameter = row[2]
                    process_value = float(row[4])
                    units = row[6]
                    
                    if parameter == "Pump1":
                        parameter = pump1_choice
                    elif parameter == "Pump2":
                        parameter = pump2_choice
                    
                    data_records.append({
                        "run_id": run_id,
                        "time_stamp": time_stamp,
                        "parameter": parameter,
                        "process_value": process_value,
                        "units": units
                    })
                except (ValueError, IndexError) as e:
                    print(f"Skipping invalid row: {row}, Error: {e}")
                    continue
    
    return client_name, run_id, data_records