from PIL import Image
import os

# Target maximum width and height for thumbnails
max_size = (400, 400)  # Adjust if needed

# Loop through files in current directory
for filename in os.listdir('.'):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            img = Image.open(filename)
            img.thumbnail(max_size)  # Resize while maintaining aspect ratio

            # Remove metadata (optional: reduces file size)
            img_without_exif = Image.new(img.mode, img.size)
            img_without_exif.putdata(list(img.getdata()))

            # Save .webp in the same directory
            webp_path = os.path.splitext(filename)[0] + '.webp'
            img_without_exif.save(webp_path, 'WEBP', quality=80)

            print(f"Converted and compressed {filename} -> {webp_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


# import os

# # Define which extensions you want to delete
# extensions_to_delete = ('.png', '.jpg', '.jpeg')

# # Loop through all files in the current directory
# for filename in os.listdir('.'):
#     if filename.lower().endswith(extensions_to_delete):
#         try:
#             os.remove(filename)
#             print(f"Deleted {filename}")
#         except Exception as e:
#             print(f"Error deleting {filename}: {e}")
