
from PIL import Image # type: ignore

def center_images_for_gif(image_paths, output_path, duration=500):
    images = [Image.open(img) for img in image_paths]
    
    # Find the maximum width and height among all images
    max_width = max(image.width for image in images)
    max_height = max(image.height for image in images)
    
    centered_images = []
    
    for img in images:
        # Create a new image with the maximum dimensions
        new_image = Image.new('RGBA', (max_width, max_height), (255, 255, 255, 0)) # Transparent background
        
        # Calculate position to paste the image centered
        paste_position = (
            (max_width - img.width) // 2,
            (max_height - img.height) // 2
        )
        
        # Paste the image onto the new image
        new_image.paste(img, paste_position)
        centered_images.append(new_image)

    # Save as GIF
    centered_images[0].save(
        output_path,
        save_all=True,
        append_images=centered_images[1:],
        duration=duration,
        loop=0,
        transparency=0
    )

# Example usage
image_files = ["image11.png", "image22.png", "image33.png"]
output_gif = "output_image.gif"
center_images_for_gif(image_files, output_gif)
