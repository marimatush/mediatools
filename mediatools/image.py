from PIL import Image
import os


def convert_image_to_webp(input_path, output_path=None, quality=80):
    if not os.path.isfile(input_path):
        print(f"❌ File not found: {input_path}")
        return

    if not output_path:
        output_path = os.path.splitext(input_path)[0] + ".webp"

    try:
        with Image.open(input_path) as img:
            img.save(output_path, format="WEBP", quality=quality)
            print(f"✅ Image converted: {output_path}")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
