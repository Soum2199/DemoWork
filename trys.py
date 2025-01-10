#Python file

def shift_string(s, direction):
    shifted_string = []
    
    for char in s:
        if direction == 'left':
            # Shift left
            new_char = chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
        elif direction == 'right':
            # Shift right
            new_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            raise ValueError("Direction must be 'left' or 'right'")
        
        shifted_string.append(new_char)
    
    return ''.join(shifted_string)

# Example usage
s = "abcxyz"
left_shifted = shift_string(s, 'left')
right_shifted = shift_string(s, 'right')

print("Original:", s)
print("Left Shifted:", left_shifted)  # Output: "zabwyz"
print("Right Shifted:", right_shifted)  # Output: "bcdyza"