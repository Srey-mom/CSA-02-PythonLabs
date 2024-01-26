# Given a string indicating a range of letters
input_str = input ("Enter a range of letters e.g., a-z: ") # alphabet = abcdefghijklmnopqrstuvwxyz
# Split the input into the start and end characters of the range (e.g., "a" and "z")
start_letter, end_letter = input_str.split('-')
# Convert the start_char and end_char to their ASCII values 
start_ascii = ord(start_letter)
end_ascii = ord(end_letter)
result_string = ''.join(chr(i) for i in range(ord(start_letter), ord(end_letter)+ 1 ))
# Display the result
print ("A range letter is", result_string)
