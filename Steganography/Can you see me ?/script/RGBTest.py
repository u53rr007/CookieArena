from PIL import Image

def extract_pixel_colors(image_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Convert the image to RGB mode if it's not already
    img = img.convert('RGB')
    
    # Get image dimensions
    width, height = img.size
    print(f"Image size: {width} x {height}")
    
    # Extract and print pixel colors
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            print(f"Pixel at ({x}, {y}) - R: {r}, G: {g}, B: {b}")

# Example usage
extract_pixel_colors('<input file>')
