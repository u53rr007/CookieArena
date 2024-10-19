# Open the hex.png file in binary mode
with open("<input file>", "rb") as file:
    data = file.read()

# Convert the content into a list of hexadecimal numbers
numbers = [hex(byte) for byte in data]

# Remove numbers at even positions
filtered_numbers = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

# Write the new content to the clean_hex.png file
with open("<output file>", "wb") as file:
    # Convert the filtered hexadecimal numbers back to bytes before writing
    cleaned_data = bytes(int(num, 16) for num in filtered_numbers)
    file.write(cleaned_data)
