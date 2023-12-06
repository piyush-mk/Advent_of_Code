DIGITS_MAP = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8", 
    "nine": "9"
}

def extract_digits(line: str) -> int:
    for digit in DIGITS_MAP:
        line = line.replace(digit, DIGITS_MAP[digit])
    digits = [s for s in line if s.isnumeric()]
    return int(digits[0] + digits[-1])

def sum_calibration_values_from_file(file_path: str) -> int:
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += extract_digits(line.strip())
    return total

print(sum_calibration_values_from_file('2023/Day1/1_data.txt'))