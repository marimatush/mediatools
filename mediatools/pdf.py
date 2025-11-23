from PyPDF2 import PdfMerger
import os


def merge_pdfs_in_directory(input_dir, output_path=None):
    if not os.path.isdir(input_dir):
        print(f"❌ Directory not found: {input_dir}")
        return

    # Collect all PDF files
    pdf_files = [
        os.path.join(input_dir, f)
        for f in sorted(os.listdir(input_dir))
        if f.lower().endswith(".pdf")
    ]

    if not pdf_files:
        print(f"❌ No PDF files found in: {input_dir}")
        return

    if not output_path:
        output_path = os.path.join(input_dir, "merged.pdf")

    try:
        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(pdf)

        merger.write(output_path)
        merger.close()

        print(f"✅ PDFs merged: {output_path}")
    except Exception as e:
        print(f"❌ Failed to merge PDFs: {e}")
