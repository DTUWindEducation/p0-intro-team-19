# Q1
def greet(name):
    return (print(f'Hello, {name}!'))
    
# Q2
def goldilocks(bed_length):
    output = ""
    if bed_length<140:
        output = "Too small"
        print(output)
    elif bed_length>150:
        output = "Too large"
        print(output)
    else:
        output = "Just right"
        print(output)
    return (output)
    
# Q3
def square_list(number_list):
    squared_numbers = []
    for numbers in number_list:
        squared_numbers.append(numbers**2)
    print(squared_numbers)
    return (squared_numbers)

# Q4
def fibonacci_stop(max):
    sequence = [1, 1]
    while True:
        new_number = sequence[-1] + sequence[-2]
        if new_number > max:
            break
        sequence.append(new_number)
    print(sequence)
    return(sequence)

# Q5
def clean_pitch(pitch_angles, status_signals):
    cleaned_list = []
    for pitch, status in zip(pitch_angles,status_signals):
        if status != 0 and (pitch < 0 or pitch > 90):
            cleaned_list.append(-999)
        else:
            cleaned_list.append(pitch)
    print(cleaned_list)
    return(cleaned_list)
