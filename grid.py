from PIL import Image, ImageDraw

def create_grid_image(image_width, image_height, rows, cols, line_color=(0, 0, 0), line_width=2, output_path="grid.png"):
    # Create a blank image with white background
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)
    
    # Calculate the width and height of each cell
    cell_width = image_width / cols
    cell_height = image_height / rows
    
    # Draw the horizontal lines
    for row in range(1, rows):
        y = int(row * cell_height)
        draw.line([(0, y), (image_width, y)], fill=line_color, width=line_width)
    
    # Draw the vertical lines
    for col in range(1, cols):
        x = int(col * cell_width)
        draw.line([(x, 0), (x, image_height)], fill=line_color, width=line_width)
    
    # Save the image
    image.save(output_path)
    print(f"Grid image saved to {output_path}")

# Example usage
image_width = 1920
image_height = 1080
rows = 6
cols = 5

create_grid_image(image_width, image_height, rows, cols)
