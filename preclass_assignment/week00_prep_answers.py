# Q1
def greet(a):
    print(f'Hello, {a}!')

greet('world')

# Q2
def goldilocks(n):
    if n<140:
        print('Too small!')
    elif n>150:
        print('Too large!')
    else:
        print('Just right. :)')

goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

# Q3
def square_list(m):
    squared_numbers = []
    for n in m:
        squared_numbers.append(n**2)
    print(squared_numbers)

square_list([1, 2, 3])

# Q4
def fibonacci_stop(max):
    sequence = [1, 1]
    while True:
        n = sequence[-1] + sequence[-2]
        if n > max:
            break
        sequence.append(n)
    print(sequence)

fibonacci_stop(30)

# Q5
def clean_pitch(pitch_angles, status_signals):
    cleaned_list = []
    for pitch, status in zip(pitch_angles,status_signals):
        if status != 0 and (pitch < 0 or pitch > 90):
            cleaned_list.append(-999)
        else:
            cleaned_list.append(pitch)
    print(cleaned_list)

x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]
clean_pitch(x, status)