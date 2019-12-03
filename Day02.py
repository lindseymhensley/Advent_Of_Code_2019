import time

# noinspection SpellCheckingInspection
_Intcode = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 2, 6, 19, 23, 1, 23,
            5, 27, 1, 27, 13, 31, 2, 6, 31, 35, 1, 5, 35, 39, 1, 39, 10, 43, 2, 6, 43, 47, 1,
            47, 5, 51, 1, 51, 9, 55, 2, 55, 6, 59, 1, 59, 10, 63, 2, 63, 9, 67, 1, 67, 5, 71,
            1, 71, 5, 75, 2, 75, 6, 79, 1, 5, 79, 83, 1, 10, 83, 87, 2, 13, 87, 91, 1, 10, 91,
            95, 2, 13, 95, 99, 1, 99, 9, 103, 1, 5, 103, 107, 1, 107, 10, 111, 1, 111, 5, 115,
            1, 115, 6, 119, 1, 119, 10, 123, 1, 123, 10, 127, 2, 127, 13, 131, 1, 13, 131, 135,
            1, 135, 10, 139, 2, 139, 6, 143, 1, 143, 9, 147, 2, 147, 6, 151, 1, 5, 151, 155, 1,
            9, 155, 159, 2, 159, 6, 163, 1, 163, 2, 167, 1, 10, 167, 0, 99, 2, 14, 0, 0]

# sets program back to 1202 program alarm state
_Intcode[1] = 12
_Intcode[2] = 2
_OpCodes = (1, 2, 99)

# loop over the list and try to find op codes
for key, value in enumerate(_Intcode):
    if (key % 4) == 0:  # If True, this is an op code!
        if value in _OpCodes:  # Is it a known op code?
            print(f"Received OpCode {value}")
            time.sleep(0.25)
            if value == 1:  # perform addition
                inputOne = _Intcode[_Intcode[key + 1]]
                inputTwo = _Intcode[_Intcode[key + 2]]
                print(f"Input values {inputOne} and {inputTwo} found!")
                time.sleep(.25)
                print("Executing addition commands...")
                time.sleep(.5)
                _Intcode[_Intcode[key + 3]] = inputOne + inputTwo
                print("Output stored.")
                time.sleep(0.25)
            if value == 2:  # perform multiplication
                inputOne = _Intcode[_Intcode[key + 1]]
                inputTwo = _Intcode[_Intcode[key + 2]]
                print(f"Input values {inputOne} and {inputTwo} found!")
                time.sleep(0.25)
                print("Executing multiplication commands...")
                time.sleep(0.5)
                _Intcode[_Intcode[key + 3]] = inputOne * inputTwo
                print("Output stored.")
                time.sleep(0.25)
            if value == 99:
                print("Operation Paused.")
                print(f"Final Calculation: {_Intcode[0]}")
                print("Operation Terminated.")
                break
        else:
            raise Exception(f"ERROR! Unknown OpCode Used! -> {value}")
