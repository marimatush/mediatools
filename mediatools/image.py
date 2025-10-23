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


def merge_images_to_pdf(input_dir, output_path=None):
    if not os.path.isdir(input_dir):
        print(f"❌ Directory not found: {input_dir}")
        return

    # Collect image files (JPG, JPEG, PNG)
    image_files = [
        os.path.join(input_dir, f)
        for f in sorted(os.listdir(input_dir))
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    if not image_files:
        print(f"❌ No image files found in: {input_dir}")
        return

    if not output_path:
        output_path = os.path.join(input_dir, "merged_images.pdf")

    try:
        images = [Image.open(f).convert("RGB") for f in image_files]
        first_image = images[0]
        rest_images = images[1:]

        first_image.save(output_path, save_all=True, append_images=rest_images)
        print(f"✅ PDF created: {output_path}")
    except Exception as e:
        print(f"❌ Failed to create PDF: {e}")
