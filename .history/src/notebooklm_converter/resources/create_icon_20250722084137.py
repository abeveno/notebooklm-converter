# Simple text-based icon placeholder
# In a real project, you would replace this with actual icon files:
# - icon.ico (for Windows)
# - icon.icns (for macOS) 
# - icon.png (for Linux)

# For now, create a simple 64x64 PNG icon using PIL
import os
from PIL import Image, ImageDraw, ImageFont

def create_simple_icon():
    """Create a simple icon for the application"""
    # Create a 64x64 image with a blue background
    size = 64
    image = Image.new('RGBA', (size, size), (65, 105, 225, 255))  # Royal blue
    draw = ImageDraw.Draw(image)
    
    # Draw a simple book-like shape
    # Book spine (left side)
    draw.rectangle([8, 12, 18, 52], fill=(139, 69, 19, 255))  # Brown
    
    # Book pages
    draw.rectangle([18, 12, 56, 52], fill=(255, 255, 255, 255))  # White
    draw.rectangle([20, 16, 54, 48], fill=(240, 240, 240, 255))  # Light gray
    
    # Draw some lines to represent text
    for y in range(20, 45, 4):
        draw.line([24, y, 50, y], fill=(100, 100, 100, 255), width=1)
    
    # Add a small "AI" text to represent NotebookLM
    try:
        # Try to use a font if available
        font = ImageFont.truetype("arial.ttf", 8)
        draw.text((42, 36), "AI", fill=(65, 105, 225, 255), font=font)
    except:
        # Fallback if font not available
        draw.text((42, 36), "AI", fill=(65, 105, 225, 255))
    
    return image

if __name__ == "__main__":
    # Create the icon and save it
    icon = create_simple_icon()
    
    # Save in different formats for different platforms
    base_path = os.path.dirname(__file__)
    
    # PNG for general use
    icon.save(os.path.join(base_path, "icon.png"))
    
    # For Windows ICO format
    icon.save(os.path.join(base_path, "icon.ico"))
    
    print("Icon files created successfully!")
