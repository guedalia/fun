from PIL import Image, ImageDraw, ImageFont
import os

def create_puzzle_grid():
    # Create a new image with white background
    image_size = 800  # Each image will be resized to 800x800
    padding = 50
    grid_width = image_size * 3 + padding * 4
    grid_height = image_size * 3 + padding * 4
    
    # Create the main image
    main_image = Image.new('RGB', (grid_width, grid_height), 'white')
    draw = ImageDraw.Draw(main_image)

    # Load and place images in grid
    image_positions = [
        (0, 0, 1), (2, 0, 2),     # Top row (skip middle)
        (0, 1, 3), (1, 1, 4), (2, 1, 5),  # Middle row
        (0, 2, 6), (1, 2, 7), (2, 2, 8)   # Bottom row
    ]
    
    for pos in image_positions:
        x_pos, y_pos, img_num = pos
        try:
            # Load image
            img = Image.open(f"{img_num}.jpg")
            
            # Resize image maintaining aspect ratio
            img.thumbnail((image_size, image_size))
            
            # Calculate padding to center if image is not square
            x_pad = (image_size - img.width) // 2
            y_pad = (image_size - img.height) // 2
            
            # Calculate position in grid
            x = padding + x_pos * (image_size + padding) + x_pad
            y = padding + y_pos * (image_size + padding) + y_pad
            
            # Paste image
            main_image.paste(img, (x, y))
            
        except Exception as e:
            print(f"Error processing image {img_num}: {e}")

    # Save the final image
    main_image.save("puzzle_grid.jpg", quality=95, dpi=(300, 300))

if __name__ == "__main__":
    create_puzzle_grid()