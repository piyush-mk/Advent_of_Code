def sum_calibration_values(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            digits = [char for char in line if char.isdigit()]
            if digits:
                calibration_value = int(digits[0] + digits[-1])
                total += calibration_value

    return total

print(sum_calibration_values('2023/Day1/1_data.txt'))