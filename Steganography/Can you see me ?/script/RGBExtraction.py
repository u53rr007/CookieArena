from PIL import Image

def extract_blue_channel_flat(image_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Convert the image to RGB mode if it's not already
    img = img.convert('RGB')
    
    # Get image dimensions
    width, height = img.size
    print(f"Image size: {width} x {height}")
    
    # Create an empty array to store blue values
    blue_channel_flat = []
    
    # Extract and store only the blue channel values in a flat array
    for y in range(height):
        for x in range(width):
            _, _, b = img.getpixel((x, y))  # Ignore red and green, keep blue
            blue_channel_flat.append(b)
    
    return blue_channel_flat

# Example usage
blue_values_flat = extract_blue_channel_flat('<input png>')

# Print blue values separated by spaces
print(' '.join(map(str, blue_values_flat)))
