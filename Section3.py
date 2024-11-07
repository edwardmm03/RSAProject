
def str_to_int(string):
    # convert string
    hex_values = []   # buffer to hold values
    for char in string:
        z = ord(char)   # convert char to ascii int
        hex_values.append(str(f'{z:x}'))   # add hex to buffer
    return int(''.join(hex_values))   # join all elements and return

def int_to_str(num):
    # Convert ascii values back to characters
    in_str = str(num)   # convert input to string
    string = ""   # string buffer to return
    for i in range(0, len(in_str), 2):
        z = "0x" + in_str[i] + in_str[i+1]   # create the hex number from pairs
        z = int(z, 16)   # convert hex to int
        string += chr(z)   # convert int to char and append to string
    return string   # return the string

# A quick driver that demonstrates the functionality
my_str = "abc def"
my_str_int = str_to_int(my_str)

print("String to convert:",my_str)

print("Converted int:",my_str_int)

print("Convert back to string:",int_to_str(my_str_int))
