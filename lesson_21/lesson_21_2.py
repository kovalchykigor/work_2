from datetime import datetime
import os

def find_special_line_and_write_to_file(input_file_name, marker:str, output_file_name):
    delete_file(output_file_name)
    with open(input_file_name, 'r') as file:
        for line in file:
            if marker in line:
                write_data_to_file(output_file_name, line)


def extract_time(line):
    start_index = line.find('Timestamp ') + len('Timestamp ')
    if start_index < len('Timestamp '):  # 'Timestamp ' not found
        return None
    time_str = line[start_index:start_index + 8]
    if len(time_str) != 8:  # Incorrect length
        return None
    try:
        return datetime.strptime(time_str, '%H:%M:%S')
    except ValueError:
        return None


def delete_file(file_name):
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} has been deleted")
        else:
            print(f"Error deleting {file_name} does not exists.")
    except Exception as e:
        print(f"Error deleting {file_name}: {e}")


def write_data_to_file(file_name, new_line, message=""):
    with open(f'{file_name}', 'a') as file:
        file.write(f'{message} {new_line}')


def return_log_file(file_name_to_read, file_name_to_write):
    delete_file(file_name_to_write)
    with open(file_name_to_read, 'r') as file:
        lines = file.readlines()

    previous_time = None
    seen_lines = set()  # Use a set to keep track of unique lines

    for line in reversed(lines):
        current_time = extract_time(line)
        if current_time is None:
            continue  # Skip lines with invalid or missing timestamps
        if previous_time is not None:
            time_difference = current_time - previous_time
            seconds = int(time_difference.total_seconds())
            if seconds > 31 and seconds < 33:
                if line not in seen_lines:
                    write_data_to_file(file_name_to_write, line, 'WARNING')
                    seen_lines.add(line)
            elif seconds >= 33:
                if line not in seen_lines:
                    write_data_to_file(file_name_to_write, line, "ERROR")
                    seen_lines.add(line)
        previous_time = current_time


find_special_line_and_write_to_file("hblog.txt", "Key TSTFEED0300|7E3E|0400", "Key_lines.txt")
return_log_file('Key_lines.txt', 'hb_test.log')
