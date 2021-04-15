while True: # Create a loop that disallows values ​​other than numbers !!!!! 111!
    try:
        x = y = int(input('Please enter an integer: ')) # We get the number that the user entered
    except ValueError:
        print('Only integer numbers are allowed for input')
    else:
        break
x = abs(x) # Getting rid of negativity
result = [] # Create an empty list

# Decimal to Binary Conversion Block
result.append(x % 2) # We perform the first division
while x >= 2: # Subsequent up to x> = 2 in parallel filling the list with residuals
    x = x//2
    result.append(x % 2)
result.reverse() # Reverse the list for correct display
z = '' # Create an empty string P.s. idk how to do better :D
for i in result: # Fill the string with numbers from the expanded list
    z+=str(i)
print(str(y) + ' in binary: -' + str(z)) if y < 0 else print(str(y) + ' in binary: ' + str(z)) # We look at what was the input < or > 0 and display the result
